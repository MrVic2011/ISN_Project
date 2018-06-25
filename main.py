# Imports
import pygame

from constants import *
from core.Bullet import Bullet
from core.Level import Level
from core.Menu import Menu
from core.Player import Player


# Main
from core.Sound import Sound


def main():
    """
    Main process of the game.
    Execute all classes and manage event returned by pygame.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    sound = Sound()
    sound.generate_sound()

    # Menu
    menu = Menu()

    game = False
    config = True
    lvl_nbr = 1
    keys = KEYS_1
    skeys = KEYS_2

    while config:
        menu.update(screen, lvl_nbr)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                config = False
            if event.type == KEYDOWN and event.key == K_F1:
                config = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                # Play Button
                btn_return = menu.btn_clicked(event)
                if btn_return == 1:
                    game = True
                    config = False
                if btn_return == 2 and 1 <= lvl_nbr < LEVEL_NUMBER:
                    lvl_nbr += 1
                if btn_return == 3 and 1 < lvl_nbr <= LEVEL_NUMBER:
                    lvl_nbr -= 1

    # Level Initialization
    level = Level(lvl_nbr)
    player = Player(50, 100, 4)

    # Game
    while game:
        level.update_sprites(screen, player)

        for e in level.enemies:
            e.move(level)
            e.display(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    message_on_screen(screen)
                    game = False

            # PLayer movement event check
            if event.type == KEYDOWN:
                if event.key == keys[0]:
                    player.statement_keys[0] = True
                if event.key == keys[1]:
                    player.statement_keys[1] = True
                if event.key == keys[2]:
                    player.statement_keys[2] = True
                if event.key == keys[3]:
                    player.statement_keys[3] = True

            if event.type == KEYUP:
                if event.key == keys[0]:
                    player.statement_keys[0] = False
                if event.key == keys[1]:
                    player.statement_keys[1] = False
                if event.key == keys[2]:
                    player.statement_keys[2] = False
                if event.key == keys[3]:
                    player.statement_keys[3] = False

            if event.type == KEYDOWN:
                if event.key == skeys[0]:
                    tmp = Bullet(player, 2, UP)
                    level.bullets.append(tmp)
                if event.key == skeys[1]:
                    tmp = Bullet(player, 2, LEFT)
                    level.bullets.append(tmp)
                if event.key == skeys[2]:
                    tmp = Bullet(player, 2, DOWN)
                    level.bullets.append(tmp)
                if event.key == skeys[3]:
                    tmp = Bullet(player, 2, RIGHT)
                    level.bullets.append(tmp)

        if player.statement_keys != [False] * 4:
            player.move(level)

    pygame.quit()


def message_on_screen(window):
    """
    Function to display a message on full screen.
    Used wehn the player loose.
    :param window: pygame Surface object
    :return:
    """
    gameover = 1
    while gameover:
        window.fill((0, 0, 0))
        font = pygame.font.Font("./assets/font/pixel.ttf", 100)

        text = "Game Over !"
        text_size = font.size(text)
        x = (SCREEN_WIDTH - text_size[0]) / 2
        y = (SCREEN_HEIGHT - text_size[1]) / 2

        msg = font.render(text, 1, (255, 255, 255))
        window.blit(msg, (x, y))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    gameover = False


main()
