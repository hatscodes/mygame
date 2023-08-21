#programing by hatsfornone(youtube)
#08/21/23
#V0.2
import pygame

pygame.init()
screen = pygame.display.set_mode((855, 480))
run = True

player = pygame.Rect((0, 0, 50, 50))

while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)
#detect key presses and react to them
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()


pygame.quit()