import pygame
import random
from pygame.locals import *


class Enemy(pygame.sprite.Sprite):
    """

    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect(center=(random.randint(100, 500), random.randint(100, 500)))


pygame.init()
continuer = 1

fenetre = pygame.display.set_mode((800, 600))
ennemyevent = pygame.USEREVENT + 1
pygame.time.set_timer(ennemyevent, 500)
group = pygame.sprite.Group()
while continuer:
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == ennemyevent:
            print("OK", ennemyevent)
            nouveau = Enemy()
            group.add(nouveau)

    group.draw(fenetre)
