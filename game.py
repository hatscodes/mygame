#programing by hatsfornone(youtube)
#08/21/23
#V0.3
import pygame
#pygame activation and window set up
pygame.init()
screen = pygame.display.set_mode((855, 480))
pygame.display.set_caption("fruit game")
clock = pygame.time.Clock()

run = True
#assets 
player = pygame.Rect((100, 0, 10, 10))
enemy = pygame.Rect((400, 200, 15, 15))
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), enemy)
#detect key presses and react to them
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.move_ip(0, -5)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 5)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(60)

pygame.quit()
