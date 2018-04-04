import bcolors


class Wall:
    """
    A class to define a wall or an obstacle and manage collisions
    """

    def __init__(self, x, y, width, height):
        self.pos = (x, y)
        self.height = height
        self.width = width

    def check_collides(self, player, direction):
        """
        Method to check if the player try to move in a wall
        :param player: an instance of PLayer CLass
        :param direction: player moving direction
        :return: True if the player new postion is in a wall. False if not
        """
        px, py = player.pos
        pw, ph = player.size
        wx, wy = self.pos
        ww = self.width
        wh = self.height

        if direction == "UP":
            if py >= wy + wh:  # upside
                return False
            if py + ph <= wy:  # downside
                return False
            if px >= wx + ww:  # right side
                return False
            if px + pw <= wx:  # left side
                return False
            return True

        if direction == "DOWN":
            if py >= wy + wh:  # upside
                return False
            if py + ph <= wy:  # downside
                return False
            if px >= wx + ww:  # right side
                return False
            if px + pw <= wx:  # left side
                return False
            return True

        if direction == "LEFT":
            if py >= wy + wh:  # upside
                return False
            if py + ph <= wy:  # downside
                return False
            if px >= wx + ww:  # right side
                return False
            if px + pw <= wx:  # left side
                return False
            return True

        if direction == "RIGHT":
            if py >= wy + wh:  # upside
                return False
            if py + ph <= wy:  # downside
                return False
            if px >= wx + ww:  # right side
                return False
            if px + pw <= wx:  # left side
                return False
            return True

        print(bcolors.WARN + "No direction in player move. Please report this to the developpers" + bcolors.ERRMSG)
        return False
