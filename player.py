import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, gruop):
        super().__init__(gruop)
        self.image = pygame.Surface((32,64))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(center = pos)
        self.dirc = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
    def input(self):
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_UP]:
            self.dirc.y = -1
        elif self.key[pygame.K_DOWN]:
            self.dirc.y = 1
        else:
            self.dirc.y = 0
            
        if self.key[pygame.K_LEFT]:
            self.dirc.x = -1
        elif self.key[pygame.K_RIGHT]:
            self.dirc.x = 1
        else:
            self.dirc.x = 0
    def move(self,dt):
        if self.dirc.magnitude() > 0:
            self.dirc = self.dirc.normalize()
        self.pos.x += self.dirc.x * self.speed * dt
        self.rect.centerx = self.pos.x
        self.pos.y += self.dirc.y * self.speed * dt
        self.rect.centery = self.pos.y
    def update(self, dt):
        self.input()
        self.move(dt)
        