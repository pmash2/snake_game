import pygame

# https://www.edureka.co/blog/snake-game-with-pygame/

pygame.init()

color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_blue = (0, 0, 255)

dis = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Snake game by pmash')
# pygame.display.update()

game_over = False

x1 = 300
y1 = 300
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

print(f"K_LEFT: {pygame.K_LEFT}")
print(f"K_RIGHT: {pygame.K_RIGHT}")
print(f"K_UP: {pygame.K_UP}")
print(f"K_DOWN: {pygame.K_DOWN}")

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

    x1 += x1_change
    y1 += y1_change
    dis.fill(color_white)
    pygame.draw.rect(dis, color_blue, [x1, y1, 10, 10])

    pygame.display.update()
    clock.tick(30)


pygame.quit()
quit()
