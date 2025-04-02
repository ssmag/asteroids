import pygame
from circleshape import CircleShape
from pygame.draw import circle


class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        circle(screen, 0xFFFFFF, (x, y), radius)

    def update(self, dt):
        self.position += self.velocity * dt
