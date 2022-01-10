import pygame
from pygame import *
import sys
from paddle import Paddle
from ball import Ball

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SIZE = (800, 600)
game_display = pygame.display.set_mode(SIZE)
pygame.display.set_caption("PONG")

paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 25
paddle1.rect.y = 250

paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 775
paddle2.rect.y = 250

ball = Ball(WHITE, 10, 10)
ball.rect.x = 400
ball.rect.y = 200

clock = pygame.time.Clock()

score1 = 0
score2 = 0

popping_sound = pygame.mixer.Sound('pop.wav')
scoring_sound = pygame.mixer.Sound('score.wav')

game_on = True

sprite_list = pygame.sprite.Group()

sprite_list.add(paddle1)
sprite_list.add(paddle2)
sprite_list.add(ball)

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_on = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        paddle1.paddles_moving_up(7)
    if keys[pygame.K_UP]:
        paddle2.paddles_moving_up(7)
    if keys[pygame.K_s]:
        paddle1.paddles_moving_down(7)
    if keys[pygame.K_DOWN]:
        paddle2.paddles_moving_down(7)

    sprite_list.update()

    if ball.rect.x >= 790:
        scoring_sound.play()
        score1 += 1
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 400
        ball.rect.y = 200

    if ball.rect.x <= 0:
        scoring_sound.play()
        score2 += 1
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 400
        ball.rect.y = 200

    if ball.rect.y >= 590:
        ball.velocity[1] = -ball.velocity[1]

    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        popping_sound.play()
        ball.bouncing()

    game_display.fill(BLACK)

    pygame.draw.line(game_display, WHITE, [400, 0], [400, 600], 5)

    sprite_list.draw(game_display)

    font = pygame.font.Font(None, 100)
    text = font.render(str(score1), 1, WHITE)
    game_display.blit(text, (320, 10))
    text = font.render(str(score2), 1, WHITE)
    game_display.blit(text, (450, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()