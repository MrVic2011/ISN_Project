import pygame


class Menu:
    """

    """

    def __init__(self):
        """

        """
        self.btn_list = []

    def spawn_btn(self):
        tmp = Button(150, 150, 25, 150)
        self.btn_list.append(tmp)

    def display_btn(self, window):
        for btn in self.btn_list:
            square = pygame.Rect(btn.pos[0], btn.pos[1], btn.width, btn.height)
            color = (255, 140, 0)
            pygame.draw.rect(window, color, square)

    def btn_clicked(self, mouse):
        for btn in self.btn_list:
            if btn.clicked(mouse):
                return True

        return False


class Button:
    def __init__(self, x, y, height, width):
        self.state = False
        self.pos = (x, y)
        self.height = height
        self.width = width

    def clicked(self, mouse):
        if mouse.pos[0] >= self.pos[0]+self.width:
            return False
        if mouse.pos[0] <= self.pos[0]:
            return False
        if mouse.pos[1] >= self.pos[1]+self.height:
            return False
        if mouse.pos[1] <= self.pos[1]:
            return False
        return True
