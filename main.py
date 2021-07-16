import pygame
from pygame.locals import *
from constants import *

WIDTH = SIZE[0] * SCALE
HEIGHT = SIZE[1] * SCALE

image_width = 512
image_height = 512
sprites = pygame.image.load('res/sprites_sheet.png')
sprites = pygame.transform.scale(sprites, (image_width * SCALE, image_height * SCALE))


def game():
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    clock = pygame.time.Clock()
    clock.tick(60)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        window.fill((0, 0, 0), (0, 0, WIDTH, HEIGHT))
        # rendering the background
        window.blit(sprites, (0, 0), BACKGROUND_AREA)
        window.blit(sprites, (BACKGROUND_AREA[2], 0), BACKGROUND_AREA)
        render_floor(window)

        pygame.display.update()


# we define a initial positions for render the floor images
floor_pos = [0, HEIGHT - FLOOR_AREA[3]]
floor_pos2 = [288, HEIGHT - FLOOR_AREA[3]]


def render_floor(surface):
    surface.blit(sprites, floor_pos, FLOOR_AREA)
    surface.blit(sprites, floor_pos2, FLOOR_AREA)

    if floor_pos[0] < -288:
        floor_pos[0] = floor_pos2[0] + 288

    if floor_pos2[0] < -288:
        floor_pos2[0] = floor_pos[0] + 288

    floor_pos[0] -= 1
    floor_pos2[0] -= 1


if __name__ == '__main__':
    game()
