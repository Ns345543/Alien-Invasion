import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Set the dimmension and properties of a button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)    # Black background (transparent-ish logic handled by drawing rect)
        self.border_color = (57, 255, 20) # Neon Green
        self.text_color = (57, 255, 20)   # Neon Green
        self.font = pygame.font.SysFont("consolas", 32, bold=True)

        # Build the buttons rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button needs to be prepare only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        # Render text normally (Neon Green)
        self.msg_img_normal = self.font.render(msg, True, self.text_color)
        
        # Render text for hover (Black)
        self.msg_img_hover = self.font.render(msg, True, (0, 0, 0))
        
        self.msg_img_rect = self.msg_img_normal.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        # draw blank button and draw message
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            # Hover: Fill with Neon Green, Text is Black
            pygame.draw.rect(self.screen, self.border_color, self.rect, border_radius=10)
            self.screen.blit(self.msg_img_hover, self.msg_img_rect)
        else:
            # Normal: Black background (or transparent), Neon Border, Neon Text
            # We fill with black to cover game elements behind if needed, or just draw border.
            # Let's fill black to ensure readability.
            pygame.draw.rect(self.screen, self.button_color, self.rect, border_radius=10)
            pygame.draw.rect(self.screen, self.border_color, self.rect, 2, border_radius=10)
            self.screen.blit(self.msg_img_normal, self.msg_img_rect)

    def resize(self):
        """Update button position when screen is resized."""
        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.msg_img_rect.center = self.rect.center
