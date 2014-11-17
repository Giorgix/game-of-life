import pygame
import sys
from pygame import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
background = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.convert()
background.fill((255, 255, 255))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Surface((20, 20))
        self.image.convert()
        self.image.fill((0, 0, 0))
        self.rect = Rect(10, 10, 20, 20)


def main():
    pygame.init()
    player = Player()
    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        screen.blit(player.image, (player.rect.left, player.rect.top))
        screen.blit(player.image, (31, 10))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()
