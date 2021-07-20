from pygame.image import load
from pygame.transform import scale


# position rectangles constants for the sprites images
SCALE = 3
SIZE = (168, 256)
WIDTH = SIZE[0] * SCALE
HEIGHT = SIZE[1] * SCALE

IMAGE_WIDTH = 512
IMAGE_HEIGHT = 512
SPRITES_SHEET = load('res/sprites_sheet.png')
SPRITES_SHEET = scale(SPRITES_SHEET, (IMAGE_WIDTH * SCALE, IMAGE_HEIGHT * SCALE))

# Floor
FLOOR_AREA = (292 * SCALE, 0, 168 * SCALE, 56 * SCALE)

# Pipes
GREEN_PIPE_UP = ()
GREEN_PIPE_DOWN = (57, 323)
RED_PIPE_UP = ()
RED_PIPE_DOWN = ()

# Flappy
FLAPPY = [
    (3 * SCALE, 491 * SCALE, 17 * SCALE, 12 * SCALE),
    (31 * SCALE, 491 * SCALE, 17 * SCALE, 12 * SCALE),
    (59 * SCALE, 491 * SCALE, 17 * SCALE, 12 * SCALE)
]
BLUE_FLAPPY = [(), (), ()]
RED_FLAPPY = [(), (), ()]
