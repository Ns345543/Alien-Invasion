class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # setting the speed of a ship
        self.ship_limit = 3

        # Bullets settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = "red"

        # limit the number of bullets
        self.bullets_allowed = 4

        # Alien speed
        self.fleet_drop_speed = 10

        # How quickly the game speed up
        self.speed_scale = 1.2

        # How quickly the Alien points increase
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        self.ship_speed = 0.9
        self.bullet_speed = 1.0
        self.alien_speed = 1.0

        # fleet direction of 1 represent right and -1 represent left
        self.fleet_direction = 1

        # scoring points
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien score value"""
        self.alien_speed *= self.speed_scale
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_points = int(self.score_scale * self.alien_points)