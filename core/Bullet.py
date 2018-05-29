from constants import *
from core.Entity import Entity


class Bullet(Entity):
    """
    Class to manage bullet physics
    """

    def __init__(self, player, speed, direction):
        self.direction = direction
        self.color = (0, 255, 0)
        self.alpha = 255
        size = (20, 20)

        x, y = self.set_spawn_pos(player, size)

        super().__init__(x, y, speed, 1, size)

    def set_spawn_pos(self, player, size):
        """

        :return:
        """
        if self.direction == UP:
            x = player.pos[0] + (player.size[0] / 2)
            x -= (size[0] / 2)

            y = player.pos[1]

            return x, y

        if self.direction == LEFT:
            x = player.pos[0]

            y = player.pos[1] + (player.size[1] / 2)
            y -= (size[1] / 2)

            return x, y

        if self.direction == DOWN:
            x = player.pos[0] + (player.size[0] / 2)
            x -= (size[0] / 2)

            y = player.pos[1] + player.size[1]

            return x, y

        if self.direction == RIGHT:
            x = player.pos[0]

            y = player.pos[1] + (player.size[1] / 2)
            y -= (size[1] / 2)

            return x, y

        else:
            return None

    def move(self, level):
        """
        Method to manage all bullets path
        :param level:
        :return:
        """

        c = level.get_constraints(self, self.direction)
        if c is None and self.direction == UP:
            self.pos[1] -= self.speed

        if c is None and self.direction == LEFT:
            self.pos[0] -= self.speed

        if c is None and self.direction == DOWN:
            self.pos[1] += self.speed

        if c is None and self.direction == RIGHT:
            self.pos[0] += self.speed

        if c is not None:
            self.alpha = 0
