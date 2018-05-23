from constants import *


class Wall:
    """
    A class to define a wall or an obstacle and manage collisions
    """

    def __init__(self, x, y, width, height):
        self.pos = (x, y)
        self.height = height
        self.width = width

    def get_constraint(self, entity, direction):
        """
        Method to check if the player is touching a wall or not
        """
        px, py = entity.pos
        pw, ph = entity.size
        wx, wy = self.pos
        ww = self.width
        wh = self.height

        if direction == DOWN:
            if px + pw <= wx or px >= wx + ww:  # no collision
                return None
            if py + ph >= wy > py:
                return wy - ph

        if direction == RIGHT:
            if py + ph <= wy or py >= wy + wh:  # no collision
                return None
            if px + pw >= wx > px:
                return wx - pw

        if direction == UP:
            if px + pw <= wx or px >= wx + ww:  # no collision
                return None
            if py <= wy + wh < py + ph:
                return wy + wh

        if direction == LEFT:
            if py + ph <= wy or py >= wy + wh:  # no collision
                return None
            if px <= wx + ww < px + pw:
                return wx + ww

        return None
