import pygame

from core.Collision import Collision


class Level:
    """
    Class to generate the selected level from a file and manage all actions that happend in the level
    """

    def __init__(self, level_id):
        self.wall_list = []
        self.id = level_id
        print("Le level d'ID:{0} Ã  Ã©tÃ© gÃ©nÃ©rer".format(self.id))
        self.generate_wall()

    def generate_wall(self):
        wall = Collision(150, 100, 20, 100)
        self.wall_list.append(wall)

        wall = Collision(170, 180, 80, 20)
        self.wall_list.append(wall)

    def collides(self, obj_pos):
        for wall in self.wall_list:
            wall.had_collision(obj_pos)

    def display_wall(self, window):
        for wall in self.wall_list:
            square = pygame.Rect(wall.pos[0], wall.pos[1], wall.width, wall.height)
            color = (0, 0, 0)
            pygame.draw.rect(window, color, square)
