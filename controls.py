from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


def handle_control(keystroke, block_size: int):
    x1_change = 0
    y1_change = 0

    if keystroke == K_LEFT:
        x1_change = -block_size
        y1_change = 0
    elif keystroke == K_RIGHT:
        x1_change = block_size
        y1_change = 0
    elif keystroke == K_UP:
        x1_change = 0
        y1_change = -block_size
    elif keystroke == K_DOWN:
        x1_change = 0
        y1_change = block_size

    return x1_change, y1_change