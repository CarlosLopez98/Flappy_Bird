import pygame
from constants import *


class Bird(pygame.sprite.Sprite):
    def __init__(self, color, image):
        super(Bird, self).__init__()
        self.pos = []
        self.center = (FLAPPY[0][2] // 2, FLAPPY[0][3] // 2)
        self.color = color
        self.image = image
        self.sprites = [FLAPPY[0], FLAPPY[1], FLAPPY[2], FLAPPY[1]]
        self.actual_sprite = 0

    def render(self, surface):
        # TODO
        surface.blit(self.image, (0, 0), self.sprites[self.actual_sprite])

    def update(self):
        # TODO
        if self.actual_sprite == 2:
            self.actual_sprite = 0
        else:
            self.actual_sprite += 1
