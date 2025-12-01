import pygame
import sys
from time import sleep

from ship import Ship
from bullet import Bullet
from settings import Settings
from soundManager import soundManager
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.sound_manager = soundManager()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height), pygame.RESIZABLE
        )
        pygame.display.set_caption("Alien Invasion")
         
        self.fullscreen = False

        import os
        from path_utils import resource_path
        
        # Set window icon
        try:
            icon_path = resource_path(os.path.join("images", "AlienInvasion.logo.png"))
            icon = pygame.image.load(icon_path)
            pygame.display.set_icon(icon)
        except FileNotFoundError:
            print("Icon image not found.")

        try:
            self.background = pygame.image.load(resource_path(os.path.join("images", "bg_space.jpg")))
        except FileNotFoundError:
            print(
                "Background image not found. Please place 'bg_space.jpg' in the 'images' folder."
            )
            self.background = None

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_event()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.settings.screen_width = event.w
                self.settings.screen_height = event.h
                self.ship.resize()
                self.sb.resize()
                self.play_button.resize()

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            pygame.mouse.set_visible(False)
            # Reset stats
            self.stats.reset_stats()
            self.stats.game_active = True

            # Remove aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_F11:
            self._toggle_fullscreen()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
            self.sound_manager.bullet_sound.play()

    def _toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode."""
        if not self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            self.fullscreen = True
        else:
            self.screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
            self.settings.screen_width = 1200
            self.settings.screen_height = 800
            self.fullscreen = False
        
        # Update ship's screen reference and position
        self.ship.resize()
        
        # Note: Existing aliens might be in weird positions, but for now we just let them be.
        # Ideally we might want to recreate the fleet or adjust their positions, 
        # but simply resizing the ship is the critical part for gameplay not breaking.

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()  # Update position of bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check for any bullets that have hit aliens.
        #   If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for alien in collisions.values():
                self.stats.score += self.settings.alien_points * len(alien)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self.aliens.empty()
            self.settings.increase_speed()
            self._create_fleet()
            self.ship.center_ship()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """Update the position of all aliens in the fleet."""
        self._check_fleet_edge()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ship_left > 0:

            # Decrement ships_left, and update scoreboard.
            self.stats.ship_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and ships
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            # Player lost all lives
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

            # Reset full game state
            self.settings.initialise_dynamic_settings()  # Reset speed
            self.stats.reset_stats()  # Reset score and ships
            self.aliens.empty()
            self.bullets.empty()
            self.ship.center_ship()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this same as if the ship got hit
                self._ship_hit()
                break

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change its direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  # Reverse the direction

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 1.4 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.sb.show_score()
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()
        self.aliens.draw(self.screen)

        # draw the button if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
