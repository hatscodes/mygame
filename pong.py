import pygame

screen_width = 480
screen_height = 520

#colors
white = (255,255,255)
black = (0,0,0)

#player paddle
player_width = 30
player_lenght = 90
player_x = 0
player_y = 240
player_speed = 4

#ball
ball_width = 10
ball_lenght = 10
ball_x = 240
ball_y = 260
ball_x_M = 2.3
ball_y_M = 2.3

#non player paddle
Npaddle_width = 30
Npaddle_leght = 90
Npaddle_x = 450
#misc1
positive = 1

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
    #misc2
    ballx = ball_x
    bally = ball_y
    Npaddle_y = ball_y 
    
    #loading image
    screen.fill(black)
    player_rectangle = pygame.Rect(player_x,player_y,player_width,player_lenght)
    pygame.draw.rect(screen,white,player_rectangle)
    
    Npaddle = pygame.Rect(Npaddle_x,Npaddle_y,Npaddle_width,Npaddle_leght)
    pygame.draw.rect(screen,white,Npaddle)

    ball = pygame.Rect(ball_x,ball_y,ball_width,ball_lenght)
    pygame.draw.rect(screen,white,ball)
    #ball movement
    ball_x -= ball_x_M
    ball_y += ball_y_M
    
    #collisons
    if positive == 1:
        if player_rectangle.colliderect(ball):
            ball_x_M = -2.1
            ball_y_M = -2.1
            positive = 0
    if positive == 0:
        if Npaddle.colliderect(ball):
            ball_x_M = 2.5
            ball_y_M = 2.0
            positive = 1
    #controls
    key = pygame.key.get_pressed()

    if key[pygame.K_s] == True:
        player_y += player_speed
    elif key[pygame.K_w] == True:
        player_y -= player_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    clock.tick(60)
#debug*
print(player_y)
pygame.quit()
