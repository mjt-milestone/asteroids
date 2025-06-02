import pygame
import random
from circleshape import *
from constants import *

# Asteroid class for sprites
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Automatically add the asteroid to the containers if they exist
        super().__init__(x, y, radius)
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        # Update the asteroid's position
        self.position += self.velocity * dt
    
    def split(self):
        # always kill original asteroid
        self.kill()

        # if the asteroid is small just kill it.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # calculate new radius for split asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # generate a randome angle for the new asteroid vectors
        random_angle = random.uniform(20, 50)

        # create two new velocity vectors rotate by the random angle
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2

        # spawn two new asteroids at the same location, with new radius and velocities
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vel2