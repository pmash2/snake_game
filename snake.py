from typing import List
import pygame
from colors import Colors as MyColors
from game_settings import Settings


class Snake:
    Nodes: List[int]
    Length: int
    Speed: int

    def __init__(self) -> None:
        self.Nodes = []
        self.Length = 1
        self.Speed = 15

    def add_node(self, x: int, y: int):
        node = self.make_node(x, y)
        self.Nodes.append(node)

        if len(self.Nodes) > self.Length:
            del self.Nodes[0]

    def collided_with_self(self, x: int, y: int):
        currentNode = self.make_node(x, y)

        # Everything but the last item in the list
        for x in self.Nodes[:-1]:
            if x == currentNode:
                print("COLLIDE")
                return True
        return False

    def eat_food(self):
        self.Length += 1


    def draw(self, _surface: pygame.Surface, _settings: Settings):
        snake_block = _settings.Snake_Block_Size
        for coord in self.Nodes:
            pygame.draw.rect(_surface, MyColors.Blue, [int(coord[0]), int(coord[1]), snake_block, snake_block])

    def make_node(self, x: int, y: int):
        node = []
        node.append(x)
        node.append(y)
        return node
