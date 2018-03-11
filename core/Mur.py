class Wall:
    """
    A class to define a wall or an obstacle and manage collisions
    """

    def __init__(self, x, y, height, width):
        self.pos = (x, y)
        self.height = height
        self.width = width

    # def had_collision(self, x, y):
