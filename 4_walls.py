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

    def accelerate(self, x, y):
        self.dx += x
        self.dy += y

    def update(self):
        self.rect.x += self.dx
        blocks_hit = pygame.sprite.spritecollide(self, self.walls, False)
        for block in blocks_hit:
            if self.dx > 0:
                # Player moved right into a wall
                self.rect.right = block.rect.left
            else:
                # Player moved left into a wall
                self.rect.left = block.rect.right

        self.rect.y += self.dy
        blocks_hit = pygame.sprite.spritecollide(self, self.walls, False)
        for block in blocks_hit:
            if self.dy > 0:
                # Player moved down into a wall
                self.rect.bottom = block.rect.top
            else:
                # Player moved up into a wall
                self.rect.top = block.rect.bottom

class Wall(pygame.sprite.Sprite):
    """Represents a wall that Player collides with."""
    def __init__(self, x, y, width, height):
        super(Wall, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up screen
RESOLUTION = [800, 600]
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('Platformer')

# Set up game objects
sprite_list = pygame.sprite.Group()

player = Player(50, 500)
sprite_list.add(player)

walls = pygame.sprite.Group()

# Level boundaries
wall = Wall(0, 0, 10, 600)
walls.add(wall)
sprite_list.add(wall)

wall = Wall(10, 0, 790, 10)
walls.add(wall)
sprite_list.add(wall)

wall = Wall(790, 10, 10, 590)
walls.add(wall)
sprite_list.add(wall)

# Blocks
wall = Wall(200, 550, 50, 50)
walls.add(wall)
sprite_list.add(wall)

wall = Wall(275, 500, 50, 50)
walls.add(wall)
sprite_list.add(wall)

wall = Wall(350, 450, 50, 50)
walls.add(wall)
sprite_list.add(wall)

wall = Wall(425, 500, 50, 50)
walls.add(wall)
sprite_list.add(wall)

wall = Wall(500, 550, 50, 50)
walls.add(wall)
sprite_list.add(wall)

player.walls = walls

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

