import random

import pygame

from constants import *
from core.Entity import Entity


class Enemy(Entity):
    def __init__(self, level):
        super().__init__(-1, -1, 0.75, (64, 64))

        self.direction = random.randint(0, 3)
        print("OK")
        self.set_spawn(level)

    def set_spawn(self, level):
        """

        :return:
        """
        print(self.pos)
        c = level.get_constraints(self, self.direction)
        while c is not None:
            self.pos[0] = random.randint(0, 1016)
            self.pos[1] = random.randint(0, 656)
            print(self.pos)
            c = level.get_constraints(self, self.direction)

    def move(self, level):
        c = level.get_constraints(self, self.direction)
        if self.direction == UP:
            pass
        if self.direction == LEFT:
            pass
        if self.direction == DOWN:
            pass
        if self.direction == RIGHT:
            pass

    def display(self, window):
        square = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        e_color = (25, 25, 110)
        pygame.draw.rect(window, e_color, square)
