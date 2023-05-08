import pygame
from setting import *
from player import Player

class Level():
    
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.sprite = pygame.sprite.Group()
        self.setup()
    def setup(self):
        self.player = Player((640,360), self.sprite)
    
    def run(self, dt):
        self.display_surface.blit(bg,(0,0))
        self.sprite.draw(self.display_surface)
        self.sprite.update(dt)
        