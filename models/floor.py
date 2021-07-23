import pygame.sprite
from settings import Settings

settings = Settings.get_instance()


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.image = settings.sprites_sheet
        self.sprite = (292 * settings.scale, 0, 168 * settings.scale, 56 * settings.scale)
        self.pos = [0, settings.height - self.sprite[3]]
        self.pos2 = [288, settings.height - self.sprite[3]]

    def render(self, surface):
        surface.blit(self.image, self.pos, self.sprite)
        surface.blit(self.image, self.pos2, self.sprite)

    def update(self):
        if self.pos[0] < -288:
            self.pos[0] = self.pos2[0] + 288

        if self.pos2[0] < -288:
            self.pos2[0] = self.pos[0] + 288

        self.pos[0] -= settings.scale
        self.pos2[0] -= settings.scale
