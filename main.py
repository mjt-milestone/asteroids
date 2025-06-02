# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group() 
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Asteroid.containers = updatable, drawable, asteroids
Shot.containers = updatable, drawable, shots

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, 0) 
updatable.add(player)
drawable.add(player)

AsteroidField.containers = updatable

asteroidfield = AsteroidField()
updatable.add(asteroidfield)

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
        for obj in updatable:
            # Update all sprites in the updatable group
            obj.update(dt)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                # Handle collision (e.g., end game.)
                running = False  # Exit the game loop
        
        # Check for collisions between shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    # Handle collision (e.g., destroy asteroid and shot)
                    asteroid.split()
                    shot.kill() 

        # Handle game logic and rendering here
        # Fill the screen with black
        screen.fill("black")  # Clear the screen with black
        for obj in drawable:
            # Draw all sprites in the drawable group
            obj.draw(screen)
        pygame.display.flip()  # Update the display

    pygame.quit()  # Quit pygame when the loop ends

if __name__ == "__main__":
    main()
