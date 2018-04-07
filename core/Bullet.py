class Bullet:
    """
    Class to manage bullet physics
    """

    def __init__(self, player):
        x = player.pos[0] + player.size[0]
        y = player.pos[1] + (player.size[1] / 2)
        self.pos = [x, y]
        self.bspeed = 0.2

    def update(self):
        self.pos[0] += self.bspeed
