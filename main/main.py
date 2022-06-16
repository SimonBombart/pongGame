import pygame, sys

# General settings
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 800  #1280
screen_height = 600 #960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)   

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7

while True:
    #Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    ball.x += ball_speed_x
    ball.y += ball_speed_y  
          
    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    
    #Updating the screen        
    pygame.display.flip()
    clock.tick(60)
