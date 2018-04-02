class Wall:
    """
    A class to define a wall or an obstacle and manage collisions
    """
    def __init__(self, x, y, width, height):
        self.pos = (x, y)
        self.height = height
        self.width = width

    @staticmethod
    def check_collides(wall_list, player):
        for wall in wall_list:
            if player.direction == "RIGHT":
                if wall.pos[0] < player.position[0] + player.size[0] < wall.pos[0] + wall.width:
                    if wall.pos[1] < player.position[1] + player.size[1] < wall.pos[1] + wall.height:
                        return True
            if player.direction == "LEFT":
                if wall.pos[0] < player.position[0] < wall.pos[0] + wall.width:
                    if wall.pos[1] < player.position[1] + player.size[1] < wall.pos[1] + wall.height:
                        return True
            if player.direction == "UP":
                if wall.pos[1] < player.position[1] < wall.pos[1] + wall.height:
                    if wall.pos[0] < player.position[0] < wall.pos[0] + wall.width:
                        return True
            if player.direction == "DOWN":
                if wall.pos[1] < player.position[1] + player.size[1] < wall.pos[1] + wall.height:
                    if wall.pos[0] < player.position[0] < wall.pos[0] + wall.width:
                        return True

        return False
