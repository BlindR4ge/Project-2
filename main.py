import os, sys

import pygame
from pygame.locals import *

from point import Point
from config import *
from location import *

class Game():

    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((width_x*20, height_y*20+40))
        pygame.display.set_caption('Сапер')
    def event(self, event):
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                sys.exit()
                

def main():
    game = Game()

    start_location = StartLocation(game)

    game.location = start_location

    clock = pygame.time.Clock()
    while 1:
        clock.tick(fps)
        game.location.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            game.location.event(event)
            game.event(event)            
            
    
if __name__ == "__main__":
    main()
