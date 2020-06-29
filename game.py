import pygame

pygame.init()  # Initializes all of the imported Pygame modules

# create the display screen for our game
dis = pygame.display.set_mode((400, 300))

# update any changes made to the screeen
pygame.display.update()

# Greet the user with a message
pygame.display.set_caption("Snake Game by Ben Griffin")

### GAME REPL begin ###
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
### GAME REPL END ###

# un-initializes the game
pygame.quit()

quit()
