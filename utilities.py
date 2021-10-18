from typing import Set
from colors import Colors as MyColors
import random
import pygame
from game_settings import Settings


def display_score(score: int, _font: pygame.font.SysFont, _surface: pygame.Surface):
    value = _font.render(f"Your Score: {score}", True, MyColors.Yellow)

    _surface.blit(value, [0, 0])


def display_message(msg: str, color: MyColors, _surface: pygame.Surface, _settings: Settings):
    _message = _settings.Status_Font.render(msg, True, color)

    _surface.blit(_message, [_settings.Display_Width / 2, _settings.Display_Height / 2])


def get_food_coord(_settings: Settings):
    coord = []
    coord.append(round(random.randrange(0, _settings.Display_Width - _settings.Snake_Block_Size) / 10.0) * 10.0)
    coord.append(round(random.randrange(0, _settings.Display_Height - _settings.Snake_Block_Size) / 10.0) * 10.0)
    return coord

def player_out_of_bounds(x: int, y: int, _settings: Settings):
    if x >= _settings.Display_Width or x < 0 or y >= _settings.Display_Height or y < 0:
        return True
    return False
