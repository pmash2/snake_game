import pygame
import time

# https://www.edureka.co/blog/snake-game-with-pygame/

pygame.init()

color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_blue = (0, 0, 255)
snake_block = 10

display_height = 800
display_width = 600

dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake game by pmash')

game_over = False

x1 = display_width / 2
y1 = display_height / 2
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

print(f"K_LEFT: {pygame.K_LEFT}")
print(f"K_RIGHT: {pygame.K_RIGHT}")
print(f"K_UP: {pygame.K_UP}")
print(f"K_DOWN: {pygame.K_DOWN}")

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    _message = font_style.render(msg, True, color)
    dis.blit(_message, [display_width / 2, display_height / 2])


while not game_over:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("LEFT")
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                print("UP")
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                print("DOWN")
                x1_change = 0
                y1_change = 10

    if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(color_white)
    pygame.draw.rect(dis, color_blue, [x1, y1, snake_block, snake_block])

    pygame.display.update()
    clock.tick(snake_speed)

message("You lost", color_red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
