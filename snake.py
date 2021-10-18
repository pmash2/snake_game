from typing import List
import pygame
from colors import Colors as MyColors


class Snake:
    Nodes: List[str]
    Length: int
    Speed: int

    def __init__(self) -> None:
        self.Nodes = []
        self.Length = 1
        self.Speed = 15

    def add_node(self, x, y):
        node = self.make_node(x, y)
        self.Nodes.append(node)

    # BUG: This is not working right...
    def collided_with_self(self, x, y):
        currentNode = self.make_node(x, y)

        # Everything but the last item in the list
        for x in self.Nodes[:-1]:
            if x == currentNode:
                print("COLLIDE")
                return True
            return False

    def draw(self, _surface, _settings):
        snake_block = _settings.Snake_Block_Size
        for coord in self.Nodes:
            pygame.draw.rect(_surface, MyColors.Blue, [int(coord[0]), int(coord[1]), snake_block, snake_block])

    def make_node(x, y):
        node = []
        node.append(x)
        node.append(y)
        return node
