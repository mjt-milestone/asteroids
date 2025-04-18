# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # Initialize the game
    pygame.init()
    print("Starting Asteroids")    
    # Set up the game window
    clock = pygame.time.Clock()  # Create a Clock object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop

        screen.fill("black")  # Clear the screen with black
        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds

    pygame.quit()  # Quit pygame when the loop ends

if __name__ == "__main__":
    main()
