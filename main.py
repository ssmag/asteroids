import pygame
import sys
from constants import *
from pygame.time import Clock
from pygame.sprite import Sprite
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    pygame.init()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    game_loop()
            
def game_loop():
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = Clock()
        
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()
    while (True):
        on_loop_start()
        screen.fill(0x000000)
        update(dt)
        check_for_collisions(player)
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

def check_for_collisions(player):
    check_player_death(player)
    check_asteroid_shot()

def check_asteroid_shot():
    for a in asteroids:
        for b in shots:
            d = a.distance_to(b)
            if (d <= 0):
                a.kill()
                b.kill()

def check_player_death(player):
    for a in asteroids:
        d = a.distance_to(player)
        if (d <= 0):
            print("Game over!")
            sys.exit()

def on_loop_start():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

if __name__ == "__main__":
    main()

