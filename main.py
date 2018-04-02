# Imports
import pygame
from pygame.locals import *
from core.Level import Level
from core.Player import Player


# Main
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    # Class initialization
    level = Level(1)
    player = Player(50, 125, 0.4)

    continuer = True
    while continuer:
        display_background(screen)
        level.display_wall(screen)
        player.display_player(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False

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

        player.move(screen, level)

    pygame.quit()


# Functions
def display_background(window):
    background = (200, 200, 200)
    window.fill(background)


main()
