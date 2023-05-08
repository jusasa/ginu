import pygame, sys, random
from setting import *
from level import Level
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('진우 키우기')
        
        self.level = Level()
    def run(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
    