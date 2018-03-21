class Wall:
    """
    A class to define a wall or an obstacle and manage collisions
    """

    def __init__(self, x, y, width, height):
        self.pos = (x, y)
        self.height = height
        self.width = width

    @staticmethod
    def wall_collides(wall_list, direction, x, y):
        for wall in wall_list:
            if direction == "UP":
                if y < wall.pos[1] or y > (wall.pos[1]+wall.height):
                    print("COLLISION")
                    return True
                else:
                    print(" PAS COLLISION")
                    return False
