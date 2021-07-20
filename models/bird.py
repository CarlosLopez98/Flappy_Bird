import pygame
from constants import *


class Bird(pygame.sprite.Sprite):
    def __init__(self, color='yellow'):
        super(Bird, self).__init__()
        self.center = (FLAPPY[0][2] // 2, FLAPPY[0][3] // 2)
        self.pos = [(SIZE[0] * SCALE / 2) - self.center[0], (((SIZE[1] * SCALE) - FLOOR_AREA[3]) / 2) - self.center[1]]
        self.color = color
        self.image = SPRITES_SHEET
        self.sprites = {
            'yellow': [
                (3 * SCALE, 491 * SCALE, 17 * SCALE, 12 * SCALE),
                (31 * SCALE, 491 * SCALE, 17 * SCALE, 12 * SCALE),
                (59 * SCALE, 491 * SCALE, 17 * SCALE, 12 * SCALE),
                (31 * SCALE, 491 * SCALE, 17 * SCALE, 12 * SCALE)
            ],
            'blue': [(), (), (), ()],
            'red': [(), (), (), ()]
        }
        self.actual_sprite = 0

    def render(self, surface):
        # TODO
        surface.blit(self.image, self.pos, self.sprites[self.color][self.actual_sprite])

    def update(self):
        # TODO
        if self.actual_sprite == 2:
            self.actual_sprite = 0
        else:
            self.actual_sprite += 1

    def jump(self):
        # TODO
        pass
