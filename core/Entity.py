class Entity:
    """
    Class to manage all types of entities in the game
    """

    def __init__(self, x, y, speed, health, size=(64, 64)):
        self.pos = [x, y]
        self.size = size
        self.speed = speed
        self.health = health
