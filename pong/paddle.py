import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, colour, [0,0,width,height])

        self.rect = self.image.get_rect()

    def paddles_moving_up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def paddles_moving_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 500:
            self.rect.y = 500