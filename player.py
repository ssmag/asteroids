import pygame
from pygame import Vector2
from circleshape import CircleShape
from pygame.draw import polygon
from constants import *

class Player(CircleShape):
    rotation = 0
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
            

    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        polygon(screen, 0xFFFFFF, self.triangle(), 2)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            print("hit a")
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
            print("hit d")
            self.rotate(dt)

    def rotate(self, dt):
        print(f'rotation before rotate: {self.rotation}')
        self.rotation += PLAYER_TURN_SPEED * dt
        print(f'rotation on rotate: {self.rotation}')
