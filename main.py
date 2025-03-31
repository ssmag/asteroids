import pygame
# import constants as Const
from constants import *
from pygame.time import Clock
from player import Player

def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    pygame.init()
    game_loop()
            
def game_loop():
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while (True):
        on_loop_start()
        screen.fill(0x000000)
        player.draw(screen)
        on_loop_end(clock, dt)


def on_loop_start():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def on_loop_end(clock: Clock, dt: int):
    pygame.display.flip()
    d_time = clock.tick(60)
    dt = d_time/1000


if __name__ == "__main__":
    main()

