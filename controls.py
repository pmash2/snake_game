from pygame import event
import pygame


def handle_control(keystroke, block_size: int):
    x1_change = 0
    y1_change = 0

    if keystroke == pygame.K_LEFT:
        x1_change = -block_size
        y1_change = 0
    elif keystroke == pygame.K_RIGHT:
        x1_change = block_size
        y1_change = 0
    elif keystroke == pygame.K_UP:
        x1_change = 0
        y1_change = -block_size
    elif keystroke == pygame.K_DOWN:
        x1_change = 0
        y1_change = block_size

    return x1_change, y1_change