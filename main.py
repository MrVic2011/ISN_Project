# Imports
import pygame
from pygame.locals import *

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

    # Class initialization
    level = Level(1)
    player = Player(50, 125, 0.4)
    interface = Menu()

    game = False
    menu = True
    while menu:
        interface.spawn_btn()
        interface.display_btn(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                menu = False
            if event.type == KEYDOWN and event.key == K_F1:
                menu = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if interface.btn_clicked(event):
                    game = True
                    menu = False

    while game:
        level.display_background(screen)
        level.display_wall(screen)
        level.display_bullets(screen)
        player.display_player(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
            if event.type == KEYDOWN and event.key == K_F1:
                game = False

            # PLayer movement event check
            if event.type == KEYDOWN:
                if event.key == K_w:
                    player.statement_keys[0] = True
                if event.key == K_a:
                    player.statement_keys[1] = True
                if event.key == K_s:
                    player.statement_keys[2] = True
                if event.key == K_d:
                    player.statement_keys[3] = True

            if event.type == KEYUP:
                if event.key == K_w:
                    player.statement_keys[0] = False
                if event.key == K_a:
                    player.statement_keys[1] = False
                if event.key == K_s:
                    player.statement_keys[2] = False
                if event.key == K_d:
                    player.statement_keys[3] = False

            if event.type == KEYDOWN and event.key == K_SPACE:
                tmp = Bullet(player)
                level.bullets.append(tmp)

        player.move(screen, level)
        level.update_sprites()

    pygame.quit()


main()
