class Collision:
    """
    A class to define a wall or an obstacle and manage collisions
    """
    def __init__(self, x, y, width, height):
        self.pos = (x, y)
        self.height = height
        self.width = width
