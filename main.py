# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    # Initialize the game
    pygame.init()
    print("Starting Asteroids")    
    # Set up the game window
    clock = pygame.time.Clock()  # Create a Clock object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    # Create the player object in the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop

        # Handle game logic and rendering here
        # Fill the screen with black
        screen.fill("black")  # Clear the screen with black
        player.draw(screen)
        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds

    pygame.quit()  # Quit pygame when the loop ends

if __name__ == "__main__":
    main()
