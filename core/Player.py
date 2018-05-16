import pygame

from core.Wall import Wall


class Player:
    """
    Class to create a player and manage it.
    """

    def __init__(self, x, y, speed):
        # PLayer statistics and state attributes
        self.pos = [x, y]
        self.size = [50, 50]
        self.speed = speed
        self.statement_keys = [False, False, False, False]  # Forward, Left, Backward, Right
        self.health = 100

    def display(self, window):
        """
        show the player on the screen
        :param window: pygame Surface object
        """
        square = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        player_color = (243, 0, 0)
        pygame.draw.rect(window, player_color, square)

    def move(self, level):
        """
        move the player in the direction of True's keys in statement_keys list
        :param level: instance of Level Class
        """

        if self.statement_keys[0]:
            c = level.get_constraints(self, Wall.UP)
            if c is not None:
                self.pos[1] = c
            else:
                self.pos[1] -= self.speed

        if self.statement_keys[1]:
            c = level.get_constraints(self, Wall.LEFT)
            if c is not None:
                self.pos[0] = c
            else:
                self.pos[0] -= self.speed

        if self.statement_keys[2]:
            c = level.get_constraints(self, Wall.DOWN)
            if c is not None:
                self.pos[1] = c
            else:
                self.pos[1] += self.speed

        if self.statement_keys[3]:
            c = level.get_constraints(self, Wall.RIGHT)
            if c is not None:
                self.pos[0] = c
            else:
                self.pos[0] += self.speed
