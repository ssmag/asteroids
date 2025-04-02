import pygame
from pygame import Vector2
from circleshape import CircleShape
from pygame.draw import polygon
from constants import *

class Player(CircleShape):
    rotation = 0
    containers = None
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
            

    def triangle(self):
        direction = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + direction * self.radius
        b = self.position - direction * self.radius - right
        c = self.position - direction * self.radius + right
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

        if keys[pygame.K_w]:
            print("hit w")
            self.move(dt)
        
        if keys[pygame.K_s]:
            print("hit s")
            self.move(-dt)
        

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        direction = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt
