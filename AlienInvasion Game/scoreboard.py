import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for storing information
        self.text_color = (0, 255, 255)  # Neon Cyan
        self.font = pygame.font.SysFont("consolas", 28, bold=True)

        # prepare the inital score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_image_with_shadow(self, text):
        """Render text with a shadow effect."""
        shadow_color = (0, 0, 0)
        shadow_offset = 2
        
        # Render shadow
        shadow_image = self.font.render(text, True, shadow_color)
        # Render main text
        text_image = self.font.render(text, True, self.text_color)
        
        # Create a surface big enough to hold both
        width = text_image.get_width() + shadow_offset
        height = text_image.get_height() + shadow_offset
        final_image = pygame.Surface((width, height), pygame.SRCALPHA)
        
        final_image.blit(shadow_image, (shadow_offset, shadow_offset))
        final_image.blit(text_image, (0, 0))
        
        return final_image

    def prep_score(self):
        """Turned a score into a render image"""

        round_scr = round(self.stats.score, -1)
        score_str = "{:,}".format(round_scr)
        self.score_str = f"SCORE: {score_str}"
        self.score_image = self.prep_image_with_shadow(self.score_str)

        # Display the score at the top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turned a score into a render image"""

        high_scr = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_scr)
        self.high_score_str = f"HIGH SCORE: {high_score_str}"
        self.high_score_image = self.prep_image_with_shadow(self.high_score_str)

        # Center the high score at the top of the screen
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check if there is new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into image and render the image"""
        level_str = str(self.stats.level)
        self.level_str = f"LVL: {level_str}"
        self.level_image = self.prep_image_with_shadow(self.level_str)

        # Postion the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)



    def show_score(self):
        """Draw score, level and ships to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def resize(self):
        """Update scoreboard positions when screen is resized."""
        self.screen_rect = self.screen.get_rect()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
