class Wall:
    """
    A class to define a wall or an obstacle and manage collisions
    """
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

    def __init__(self, x, y, width, height):
        self.pos = (x, y)
        self.height = height
        self.width = width

    """
    def check_collides(self, player):
        "\""
        Method to check if the player try to move in a wall
        :param player: an instance of PLayer CLass
        :return: True if the player new postion is in a wall. False if not
        "\""
        px, py = player.pos
        pw, ph = player.size
        wx, wy = self.pos
        ww = self.width
        wh = self.height

        if py > wy + wh:  # upside
            return False
        if py + ph < wy:  # downside
            return False
        if px > wx + ww:  # right side
            return False
        if px + pw < wx:  # left side
            return False

        return True
    """

    def get_constraints(self, player, direction):
        """

        """
        px, py = player.pos
        pw, ph = player.size
        wx, wy = self.pos
        ww = self.width
        wh = self.height

        if direction == Wall.DOWN:
            if px + pw <= wx or px >= wx + ww:  # no collision
                return None
            if py + ph >= wy > py:
                return wy - ph

        if direction == Wall.RIGHT:
            if py + ph <= wy or py >= wy + wh:  # no collision
                return None
            if px + pw >= wx > px:
                return wx - pw

        if direction == Wall.UP:
            if px + pw <= wx or px >= wx + ww:  # no collision
                return None
            if py <= wy + wh < py + ph:
                return wy + wh

        if direction == Wall.LEFT:
            if py + ph <= wy or py >= wy + wh:  # no collision
                return None
            if px <= wx + ww < px + pw:
                return wx + ww

        return None
