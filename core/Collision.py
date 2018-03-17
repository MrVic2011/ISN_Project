class Collision:
    """
    A class to define a wall or an obstacle and manage collisions
    """
    def __init__(self, x, y, width, height):
        self.pos = (x, y)
        self.height = height
        self.width = width

    def had_collision(self, obj_pos):
        if self.pos[0] < obj_pos[0] < (self.pos[0]+self.width):
            if self.pos[1] < obj_pos[1] < (self.pos[1]+self.height):
                print("COLLISION")
