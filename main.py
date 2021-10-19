import pygame
from game_settings import Settings
import utilities
import snake
import controls
import food

# https://www.edureka.co/blog/snake-game-with-pygame/

pygame.init()

_settings = Settings()
clock = pygame.time.Clock()
_snake = snake.Snake()
_food = food.Food(_settings.Display_Height, _settings.Display_Width, _settings.Snake_Block_Size)

_surface = pygame.display.set_mode((_settings.Display_Width, _settings.Display_Height))
pygame.display.set_caption('Snake game by pmash')


def gameLoop():
    game_over = False
    game_close = False

    x1 = int(_settings.Display_Width / 2)
    y1 = int(_settings.Display_Height / 2)
    x1_change = 0
    y1_change = 0

    while not game_over:

        while game_close == True:
            _surface.fill(pygame.Color('lightsteelblue'))
            utilities.display_message("You Lost! Press Q-Quit or C-Play Again", pygame.Color('red'), _surface, _settings)
            utilities.display_score(_snake.Length - 1, _settings.Score_Font, _surface)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        _snake.__init__()
                        gameLoop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                x1_change, y1_change = controls.handle_control(event.key, _settings.Snake_Block_Size)

        if utilities.player_out_of_bounds(x1, y1, _settings):
            game_close = True

        x1 += x1_change
        y1 += y1_change
        _surface.fill(pygame.Color('lightsteelblue'))
        _food.draw(_surface, _settings.Snake_Block_Size)

        _snake.add_node(x1, y1)

        if _snake.collided_with_self(x1, y1):
            game_close = True

        _snake.draw(_surface, _settings)
        utilities.display_score(_snake.Length - 1, _settings.Score_Font, _surface)

        pygame.display.update()

        snake_head = [x1, y1]
        if snake_head == _food.Coordinate:
            _food.set_coordinate(_settings.Display_Height, _settings.Display_Width, _settings.Snake_Block_Size)
            _snake.eat_food()

        clock.tick(_snake.Speed)

    pygame.quit()
    quit()


gameLoop()
