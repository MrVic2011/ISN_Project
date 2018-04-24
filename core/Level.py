import pygame

from core.Wall import Wall


class Level:

    """
    Class to generate the selected level from a file and manage all actions that happend in the level
    """
    def __init__(self, level_id):
        self.wall_list = []
        self.bullets = []
        self.id = str(level_id)
        self.file = open("./levels/lvl_" + self.id + ".txt")
        print("Level {0} created".format(self.id))
        self.generate_level()

    @staticmethod
    def display_background(window):
        """
        Method to display a background on the game screen
        :param window: pygame Surface object
        """
        background = (200, 200, 200)
        window.fill(background)

    def generate_level(self):
        """
        Method to read level's file and create walls using position which are in a text file
        :return:
        """
        file_line = self.file.readline()
        while len(file_line) > 0:
            self.generate_wall(file_line)
            file_line = self.file.readline()

        self.file.close()

    def generate_wall(self, string):
        """
        Method to initialize each wall of the level using the class Wall
        """
        index1 = string.find(' ')
        index2 = string.find(' ', index1 + 1)
        index3 = string.find(' ', index2 + 1)

        wx = string[0:index1]
        wx = int(wx)

        wy = string[index1 + 1:index2]
        wy = int(wy)

        ww = string[index2 + 1:index3]
        ww = int(ww)

        wh = string[index3 + 1:len(string)]
        wh = int(wh)

        wall = Wall(wx, wy, ww, wh)
        self.wall_list.append(wall)

    def display_wall(self, window):
        """
        Method to draw a black square at the postion of each wall in the wall list of the Level instance
        :param window: pygame Surface object
        """
        for wall in self.wall_list:
            square = pygame.Rect(wall.pos[0], wall.pos[1], wall.width, wall.height)
            color = (0, 0, 0)
            pygame.draw.rect(window, color, square)

    def collides(self, player, direction):
        """
        Method to check with each wall of the level if the player try to pass through a wall
        :param player: instance of PLayer CLass
        :param direction: "UP", "DOWN", "LEFT" or "RIGHT" - Player moving direction
        :return:
        """
        for wall in self.wall_list:
            collides = wall.check_collides(player, direction)
            if collides:
                player.pos[0] = round(player.pos[0])
                player.pos[1] = round(player.pos[1])
                return True
        return False

    def display_bullets(self, window):
        """
        Method to draw bullets shooted by player on the screen
        :param window: pygame Surface object
        :return:
        """
        for bullet in self.bullets:
            square = pygame.Rect(bullet.pos[0], bullet.pos[1], 20, 4)
            color = (0, 255, 0)
            pygame.draw.rect(window, color, square)

    def update_sprites(self):
        """
        Method to upadate sprties on the screen with their new positions
        :return:
        """
        for bullet in self.bullets:
            bullet.update()
