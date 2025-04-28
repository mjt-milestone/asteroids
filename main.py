# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group() 

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, 0) 
updatable.add(player)
drawable.add(player)

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

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds

        # Update the player
        for sprite in updatable:
            # Update all sprites in the updatable group
            sprite.update(dt)


        # Handle game logic and rendering here
        # Fill the screen with black
        screen.fill("black")  # Clear the screen with black
        for sprite in drawable:
            # Draw all sprites in the drawable group
            sprite.draw(screen)
        pygame.display.flip()  # Update the display

    pygame.quit()  # Quit pygame when the loop ends

if __name__ == "__main__":
    main()
