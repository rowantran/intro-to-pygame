import os
import pygame
import sys

pygame.init()

font = pygame.font.Font(None, 24)

def check_standing_on_block(s1, s2):
    return s2.rect.collidepoint((s1.rect.centerx, s1.rect.bottom))

class Player(pygame.sprite.Sprite):
    """Represents the user-controlled character."""

    def __init__(self, x, y):
        super(Player, self).__init__()
        self.image = pygame.image.load(os.path.join('img', 'mario.bmp')).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.dx = 0
        self.dy = 0

        self.coins_collected = 0

    def accelerate(self, x, y):
        self.dx += x
        self.dy += y

    def gravity(self):
        if self.dy == 0:
            self.dy = 1
        else:
            self.accelerate(0, 0.35)

        # Check if on a wall
        blocks_hit = pygame.sprite.spritecollide(self, self.walls, False, check_standing_on_block)
        standing_on_block = False
        for block in blocks_hit:
            standing_on_block = True
        
        # Check if on ground
        if (self.rect.y >= RESOLUTION[1] - self.rect.height and self.dy >= 0) or (standing_on_block and self.dy >= 0):
            self.dy = 0

    def update(self):
        self.gravity()

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

        coins_hit = pygame.sprite.spritecollide(self, self.coins, True)
        for coin in coins_hit:
            self.coins_collected += 1
        
        self.draw_coins()

    def draw_coins(self):
        screen.blit(coin_image, (616, 50))
        text = font.render(str(self.coins_collected), 1, (255, 255, 255))
        screen.blit(text, (655, 50))

class Wall(pygame.sprite.Sprite):
    """Represents a wall that Player collides with."""
    def __init__(self, x, y, width, height):
        super(Wall, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Coin(pygame.sprite.Sprite):
    """Represents a coin that Player can collect."""
    def __init__(self, x, y):
        super(Coin, self).__init__()

        self.image = pygame.image.load(os.path.join('img', 'coin.bmp'))
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
coins = pygame.sprite.Group()

# Load images
coin_image = pygame.image.load(os.path.join('img', 'coin.bmp'))

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
wall = Wall(200, 500, 50, 50)
walls.add(wall)
sprite_list.add(wall)

wall = Wall(275, 450, 50, 50)
walls.add(wall)
sprite_list.add(wall)

wall = Wall(350, 400, 50, 50)
walls.add(wall)
sprite_list.add(wall)

# Coins
coin = Coin(300, 400)
coins.add(coin)
sprite_list.add(coin)

coin = Coin(330, 400)
coins.add(coin)
sprite_list.add(coin)

coin = Coin(360, 400)
coins.add(coin)
sprite_list.add(coin)

coin = Coin(390, 370)
coins.add(coin)
sprite_list.add(coin)

player.walls = walls
player.coins = coins

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
                player.accelerate(0, -6)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.accelerate(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.accelerate(-3, 0)

    screen.fill(BLACK)
    sprite_list.update()
    sprite_list.draw(screen)
    pygame.display.flip()

    clock.tick(60)
