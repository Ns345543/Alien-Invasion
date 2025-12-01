import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        import os
        base_path = os.path.dirname(__file__)
        try:
            self.image = pygame.image.load(os.path.join(base_path, "images", "Ship.png"))
        except FileNotFoundError:
            print("Ship image not found. Using a placeholder.")
            self.image = pygame.Surface([60, 60])
            self.image.fill((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def resize(self):
        """Update the ship's position when the screen is resized."""
        self.screen_rect = self.screen.get_rect()
        self.center_ship()
