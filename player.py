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
        pass
#
# import pygame
# 
# class CircleShape(pygame.sprite.Sprite):
#     def __init__(self, x, y, radius):
#         if hasattr(self, "containers"):
#             super().__init__(self.containers)
#         else:
#             super().__init__()
#         
#         self.position = pygame.Vector2(x, y)
#         self.velocity = pygame.Vector2(0,0)
#         self.radius = radius
# 
# 
#     def update(self, dt):
#         pass
#
