import pygame
from settings import Settings

settings = Settings.get_instance()


class Bird(pygame.sprite.Sprite):
    def __init__(self, color='yellow'):
        super(Bird, self).__init__()
        # TODO modify all this operations with the new setting file
        self.center = (17 * settings.scale // 2, 12 * settings.scale // 2)
        self.pos = [
            (settings.width // 2) - self.center[0],
            ((settings.height - 56 * settings.scale) // 2) - self.center[1]
        ]
        self.rect = pygame.Rect(self.pos, (17 * settings.scale, 12 * settings.scale))
        self.rect.center = self.center
        self.color = color
        self.image = settings.sprites_sheet
        self.sprites = {
            'yellow': [
                (3 * settings.scale, 491 * settings.scale, 17 * settings.scale, 12 * settings.scale),
                (31 * settings.scale, 491 * settings.scale, 17 * settings.scale, 12 * settings.scale),
                (59 * settings.scale, 491 * settings.scale, 17 * settings.scale, 12 * settings.scale),
                (31 * settings.scale, 491 * settings.scale, 17 * settings.scale, 12 * settings.scale)
            ],
            'blue': [(), (), (), ()],
            'red': [(), (), (), ()]
        }
        self.actual_sprite = 0

        self.speed = [0, 0]
        self.acc = [0, 1]

    def render(self, surface):
        # TODO
        surface.blit(self.image, self.pos, self.sprites[self.color][self.actual_sprite])

    def update(self):
        # TODO
        # animation
        if settings.frame % 5 == 0:
            if self.actual_sprite == 2:
                self.actual_sprite = 0
            else:
                self.actual_sprite += 1

        # gravity
        self.pos = [self.pos[0] + self.speed[0], self.pos[1] + self.speed[1]]
        # acceleration
        self.speed = [self.speed[0] + self.acc[0], self.speed[1] + self.acc[1]]

        print('speed:', self.speed)

    def jump(self):
        # TODO
        self.speed[1] = -10
