import pygame
from random import randint
BLACK = (0,0,0)

class Tiniball(pygame.sprite.Sprite):
    def  __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.rect = self.image.get_rect()
        self.speed =[randint(4,8),randint(-8,8)]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def bounce(self):
        self.speed[0] = -self.speed[0]
        self.speed[1] = randint(-8,8)
        

