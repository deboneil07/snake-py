from curses import window
import pygame
import time
import random

snake_speed = 15

#window size

window_x = 720
window_y = 480

#defining colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

#initializing the game
pygame.init()

#initializing the game window
pygame.display.set_caption("Cobra Tate")
game_window = pygame.display.set_mode((window_x, window_y))

# Frame rate
fps = pygame.time.Clock()


#defining snake's default pos
snake_position = [100,50]

#defining first four blocks of snake
#body
snake_body = [
    [100,50],
    [90,50],
    [80,50],
    [70,50]
]

#fruit pos
fruit_position = [random.randrange(1, window_x//10) * 10,
                  random.randrange(1, window_y//10) * 10]
fruit_spawn = True

#setting default snake dir
#toward right

direction = "RIGHT"
change_to = direction

#initial score
score = 0

#displaying score function
def show_score(choice, color, font, size):
    
    #creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    #create display surface object
    #score surface
    score_surface = score_font.render(f'Score: {str(score)}', True, color)

    # create a rect object for text surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)

#game over function
def game_over():
    
    #creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    #creating a surface on which text will be displayed
    game_over_surface = my_font.render(f"Your Score: {str(score)}", True, red)

    #create a rect object for text surface object
    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x/2, window_y/4)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    

    time.sleep(2)

    pygame.quit()
    quit()


