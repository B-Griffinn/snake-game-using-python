import pygame
import time
import random

pygame.init()  # Initializes all of the imported Pygame modules

# Game Color Variables
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

# create the display screen for our game
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
# Greet the user with a message
pygame.display.set_caption("Snake Game by Ben Griffin")

# Add Clock var to our game
clock = pygame.time.Clock()

# snake block
snake_block = 10
# snake speed
snake_speed = 25

# Font Style
font_style = pygame.font.SysFont(None, 30)

### GAME REPL begin ###


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    # game REPL
    while not game_over:

        # logic for cloisng our game if the user loses
        while game_close == True:
            dis.fill(white)
            message("You lost! Press Q to Quit or C to Play Again.", red)
            pygame.display.update()

            # check if the user wants to quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # loop through all the commands coming in from our screen
        for event in pygame.event.get():
            # handle a using 'Xing' out of the screen
            if event.type == pygame.QUIT:
                game_over = True

            # MOVE SNAKE
            # handle key strokes to move snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

            # end our game if the snake touches our screen walls
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True

        # udpate our snake coordinates to now be where we moved it to
        x1 += x1_change
        y1 += y1_change

        # fill our game screen
        dis.fill(white)
        # draw our food
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        # draw our snake
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        # udpate the screen
        pygame.display.update()

        # if the snake eats the food print something
        if x1 == foodx and y1 == foody:
            print("TTTTThanksssss.")

        # adjust clock
        clock.tick(snake_speed)

    # un-initializes the game
    pygame.quit()
    quit()


# Call The Game
game_loop()
