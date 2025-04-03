import pygame
from circleshape import CircleShape
from pygame.draw import circle
from constants import *


class Shot(CircleShape):
    containers = None
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        circle(screen, 0xFFFFFF, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
