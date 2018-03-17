import os
import pygame


class Player:
    """
    Class to create a player and manage it.
    """

    def __init__(self, x, y, speed):
        root = os.path.dirname(__file__)
        rel_path = os.path.join("..", "assets", "player_right.png")
        abs_path = os.path.join(root, rel_path)
        # PLayer img
        self.right_img = pygame.image.load_basic(abs_path).convert_alpha()
        self.left_img = pygame.image.load_basic("../assets/player_left.png").convert_alpha()
        self.up_img = pygame.image.load_basic("../assets/player_up.png").convert_alpha()
        self.down_img = pygame.image.load_basic("../assets/player_down.png").convert_alpha()
        self.direction = self.down_img

        # PLayer statistics and state attributes
        self.position = [x, y]
        self.speed = speed
        self.statement_keys = [False, False, False, False]  # Forward, Left, Backward, Right
        self.health = 100

    def display_player(self, window):
        """
        show the player on the screen
        :param window: pygame Surface object
        """
        window.blit(self.direction, (self.position[0], self.position[1]))
        # square = pygame.Rect(self.position[1], self.position[0], 50, 50)
        # player_color = (243, 0, 0)
        # pygame.draw.rect(window, player_color, square)

    def move(self, window):
        """
        move the player in the direction of True's keys in statement_keys attribut
        """
        if self.statement_keys[0]:
            self.position[0] -= self.speed
            self.display_player(window)
        if self.statement_keys[1]:
            self.position[1] -= self.speed
            self.display_player(window)
        if self.statement_keys[2]:
            self.position[0] += self.speed
            self.display_player(window)
        if self.statement_keys[3]:
            self.position[1] += self.speed
            self.display_player(window)
