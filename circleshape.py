import pygame
from pygame.sprite import Sprite

class CircleShape(Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def distance_to(self, other):
        return (self.position - other.position).magnitude() - (self.radius + other.radius)


