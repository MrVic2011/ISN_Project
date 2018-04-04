import bcolors
import pygame


class Player:
    """
    Class to create a player and manage it.
    """

    def __init__(self, x, y, speed):

        # PLayer img
        # PLayer statistics and state attributes
        self.pos = [x, y]
        self.size = [50, 50]
        self.speed = speed
        self.statement_keys = [False, False, False, False]  # Forward, Left, Backward, Right
        self.health = 100

    def display_player(self, window):
        """
        show the player on the screen
        :param window: pygame Surface object
        """
        # window.blit(self.direction, (self.position[0], self.position[1]))
        square = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        player_color = (243, 0, 0)
        pygame.draw.rect(window, player_color, square)

    def move(self, window, level):
        """
        move the player in the direction of True's keys in statement_keys attribut
        :param level: instance of Level Class
        :param window: pygame Surface object
        """

        if self.statement_keys[0]:
            collide = level.collides(self, "UP")
            if collide:
                print(bcolors.OKMSG + "collide UP")
            if not collide:
                self.pos[1] -= self.speed
            self.display_player(window)

        if self.statement_keys[1]:
            collide = level.collides(self, "LEFT")
            if collide:
                print(bcolors.OKMSG + "collide LEFT")
            if not collide:
                self.pos[0] -= self.speed
            self.display_player(window)

        if self.statement_keys[2]:
            collide = level.collides(self, "DOWN")
            if collide:
                print(bcolors.OKMSG + "collide DOWN")
            if not collide:
                self.pos[1] += self.speed
            self.display_player(window)

        if self.statement_keys[3]:
            collide = level.collides(self, "RIGHT")
            if collide:
                print(bcolors.OKMSG + "collide RIGHT")
            if not collide:
                self.pos[0] += self.speed
            self.display_player(window)
