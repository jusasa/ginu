import pygame
from setting import *
from player import Player

class Level:
    def __init__(self):
        self.displays = pygame.display.get_surface()
        self.sprite = pygame.sprite.Group()
        self.setup()
        
    def setup(self):
        self.player = Player((640,480),self.sprite)
    
    def run(self,dt):
        self.displays.blit(bg,(0,0))
        self.sprite.draw(self.displays)
        self.sprite.update(dt)
        