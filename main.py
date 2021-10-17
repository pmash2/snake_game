import pygame

# https://www.edureka.co/blog/snake-game-with-pygame/

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()

pygame.display.set_caption('Snake game by pmash')

color_blue = (0, 0, 255)
color_red = (255, 0, 0)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        print(event)

        pygame.draw.rect(dis, color_blue, [200, 150, 10, 10])
        pygame.display.update()

pygame.quit()
quit()
