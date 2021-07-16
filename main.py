import pygame
from pygame.locals import *
import time
from constants import *
from models.bird import Bird

WIDTH = SIZE[0] * SCALE
HEIGHT = SIZE[1] * SCALE

frame_rate = 60

image_width = 512
image_height = 512
sprites = pygame.image.load('res/sprites_sheet.png')
sprites = pygame.transform.scale(sprites, (image_width * SCALE, image_height * SCALE))

# instance of the bird
flappy = Bird(None, sprites)


def game():
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    clock = pygame.time.Clock()

    # Frame rate independence
    last_time = time.time()

    # clock
    frame = 0
    running = True
    while running:
        delta_time = time.time() - last_time
        delta_time *= 60
        print(delta_time)
        last_time = time.time()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        window.fill((0, 0, 0), (0, 0, WIDTH, HEIGHT))
        # rendering the background
        window.blit(sprites, (0, 0), BACKGROUND_AREA)
        window.blit(sprites, (BACKGROUND_AREA[2], 0), BACKGROUND_AREA)
        render_floor(window)

        # render the bird
        flappy.render(window)
        if frame % 5 == 0:
            flappy.update()

        clock.tick(frame_rate)
        frame += 1

        if frame >= 100:
            frame = 0

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

    floor_pos[0] -= SCALE
    floor_pos2[0] -= SCALE


if __name__ == '__main__':
    game()
