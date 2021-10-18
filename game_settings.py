import pygame


class Settings:
    Display_Height = 400
    Display_Width = 600
    Snake_Block_Size = 10

    def __init__(self) -> None:
        self.Score_Font = pygame.font.SysFont("comicsansms", 35)
        self.Status_Font = pygame.font.SysFont(None, 50)
