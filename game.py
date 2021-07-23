import sys
import time
import pygame
from pygame.locals import *
from settings import Settings
from models.world import World
from models.floor import Floor
from models.pipe import Pipe
from models.bird import Bird

settings = Settings.get_instance()


class Game:
    def __init__(self):
        pygame.init()
        self.width = settings.width
        self.height = settings.height
        self.bg_color = (255, 255, 255)
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        # components
        self.world = World()
        self.floor = Floor()
        self.flappy = Bird()
        self.pipes = [Pipe(), ]

        # add the sprites to the group
        self.world.add(self.floor)
        self.world.add(self.flappy)

    def run(self):
        last_time = time.time()

        while self.running:
            settings.delta_time = time.time() - last_time
            settings.delta_time *= settings.frame_rate
            last_time = time.time()

            self.clock.tick(settings.frame_rate)
            settings.frame += 1

            if settings.frame >= 100:
                settings.frame = 0

            self._check_events()
            self._update_window()

        pygame.quit()
        sys.exit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            # Other events, like keys and mouse
            if event.type == KEYDOWN:
                if event.key == K_c:
                    # Change the background
                    self.world.change_background()
                if event.key == K_UP:
                    # Flappy jumps
                    self.flappy.jump()

    def _update_window(self):
        self.window.fill(self.bg_color)

        self.world.render(self.window)
        self.floor.render(self.window)
        self.flappy.render(self.window)

        self.world.update()
        # self.floor.update()
        # self.flappy.update()

        pygame.display.update()
