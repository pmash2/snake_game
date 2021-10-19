import random
import pygame
from colors import Colors as MyColors
from typing import List


class Food:
    Coordinate: List[int]

    def __init__(self, height, width, block_size) -> None:
        self.set_coordinate(height, width, block_size)

    def set_coordinate(self, height: int, width: int, block_size: int):
        coord = []
        rand_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        rand_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
        coord.append(rand_x)
        coord.append(rand_y)
        self.Coordinate = coord

    def draw(self, _surface: pygame.Surface, block_size: int):
        pygame.draw.rect(_surface, MyColors.Green, [self.Coordinate[0], self.Coordinate[1], block_size, block_size])
