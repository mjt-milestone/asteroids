import pygame
from circleshape import *
from constants import *

# player class for sprites
class Player(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.rotation = rotation
        rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # draw the player
        pygame.draw.polygon(screen, "white ", self.triangle(), 2)

    def rotate(self, dt):
        # rotate the player
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # rotate left
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            # rotate right
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            # move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # move backward
            self.move(dt)
    
    def move(self, dt): 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            # move forward
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            # move backward
            backward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position -= backward * PLAYER_SPEED * dt