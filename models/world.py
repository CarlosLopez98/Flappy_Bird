import pygame.sprite
from settings import Settings

settings = Settings.get_instance()


class World(pygame.sprite.Group):
    # Class that will contain all the other elements
    # like the floor, pipes and the bird
    def __init__(self):
        super(World, self).__init__()
        self.backgrounds = {
            'light': (0, 0, 144 * settings.scale, 256 * settings.scale),
            'dark': (146 * settings.scale, 0, 144 * settings.scale, 256 * settings.scale)
        }
        self.actual_background = 'light'

    def render(self, surface):
        # Rendering the background
        surface.blit(settings.sprites_sheet, (0, 0), self.backgrounds[self.actual_background])
        surface.blit(settings.sprites_sheet,
                     (self.backgrounds[self.actual_background][2], 0), self.backgrounds[self.actual_background])

        # Rendering the other elements
        # TODO
        # self.draw(surface)  # Could be this

    def change_background(self):
        if self.actual_background == 'light':
            self.actual_background = 'dark'
        else:
            self.actual_background = 'light'
