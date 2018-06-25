import random

import pygame

from constants import *
from core.Entity import Entity


class Enemy(Entity):
    def __init__(self, level):
        super().__init__(-1, -1, 0.75, 3, (64, 64))

        self.direction = random.randint(0, 3)
        self.set_spawn(level)

        self.dir = "./assets/img/player_"
        self.img = pygame.image.load(self.dir + "right.png")

    def set_spawn(self, level):
        """
        Setting random spawn positions for enemies
        :return:
        """
        c = level.get_constraints(self, self.direction)
        while c is not None:
            self.pos[0] = random.randint(0, 1016)
            self.pos[1] = random.randint(0, 656)
            c = level.get_constraints(self, self.direction)

    def move(self, level):
        c = level.get_constraints(self, self.direction)
        if self.direction == UP:
            if c is not None:
                self.pos[1] = c
                self.direction = DOWN
                c = None
            else:
                self.pos[1] -= self.speed
        if self.direction == LEFT:
            if c is not None:
                self.pos[0] = c
                self.direction = RIGHT
                c = None
            else:
                self.pos[0] -= self.speed
        if self.direction == DOWN:
            if c is not None:
                self.pos[1] = c
                self.direction = UP
                c = None
            else:
                self.pos[1] += self.speed
        if self.direction == RIGHT:
            if c is not None:
                self.pos[0] = c
                self.direction = LEFT
            else:
                self.pos[0] += self.speed

    def display(self, window):

        if self.direction == UP:
            self.img = pygame.image.load(self.dir + "up.png")
            window.blit(self.img, self.pos)

        if self.direction == LEFT:
            self.img = pygame.image.load(self.dir + "left.png")
            window.blit(self.img, self.pos)

        if self.direction == DOWN:
            self.img = pygame.image.load(self.dir + "down.png")
            window.blit(self.img, self.pos)

        if self.direction == RIGHT:
            self.img = pygame.image.load(self.dir + "right.png")
            window.blit(self.img, self.pos)
