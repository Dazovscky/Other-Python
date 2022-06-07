import random

import pygame
from pygame.locals import *
import sys
from os import path

img_dir = path.join(path.dirname(__file__) )
pygame.init()

vec = pygame.math.Vector2
HEIGHT = 700
WIDTH = 800
ACC = 1
FRIC = -1
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
player_img = pygame.image.load(path.join(img_dir, "dino.png")).convert()
cactus_img = pygame.image.load(path.join(img_dir, "cactus.png")).convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.transform.scale(player_img, (50, 50))
        self.rect = self.surf.get_rect()

        self.pos = vec((100, 580))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def move(self):
        self.acc = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.acc.y = -ACC
        if not pressed_keys[K_SPACE]:
            self.acc.y = ACC * 2

        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 20 * self.acc

        if self.pos.y >= 780:
            self.pos.y = 780
        if self.pos.y < 500:
            self.pos.y = 500

        self.rect.midbottom = self.pos


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.transform.scale(cactus_img, (30, 30))
        self.rect = self.surf.get_rect()
        self.rect.center = (WIDTH, 760)
        self.rect.x = random.randrange(0, 18)
        self.speedy = random.randrange(0, 8)

    def update(self):
        self.rect.x -= self.speedy
        if self.rect.left < 0:
            self.rect.x = WIDTH



PT1 = Platform()
P1 = Player()
W = Wall()

all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
walls.add(W)
all_sprites.add(P1)
all_sprites.add(PT1)
for i in range(10):
    all_sprites.add(W)



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                W.update()

    all_sprites.update()
    hits = pygame.sprite.spritecollide(P1, walls, True)
    if hits:
        run = False
    displaysurface.fill(WHITE)
    P1.move()
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()

    FramePerSec.tick(FPS)
