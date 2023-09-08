import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """class to manage ship"""
    
    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        self.rect = self.image.get_rect()

        self.center_ship()

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on movement flags"""
        # update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """center ship on screen"""
        # start each new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal postion
        self.x = float(self.rect.x)