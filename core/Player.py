import pygame


class Player:
    """
    Class to create a player and manage it.
    """

    def __init__(self, x, y, speed):

        # PLayer img
        # PLayer statistics and state attributes
        self.position = [x, y]
        self.size = [50,50]
        self.speed = speed
        self.direction = "DOWN"
        self.statement_keys = [False, False, False, False]  # Forward, Left, Backward, Right
        self.health = 100

    def display_player(self, window):
        """
        show the player on the screen
        :param window: pygame Surface object
        """
        # window.blit(self.direction, (self.position[0], self.position[1]))
        square = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        player_color = (243, 0, 0)
        pygame.draw.rect(window, player_color, square)

    def move(self, window, level):
        """
        move the player in the direction of True's keys in statement_keys attribut
        :param level:
        :param window:
        """

        if self.statement_keys[0]:
            self.direction = "UP"
            collide = level.collides(self)
            if collide:
                print("OK")
            if not collide:
                self.position[1] -= self.speed
            self.display_player(window)

        if self.statement_keys[1]:
            self.direction = "LEFT"
            collide = level.collides(self)
            if collide:
                print("OK")
            if not collide:
                self.position[0] -= self.speed
            self.display_player(window)

        if self.statement_keys[2]:
            self.direction = "DOWN"
            collide = level.collides(self)
            if collide:
                print("OK")
            if not collide:
                self.position[1] += self.speed
            self.display_player(window)

        if self.statement_keys[3]:
            self.direction = "RIGHT"
            collide = level.collides(self)
            if collide:
                print("OK")
            if not collide:
                self.position[0] += self.speed
            self.display_player(window)
