import pygame
import sys

pygame.init()

RESOLUTION = [800, 600]

screen = pygame.display.set_mode(RESOLUTION)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
