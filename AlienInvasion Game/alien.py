import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        import os
        base_path = os.path.dirname(__file__)
        try:
            self.image = pygame.image.load(os.path.join(base_path, "images", "alienShip.png"))
        except FileNotFoundError:
            print("Alien image not found. Using a placeholder.")
            self.image = pygame.Surface([60, 100])
            self.image.fill((0, 255, 0))
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
