import pygame
import time
import random


pygame.init()


dis_w = 800
dis_h = 600

dis = pygame.display.set_mode((dis_w, dis_h))
score_font = pygame.font.SysFont("comicsansms", 35)
pygame.display.set_caption('Snake')


YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


snake_block = 10




def block(random_block_x, random_block_y):
    pygame.draw.rect(dis, WHITE, [random_block_x, random_block_y, random_block_x, random_block_y])


def snake(snake_block, snake_List):
    for c in snake_List:
        pygame.draw.rect(dis, YELLOW, [c[0], c[1], snake_block, snake_block])


def eat_snake(eat_x, eat_y):
    pygame.draw.rect(dis, RED, [eat_x, eat_y, snake_block, snake_block])


def your_scor(score, level):
    value = score_font.render("Score: " + str(score), True, YELLOW)
    value2 = score_font.render("Level: " + str(level), True, YELLOW)
    dis.blit(value2, [350, 0])
    dis.blit(value, [0, 0])


clock = pygame.time.Clock()
game_over = False
def game():
    snake_speed = 20
    snake_x = int(dis_w / 2)
    snake_y = int(dis_h / 2)
    x1_c = 0
    y1_c = 0
    snake_List = []
    Len_snake = 1
    score = 0
    level = 1
    random_block_x = random.randrange(0, dis_w, 10)
    random_block_y = random.randrange(0, dis_h, 10)
    eat_x = random.randrange(0, dis_w, 10)
    eat_y = random.randrange(0, dis_h, 10)
    while not game_over:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_c = -10
                    y1_c = 0
                elif event.key == pygame.K_RIGHT:
                    x1_c = 10
                    y1_c = 0
                elif event.key == pygame.K_UP:
                    x1_c = 0
                    y1_c = -10
                elif event.key == pygame.K_DOWN:
                    x1_c = 0
                    y1_c = 10
                elif event.key == pygame.K_ESCAPE:
                    qiut()
        snake_x += x1_c
        snake_y += y1_c
        if snake_x >= dis_w:
            snake_x = 0
        elif snake_x < 0:
            snake_x = dis_w
        elif snake_y >= dis_h:
            snake_y = 0
        elif snake_y < 0:
            snake_y = dis_h

        clock.tick(snake_speed)
        dis.fill(BLACK)

        your_scor(score, level)

        eat_snake(eat_x, eat_y)
        snake(snake_block, snake_List)

        if len(snake_List) > Len_snake:
            del snake_List[0]

        pygame.display.update()
        snake_Head = []
        snake_Head.append(snake_x)
        snake_Head.append(snake_y)
        snake_List.append(snake_Head)
        if snake_y == eat_y and snake_x == eat_x:
            eat_x = random.randrange(0, dis_w, 10)
            eat_y = random.randrange(0, dis_h, 10)
            Len_snake += 1
            score += 1
            if score > 2:
                level += 1
        elif snake_x == random_block_x and snake_y == random_block_y:
            break
        if score > 0:
            block(random_block_x, random_block_y)
            snake_speed = 20
        elif score > 1:
            block(random_block_x, random_block_y)


game()
pygame.quit()
