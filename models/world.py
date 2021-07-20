import pygame.sprite
from constants import SCALE, SPRITES_SHEET


class World(pygame.sprite.Group):
    # Class that will contain all the other elements
    # like the floor, pipes and the bird
    def __init__(self):
        super(World, self).__init__()
        self.backgrounds = {
            'light': (0, 0, 144 * SCALE, 256 * SCALE),
            'dark': (146 * SCALE, 0, 144 * SCALE, 256 * SCALE)
        }
        self.actual_background = 'light'

    def render(self, surface):
        # Rendering the background
        surface.blit(SPRITES_SHEET, (0, 0), self.backgrounds[self.actual_background])
        surface.blit(SPRITES_SHEET,
                     (self.backgrounds[self.actual_background][2], 0), self.backgrounds[self.actual_background])

        # Rendering the other elements
        # TODO
        # self.draw(surface)  # Could be this

    def change_background(self):
        if self.actual_background == 'light':
            self.actual_background = 'dark'
        else:
            self.actual_background = 'light'
