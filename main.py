import pygame
# import constants as Const
from constants import *


def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    pygame.init()
    game_loop()
            
def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while (True):
        on_loop_start()
        screen.fill(0x000000)
        on_loop_end()


def on_loop_start():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def on_loop_end():
    pygame.display.flip()


if __name__ == "__main__":
    main()

