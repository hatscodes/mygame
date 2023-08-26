import pygame

screen_width = 480
screen_height = 520

#colors
white = (255,255,255)
black = (0,0,0)

#player paddle
player_width = 5
player_lenght = 15
player_x = 0
player_y = 0
player_speed = 10

#ball
ball_width = 5
ball_lenght = 5
ball_x = 240
ball_y = 260
ball_speed = 20

#non player paddle
Npaddle_width = 5
Npaddle_leght = 15
Npaddle_x = 400
Npaddle_y = ball_y

run = True
pygame.init()
#screen shit
pygame_icon = pygame.image.load('pong/pixil-frame-0.png')
pygame.display.set_icon(pygame_icon)
screen = pygame.display.set_mode((screen_width,screen_height))
#fps limiter
clock = pygame.time.Clock()
#the while loop
while run:
    screen.fill(black)
    
    #player_paddle = pygame.draw.rect(screen,white,pygame.Rect(player_width, player_lenght))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    clock.tick(24)
pygame.quit()