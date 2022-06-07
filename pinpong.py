import pygame
import random

pygame.init()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
FPS = 40

W = 800
H = 600

scr = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
player_w = 400
player_h = 590
block_w = 50
block_h = 100
boll_w = 400
boll_h = 400
speed = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.bottom = player_h
        self.rect.x = player_w

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 5
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > W:
            self.rect.right = W


class Boll(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (boll_w, boll_h)
        self.speed_x = 0
        self.speed_y = 0
        self.rect.x = boll_w
        self.rect.y = boll_h

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.speed_x += 1
            self.speed_y -= 1
        if self.rect.right > W:
            self.speed_x = -1
        if self.rect.top <= 0:
            self.speed_y += 1
        if self.rect.left <= 0:
            self.speed_x += 1
        if self.rect.bottom >= H:
            self.speed_y -= 1


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (block_w, block_h)


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 3))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()


player = Player()
boll = Boll()
wall = Wall()
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

blocks.add(boll)
all_sprites.add(player)

for i in range(11):
    block = Block()
    blocks.add(block)
    block_w += 70
print(blocks)
score = 0
game = True
while game:

    pygame.display.flip()
    scr.fill(BLACK)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False

    colaide = pygame.sprite.spritecollideany(boll, all_sprites)
    if colaide:
        score += 1
        boll.rect.x -= 10
        boll.rect.y += 10
        print(score)

    blocks.draw(scr)
    blocks.update()
    all_sprites.draw(scr)
    all_sprites.update()
