import pygame
from circleshape import *
from constants import *

# Shot class for bullet sprites
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        # Automatically add the shot to the containers if they exist
        super().__init__(x, y, radius)
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        # Draw the shot as a circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        # Update the shot's position
        self.position += self.velocity * dt