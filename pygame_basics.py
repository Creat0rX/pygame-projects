import pygame
from pygame.locals import *

pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600

game_display = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption('My Game')

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and any([event.key == K_ESCAPE, event.key == K_q])):
            pygame.quit()
            quit()

while True:
    event_handler()
    pygame.display.update()