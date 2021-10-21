import pygame
from game_settings import Settings
import utilities
import snake
import controls
import food

from pygame.locals import (
    KEYDOWN,
    QUIT,
    K_q,
    K_c
)

# https://www.edureka.co/blog/snake-game-with-pygame/

pygame.init()
pygame.display.set_caption('Snake game by pmash')

_settings = Settings()
clock = pygame.time.Clock()
_snake = snake.Snake()
_food = food.Food(_settings.Display_Height, _settings.Display_Width, _settings.Snake_Block_Size)
_background_color = pygame.Color('lightsteelblue')
_surface = pygame.display.set_mode((_settings.Display_Width, _settings.Display_Height))


def gameLoop():
    game_over = False
    game_close = False

    x1 = int(_settings.Display_Width / 2)
    y1 = int(_settings.Display_Height / 2)
    x1_change = 0
    y1_change = 0

    while not game_over:

        while game_close == True:
            _surface.fill(_background_color)
            utilities.display_message("You Lost! Press Q-Quit or C-Play Again", pygame.Color('red'), _surface, _settings)
            utilities.display_score(_snake.Length - 1, _settings.Score_Font, _surface)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        game_over = True
                        game_close = False
                    if event.key == K_c:
                        _snake.__init__()
                        gameLoop()

        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True

            if event.type == KEYDOWN:
                x1_change, y1_change = controls.handle_control(event.key, _settings.Snake_Block_Size)

        if utilities.player_out_of_bounds(x1, y1, _settings):
            game_close = True

        x1 += x1_change
        y1 += y1_change
        _snake.add_node(x1, y1)

        if _snake.collided_with_self(x1, y1):
            game_close = True

        refresh_game(_surface, _snake, _food)

        if [x1, y1] == _food.Coordinate:
            _snake.eat_food()
            _food.set_coordinate(_settings.Display_Height, _settings.Display_Width, _settings.Snake_Block_Size)

        clock.tick(_snake.Speed)

    pygame.quit()
    quit()


def refresh_game(_surface: pygame.Surface, _snake: snake.Snake, _food: food.Food) :
    _surface.fill(_background_color)
    _food.draw(_surface, _settings.Snake_Block_Size)
    _snake.draw(_surface, _settings)
    utilities.display_score(_snake.Length - 1, _settings.Score_Font, _surface)
    pygame.display.update()


gameLoop()
