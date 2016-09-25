import os
import pygame
import sys

pygame.init()

class Player(pygame.sprite.Sprite):
    """Represents the user-controlled character."""

    def __init__(self, x, y):
        super(Player, self).__init__()
        self.image = pygame.image.load(os.path.join('img', 'mario.bmp'))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.dx = 0
        self.dy = 0

        self.walls = None

    def accelerate(self, x, y):
        self.dx += x
        self.dy += y

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

# Define colors
BLACK = (0, 0, 0)

# Set up screen
RESOLUTION = [800, 600]
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('Platformer')

# Set up game objects
sprite_list = pygame.sprite.Group()

player = Player(50, 500)
sprite_list.add(player)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.accelerate(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.accelerate(3, 0)
            elif event.key == pygame.K_UP:
                player.accelerate(0, -3)
            elif event.key == pygame.K_DOWN:
                player.accelerate(0, 3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.accelerate(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.accelerate(-3, 0)
            elif event.key == pygame.K_UP:
                player.accelerate(0, 3)
            elif event.key == pygame.K_DOWN:
                player.accelerate(0, -3)

    screen.fill(BLACK)
    sprite_list.update()
    sprite_list.draw(screen)
    pygame.display.flip()
    
    clock.tick(60)
