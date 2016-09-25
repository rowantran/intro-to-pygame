import pygame
import sys

pygame.init()

# Set up screen
RESOLUTION = [800, 600]
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('Platformer')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(60)
