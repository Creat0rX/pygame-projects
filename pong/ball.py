import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, colour, [0,0,width,height])

        self.velocity = [randint(4,8), randint(-8,8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bouncing(self):
        self.velocity[0] = -self.velocity[0]