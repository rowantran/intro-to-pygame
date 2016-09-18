import os
import pygame
import sys

pygame.init()

# Set up sprites
player_sprite = pygame.image.load(os.path.join('img', 'Mario_Sprite.bmp'))

# Set up screen
RESOLUTION = [800, 600]
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('Platformer')

# Define colors
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    """Represents the user-controlled character."""

    def __init__(self, x, y):
        super(Player, self).__init__()
        self.image = pygame.image.load(os.path.join('img', 'Mario_Sprite.bmp'))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.dx = 0
        self.dy = 0

        self.walls = None

    def accelerate(self, x, y):
        """Change the velocity of the player."""
        self.dx += x
        self.dy += y

    def update(self):
        """Updates the position of the player."""
        self.rect.x += self.dx
        self.rect.y += self.dy

# Instantiate player and add to list of sprites
sprite_list = pygame.sprite.Group()

player = Player(100, 100)
sprite_list.add(player)

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
