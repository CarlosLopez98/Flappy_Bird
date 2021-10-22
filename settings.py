from pygame.image import load
from pygame.transform import scale


class Settings:
    _instance = None

    def __init__(self):
        self.scale = 3
        self.size = (168, 256)
        self.width = self.size[0] * self.scale
        self.height = self.size[1] * self.scale

        self.sprites_sheet = load('res/sprites_sheet.png')
        self.image_width = self.sprites_sheet.get_width()
        self.image_height = self.sprites_sheet.get_height()
        self.sprites_sheet = scale(self.sprites_sheet, (self.image_width * self.scale, self.image_height * self.scale))

        # range to create the pipes
        self.hit_box_size = 0
        self.pipes_range = []

        # Frame independence
        self.frame_rate = 60
        self.delta_time = 0
        self.frame = 0

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Settings()

        return cls._instance
