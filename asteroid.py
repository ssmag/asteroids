import pygame
from circleshape import CircleShape
from pygame.draw import circle


class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, radius)

    def draw(self, screen):
        circle(screen, 0xFFFFFF, (self.x, self.y), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
