import pygame
import time
import random
from colors import Colors as MyColors
from game_settings import Settings
import utilities

# https://www.edureka.co/blog/snake-game-with-pygame/

pygame.init()
_settings = Settings()

snake_block = _settings.Snake_Block_Size
snake_speed = 15

dis = pygame.display.set_mode(
    (_settings.Display_Width, _settings.Display_Height))
pygame.display.set_caption('Snake game by pmash')

clock = pygame.time.Clock()


def our_snake(snake_block, snake_list):
    for coord in snake_list:
        pygame.draw.rect(dis, MyColors.Blue, [
                         coord[0], coord[1], snake_block, snake_block])


def gameLoop():
    game_over = False
    game_close = False

    x1 = _settings.Display_Width / 2
    y1 = _settings.Display_Height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_coord = utilities.get_food_coord(_settings)

    while not game_over:

        while game_close == True:
            dis.fill(MyColors.Light_Blue)
            utilities.display_message("You Lost! Press Q-Quit or C-Play Again",
                                      MyColors.Red, dis, _settings)
            utilities.display_score(
                snake_length - 1, _settings.Score_Font, dis)
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

        if x1 >= _settings.Display_Width or x1 < 0 or y1 >= _settings.Display_Height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(MyColors.Light_Blue)
        pygame.draw.rect(dis, MyColors.Green, [
                         food_coord[0], food_coord[1], snake_block, snake_block])

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
        utilities.display_score(snake_length - 1, _settings.Score_Font, dis)

        pygame.display.update()

        if x1 == food_coord[0] and y1 == food_coord[1]:
            food_coord = utilities.get_food_coord(_settings)
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
