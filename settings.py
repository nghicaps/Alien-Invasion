class Settings:
    def __init__(self):
        """initialize the game's static settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (41, 141, 201)
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10
        
        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly alien point values increase
        self.score_scale = 2

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """initialize settings that change throughout game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 2.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 1
    
    def increase_speed(self):
        """increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)