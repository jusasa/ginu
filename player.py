import pygame
from setting import *
from surpport import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self,pos, group):
        super().__init__(group)
        
        self.import_assets()
        self.status = 'right'
        self.frame_index = 0
        
        self.image = self.animation[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        
        self.dirt = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 350
        
    def import_assets(self):
        self.animation = {'left': [], 'right' : []}
        
        for anime in self.animation.keys():
            full_path = 'resourse\\images\\character\\' + anime
            self.animation[anime] = import_folder(full_path)
     
    def animate(self,dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animation[self.status]):
            self.frame_index = 0
        self.image = self.animation[self.status][int(self.frame_index)]       
    def input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_w]:
            self.dirt.y = -1
        elif key[pygame.K_s]:
            self.dirt.y = 1
        else:
            self.dirt.y = 0
            
        if key[pygame.K_a]:
            self.dirt.x = -1
        elif key[pygame.K_d]:
            self.dirt.x = 1
        else:
            self.dirt.x = 0
        
    def move(self, dt):
        
        if self.dirt.magnitude() > 0:
            self.dirt = self.dirt.normalize()
            
        # horizontal
        self.pos.x += self.dirt.x * self.speed * dt
        self.rect.centerx = self.pos.x
        
        # vertical    
        self.pos.y += self.dirt.y * self.speed * dt
        self.rect.centery = self.pos.y
        
    def update(self,dt):
        self.input()
        self.move(dt)
        self.animate(dt)