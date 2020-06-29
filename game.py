import pygame

pygame.init()  # Initializes all of the imported Pygame modules

# create the display screen for our game
dis = pygame.display.set_mode((400, 300))

# update any changes made to the screeen
pygame.display.update()

# Greet the user with a message
pygame.display.set_caption("Snake Game by Ben Griffin")

### GAME REPL begin ###

# Game Color Variables
blue = (0, 0, 255)
red = (255, 0, 0)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # draw our snake and update the screen
    pygame.draw.rect(dis, blue, [200, 150, 10, 10])
    pygame.display.update*()
### GAME REPL END ###

# un-initializes the game
pygame.quit()

quit()
