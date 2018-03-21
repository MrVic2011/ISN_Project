import pygame

from core.Collision import Collision


class Level:
    """
    Class to generate the selected level from a file and manage all actions that happend in the level
    """

    def __init__(self, level_id):
        self.wall_list = []
        self.id = level_id
        print("Le level d'ID:{0} ÃƒÂ  ÃƒÂ©tÃƒÂ© gÃƒÂ©nÃƒÂ©rer".format(self.id))
        self.generate_wall()

    def generate_wall(self):
        wall = Collision(150, 100, 20, 100)
        self.wall_list.append(wall)

        wall = Collision(50, 180, 80, 20)
        self.wall_list.append(wall)

        wall = Collision(20, 100, 20, 100)
        self.wall_list.append(wall)

    def collides(self, player):
        for wall in self.wall_list:
            if player.direction == "RIGHT":
                if wall.pos[0] <= player.position[0]+player.size[0] <= wall.pos[0]+wall.width:
                    if wall.pos[1] <= player.position[1]+player.size[1] <= wall.pos[1]+wall.height:
                        player.position[0] = wall.pos[0]-player.size[0]
                        return True
            if player.direction == "LEFT":
                if wall.pos[0] <= player.position[0] <= wall.pos[0]+wall.width:
                    if wall.pos[1] <= player.position[1]+player.size[1] <= wall.pos[1]+wall.height:
                        player.position[0] = wall.pos[0]+wall.width
                        return True
            if player.direction == "UP":
                if wall.pos[1] <= player.position[1] <= wall.pos[1]+wall.height:
                    if wall.pos[0] <= player.position[0] <= wall.pos[0]+wall.width:
                        return True
            if player.direction == "DOWN":
                if wall.pos[1] <= player.position[1] <= wall.pos[1]+wall.height:
                    if wall.pos[0] <= player.position[0] <= wall.pos[0]+wall.width:
                        return True

        return False


    def display_wall(self, window):
        for wall in self.wall_list:
            square = pygame.Rect(wall.pos[0], wall.pos[1], wall.width, wall.height)
            color = (0, 0, 0)
            pygame.draw.rect(window, color, square)
