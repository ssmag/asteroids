import pygame
import sys
from constants import *
from pygame.time import Clock
from pygame.sprite import Sprite
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    pygame.init()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    game_loop()
            
def game_loop():
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = Clock()
        
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()
    print(f'asteroid containers {Asteroid.containers}')
    print(f'asteroidfield containers {AsteroidField.containers}')
    print(f'asteroidfield {field}')
    print(f'field containers {field.containers}')
    while (True):
        on_loop_start()
        screen.fill(0x000000)
        update(dt)
        draw(screen)
        pygame.display.flip()
        d_time = clock.tick(60)
        dt = d_time/1000

def update(dt):
    for u in updateable:
        u.update(dt)

def draw(screen):
    for d in drawable:
        d.draw(screen)

def on_loop_start():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

if __name__ == "__main__":
    main()

