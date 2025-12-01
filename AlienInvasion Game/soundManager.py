import pygame


class soundManager:

    def __init__(self):
        pygame.mixer.init()

        import os
        from path_utils import resource_path
        self.bullet_sound = pygame.mixer.Sound(resource_path(os.path.join("Sfx", "lowRandom.ogg")))
        self.bullet_sound.set_volume(0.5)
