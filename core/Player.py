import pygame

from constants import *
from core.Entity import Entity


class Player(Entity):
    """
    Class to create a player and manage it.
    """

    def __init__(self, x, y, speed):
        # PLayer statistics and state attributes
        size = (64, 64)
        super().__init__(x, y, speed, 3, size)
        self.statement_keys = [False, False, False, False]  # Forward, Left, Backward, Right
        self.dir = "./assets/img/player_"
        self.img = pygame.image.load(self.dir + "right.png")

    def display(self, window):
        """
        Display the player on the screen
        :param window: pygame Surface object
        """
        if self.statement_keys[0]:
            self.img = pygame.image.load(self.dir + "up.png")
            window.blit(self.img, self.pos)

        if self.statement_keys[1]:
            self.img = pygame.image.load(self.dir + "left.png")
            window.blit(self.img, self.pos)

        if self.statement_keys[2]:
            self.img = pygame.image.load(self.dir + "down.png")
            window.blit(self.img, self.pos)

        if self.statement_keys[3]:
            self.img = pygame.image.load(self.dir + "right.png")
            window.blit(self.img, self.pos)

        if self.statement_keys == [False]*4:
            self.img = pygame.image.load(self.dir + "right.png")
            window.blit(self.img, self.pos)

    def move(self, level):
        """
        move the player in the direction of True's keys in statement_keys list
        :param level: instance of Level Class
        """

        if self.statement_keys[0]:
            c = level.get_constraints(self, UP)
            if c is not None:
                self.pos[1] = c
            else:
                self.pos[1] -= self.speed

        if self.statement_keys[1]:
            c = level.get_constraints(self, LEFT)
            if c is not None:
                self.pos[0] = c
            else:
                self.pos[0] -= self.speed

        if self.statement_keys[2]:
            c = level.get_constraints(self, DOWN)
            if c is not None:
                self.pos[1] = c
            else:
                self.pos[1] += self.speed

        if self.statement_keys[3]:
            c = level.get_constraints(self, RIGHT)
            if c is not None:
                self.pos[0] = c
            else:
                self.pos[0] += self.speed
