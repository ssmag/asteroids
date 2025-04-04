import pygame
import random
from pygame import Vector2
from circleshape import CircleShape
from pygame.draw import circle
from constants import *


class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        circle(screen, 0xFFFFFF, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if (self.radius == ASTEROID_MIN_RADIUS):
            return
        self.spawn_new_asteroids()

    def spawn_new_asteroids(self):
        random_angle = random.uniform(20, 50)
        t1 = self.velocity.rotate(random_angle)
        t2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x = self.position.x
        y = self.position.y
        a1 = Asteroid(x, y, new_radius)
        a2 = Asteroid(x, y, new_radius)
        a1.velocity = t1
        a2.velocity = t2
        


