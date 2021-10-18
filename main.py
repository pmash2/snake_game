import pygame
import time
import random

# https://www.edureka.co/blog/snake-game-with-pygame/

pygame.init()

color_white = (255, 255, 255)
color_light_blue = (50, 153, 213)
color_red = (255, 0, 0)
color_blue = (0, 0, 255)
color_yellow = (255, 255, 102)
color_green = (0, 255, 0)

snake_block = 10
snake_speed = 15

display_height = 400
display_width = 600

dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake game by pmash')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render(f"Your Score: {score}", True, color_yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for coord in snake_list:
        pygame.draw.rect(dis, color_blue, [
                         coord[0], coord[1], snake_block, snake_block])


def message(msg, color):
    _message = font_style.render(msg, True, color)
    dis.blit(_message, [display_width / 2, display_height / 2])


def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(
        0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(
        0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(color_light_blue)
            message("You Lost! Press Q-Quit or C-Play Again", color_red)
            your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(color_light_blue)
        pygame.draw.rect(dis, color_green, [
                         foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, display_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
