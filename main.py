# Imports
import pygame

from constants import *
from core.Bullet import Bullet
from core.Level import Level
from core.Menu import Menu
from core.Player import Player


# Main
def main():
    """
    Main process of the game.
    Execute all classes and manage event returned by pygame
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Menu
    menu = Menu()

    game = False
    config = True
    lvl_nbr = 1
    keys = KEYS_1

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
    player = Player(50, 125, 1.5)

    # Game
    while game:
        level.update_sprites(screen, player)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
            if event.type == KEYDOWN and event.key == K_F1:
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

            if event.type == KEYDOWN and event.key == K_SPACE:
                tmp = Bullet(player)
                level.bullets.append(tmp)

        if player.statement_keys != [False] * 4:
            player.move(level)

    pygame.quit()


main()
