import sys
import pygame
from pygame.locals import *
from constants import *
from models.world import World
from models.floor import Floor
from models.pipe import Pipe
from models.bird import Bird


class Game:
    def __init__(self):
        pygame.init()
        self.width = SIZE[0] * SCALE
        self.height = SIZE[1] * SCALE
        self.bg_color = (255, 255, 255)
        self.window = pygame.display.set_mode((self.width, self.height))
        self.running = True

        # components
        self.world = World()
        self.floor = Floor()
        self.flappy = Bird()

        # add the sprites to the group
        self.world.add(self.floor)
        self.world.add(self.flappy)

    def run(self):
        while self.running:
            self._check_events()
            self._update_window()

        pygame.quit()
        sys.exit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            # Other events, like keys and mouse

    def _update_window(self):
        self.window.fill(self.bg_color)

        self.world.render(self.window)
        self.floor.render(self.window)
        self.flappy.render(self.window)

        self.world.update()

        pygame.display.update()
