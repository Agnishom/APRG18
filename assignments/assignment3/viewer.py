import pygame, sys, os
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1366, 768))

player = pygame.image.load(os.path.join("test.png"))
player.convert()

while True:
    screen.blit(player, (10, 10))
    pygame.display.flip()
    event = pygame.event.wait()
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            break
    for event in pygame.event.get():
           if event.type == QUIT:
               break
           elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   break


pygame.quit()
