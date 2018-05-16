import pygame

from constants import *


class Menu:
    """
    A Class to manage the main menu of the game where
    you can choose the volume of the music, and the level
    you want to play.
    """

    def __init__(self):
        self.btn_list = []
        self.font = pygame.font.Font("./assets/font/doublefeature.ttf", 30)

        self.spawn_btn()

    def spawn_btn(self):
        """
        Method of listing all menu's buttons
        """

        # Center the button in the middle of the screen
        tmp_p1 = (SCREEN_WIDTH - 200) / 2
        tmp_p2 = (SCREEN_HEIGHT / 2) + 50

        # Initialize the button
        tmp_msg = "JOUER"
        tmp = Button(1, tmp_p1, tmp_p2, 50, 200, tmp_msg)
        self.btn_list.append(tmp)

        # Buttons for choosing level
        # Plus Button
        tmp_p1 = (SCREEN_WIDTH - 50) / 2
        tmp_p1 += 75
        tmp_p2 = (SCREEN_HEIGHT - 100) / 2

        tmp_msg = "+"
        tmp = Button(2, tmp_p1, tmp_p2, 50, 50, tmp_msg)
        self.btn_list.append(tmp)

        # Minus Button
        tmp_p1 = (SCREEN_WIDTH - 50) / 2
        tmp_p1 -= 75
        tmp_p2 = (SCREEN_HEIGHT - 100) / 2

        tmp_msg = "-"
        tmp = Button(3, tmp_p1, tmp_p2, 50, 50, tmp_msg)
        self.btn_list.append(tmp)

    def display_btn(self, window, back_color):
        """
        Method for displaying all buttons of btn_list attribute
        :param window: Pygame Surface object
        """
        for btn in self.btn_list:
            # Drawing the display_background of the button
            square = pygame.Rect(btn.pos[0], btn.pos[1], btn.width, btn.height)
            color = back_color
            pygame.draw.rect(window, color, square)

            # Center the text of the button
            txt_size = self.font.size(btn.txt)
            pos_1 = (btn.width - txt_size[0]) / 2
            pos_2 = (btn.height - txt_size[1]) / 2

            pos_1 = btn.pos[0] + pos_1
            pos_2 = btn.pos[1] + pos_2
            txt_pos = (pos_1, pos_2)

            # Print the button's text on screen
            text = self.font.render(btn.txt, 1, (0, 0, 0))
            window.blit(text, (txt_pos[0], txt_pos[1]))

    def btn_clicked(self, mouse):
        """
        Check all button of the menu to see if they get clicked
        :param mouse: pygame Mouse's events
        :return:
        """
        for btn in self.btn_list:
            if btn.clicked(mouse):
                return btn.id

        return None

    def display_lvl(self, window, lvl_id):
        """

        :param lvl_id: level_id of Level object
        :param window: pygame Surface object
        :return:
        """
        pos_1 = (SCREEN_WIDTH - 100) / 2
        pos_2 = (SCREEN_HEIGHT - 100) / 2

        lvl_id = str(lvl_id)

        level = Button(2, pos_1, pos_2, 50, 100, lvl_id)

        square = pygame.Rect(level.pos[0], level.pos[1], level.width, level.height)
        color = (0, 0, 0)
        pygame.draw.rect(window, color, square)

        # Center the text of the button
        txt_size = self.font.size(level.txt)
        pos_1 = (level.width - txt_size[0]) / 2
        pos_2 = (level.height - txt_size[1]) / 2

        pos_1 = level.pos[0] + pos_1
        pos_2 = level.pos[1] + pos_2
        txt_pos = (pos_1, pos_2)

        # Print the button's text on screen
        text = self.font.render(level.txt, 1, (178, 34, 34))
        window.blit(text, (txt_pos[0], txt_pos[1]))

    @staticmethod
    def display_background(window):
        """
        Display the display_background of the Menu
        :return:
        """
        window.fill((0, 0, 0))

    def update(self, window, lvl_number):
        """
        Method to update all elements on the menu
        :param lvl_number:
        :type window:
        :return:
        """
        self.display_background(window)
        self.display_btn(window, (34, 139, 34))
        self.display_lvl(window, lvl_number)


class Button:
    def __init__(self, btn_id, x, y, height, width, txt=""):
        self.state = False
        self.id = btn_id
        self.pos = (x, y)
        self.height = height
        self.width = width
        self.txt = txt

    def clicked(self, mouse):
        if mouse.pos[0] >= self.pos[0] + self.width:
            return False
        if mouse.pos[0] <= self.pos[0]:
            return False
        if mouse.pos[1] >= self.pos[1] + self.height:
            return False
        if mouse.pos[1] <= self.pos[1]:
            return False
        return True
