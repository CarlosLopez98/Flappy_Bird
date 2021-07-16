import pygame
from pygame.locals import *
from positions import *


WIDTH = 144 * 2
HEIGHT = 257 * 2

image_width = 512
image_height = 512
sprites = pygame.image.load('res/sprites.png')
sprites = pygame.transform.scale(sprites, (image_width * 2, image_height * 2))


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

        window.blit(sprites, (0, 0), BACKGROUND)

        pygame.display.update()


if __name__ == '__main__':
    game()
