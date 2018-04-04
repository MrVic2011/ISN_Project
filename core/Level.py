import pygame

from core.Wall import Wall


class Level:
    """
    Class to generate the selected level from a file and manage all actions that happend in the level
    """

    def __init__(self, level_id):
        self.wall_list = []
        self.id = level_id
        print("Le level d'ID:{0} generer".format(self.id))
        self.generate_wall()

    def generate_wall(self):
        """
        Method to initialize each wall of the level using the class Wall
        """
        wall = Wall(150, 100, 20, 100)
        self.wall_list.append(wall)

        wall = Wall(50, 180, 80, 20)
        self.wall_list.append(wall)

        wall = Wall(20, 100, 20, 100)
        self.wall_list.append(wall)

    def display_wall(self, window):
        for wall in self.wall_list:
            square = pygame.Rect(wall.pos[0], wall.pos[1], wall.width, wall.height)
            color = (0, 0, 0)
            pygame.draw.rect(window, color, square)

    def collides(self, player, direction):
        for wall in self.wall_list:
            collides = wall.check_collides(player, direction)
            if collides:
                player.pos[0] = round(player.pos[0])
                player.pos[1] = round(player.pos[1])
                return True
        return False
