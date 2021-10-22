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
        self.pipes = [Pipe([300, -200], 'down'), Pipe([300, 400], 'up')]

        self.actual_height = self.height - self.floor.rect[3]  # actual gaming zone, without the floor
        settings.hit_box_size = (40, self.actual_height / 4)
        settings.pipes_range.append(self.actual_height / 6)
        settings.pipes_range.append((self.actual_height / 6 * 5) - settings.hit_box_size[1])

        # add the sprites to the group
        self.world.add(self.floor)
        self.world.add(self.flappy)
        for pipe in self.pipes:
            self.world.add(pipe)

        # score
        self.score = 0

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
                if event.key == K_SPACE:
                    # Flappy jumps
                    self.flappy.jump()
            if event.type == MOUSEBUTTONDOWN:
                self.flappy.jump()

        self.flappy.check_collision(self.floor)

    def _update_window(self):
        self.window.fill(self.bg_color)

        self.world.render(self.window)
        for pipe in self.pipes:
            pipe.render(self.window)
        self.floor.render(self.window)
        self.flappy.render(self.window)

        # references
        pygame.draw.line(self.window, (0, 0, 0), (0, self.actual_height / 6), (self.width, self.actual_height / 6), 1)
        pygame.draw.line(self.window, (0, 0, 0), (0, self.actual_height / 6 * 5), (self.width, self.actual_height / 6 * 5), 1)

        self.world.update()

        pygame.display.update()
