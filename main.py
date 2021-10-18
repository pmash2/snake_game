import pygame
from colors import Colors as MyColors
from game_settings import Settings
import utilities
import snake

# https://www.edureka.co/blog/snake-game-with-pygame/

pygame.init()

_settings = Settings()
clock = pygame.time.Clock()
_snake = snake.Snake()

_surface = pygame.display.set_mode((_settings.Display_Width, _settings.Display_Height))
pygame.display.set_caption('Snake game by pmash')


def gameLoop():
    game_over = False
    game_close = False

    x1 = int(_settings.Display_Width / 2)
    y1 = int(_settings.Display_Height / 2)
    x1_change = 0
    y1_change = 0

    food_coord = utilities.get_food_coord(_settings)

    while not game_over:

        while game_close == True:
            _surface.fill(MyColors.Light_Blue)
            utilities.display_message("You Lost! Press Q-Quit or C-Play Again", MyColors.Red, _surface, _settings)
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
                if event.key == pygame.K_LEFT:
                    x1_change = -_settings.Snake_Block_Size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = _settings.Snake_Block_Size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -_settings.Snake_Block_Size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = _settings.Snake_Block_Size

        if utilities.player_out_of_bounds(x1, y1, _settings):
            game_close = True

        x1 += x1_change
        y1 += y1_change
        _surface.fill(MyColors.Light_Blue)
        pygame.draw.rect(_surface, MyColors.Green, [food_coord[0], food_coord[1], _settings.Snake_Block_Size, _settings.Snake_Block_Size])

        _snake.add_node(x1, y1)

        if _snake.collided_with_self(x1, y1):
            game_close = True

        _snake.draw(_surface, _settings)
        utilities.display_score(_snake.Length - 1, _settings.Score_Font, _surface)

        pygame.display.update()

        if x1 == food_coord[0] and y1 == food_coord[1]:
            food_coord = utilities.get_food_coord(_settings)
            _snake.Length += 1

        clock.tick(_snake.Speed)

    pygame.quit()
    quit()


gameLoop()
