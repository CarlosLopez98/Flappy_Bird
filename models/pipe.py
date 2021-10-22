from random import randint
import pygame.sprite
from settings import Settings

settings = Settings.get_instance()


class Pipe(pygame.sprite.Sprite):
    def __init__(self, init_pos: list, side: str):
        super(Pipe, self).__init__()
        # 'up' - 'down'
        self.side = side
        self.image = settings.sprites_sheet
        self.pos = init_pos
        self.rect = pygame.Rect(self.pos, (26 * settings.scale, 160 * settings.scale))
        self.sprites = {
            'up': [84 * settings.scale, 323 * settings.scale, 26 * settings.scale, 160 * settings.scale],
            'down': [56 * settings.scale, 323 * settings.scale, 26 * settings.scale, 160 * settings.scale]
        }

    def render(self, surface):
        surface.blit(self.image, self.pos, self.sprites[self.side])

    def update(self):
        # self.pos[0] -= settings.scale
        pass

    @classmethod
    def generate_pipes(cls):
        pass
