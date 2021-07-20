import pygame.sprite
from constants import SPRITES_SHEET, HEIGHT, SCALE


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.image = SPRITES_SHEET
        self.sprite = (292 * SCALE, 0, 168 * SCALE, 56 * SCALE)
        self.pos = [0, HEIGHT - self.sprite[3]]
        self.pos2 = [288, HEIGHT - self.sprite[3]]

    def render(self, surface):
        surface.blit(self.image, self.pos, self.sprite)
        surface.blit(self.image, self.pos2, self.sprite)

        # TODO separate the update functionality
        if self.pos[0] < -288:
            self.pos[0] = self.pos2[0] + 288

        if self.pos2[0] < -288:
            self.pos2[0] = self.pos[0] + 288

        self.pos[0] -= SCALE
        self.pos2[0] -= SCALE

    def update(self):
        # TODO
        pass
