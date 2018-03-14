# Imports
import pygame
from pygame.locals import *
from core.Level import Level


# Main
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    # Class initialization
    level = Level(screen, 1)

    statement_keys = [False, False, False, False]
    player_pos = [50, 50]
    player_speed = 0.4

    continuer = True
    while continuer:
        display_background(screen)
        level.display_wall(screen)
        spawn_player(screen, player_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False

            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    statement_keys[0] = True
                elif event.key == K_a:
                    statement_keys[1] = True
                elif event.key == K_s:
                    statement_keys[2] = True
                elif event.key == K_d:
                    statement_keys[3] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    statement_keys[0] = False
                elif event.key == pygame.K_a:
                    statement_keys[1] = False
                elif event.key == pygame.K_s:
                    statement_keys[2] = False
                elif event.key == pygame.K_d:
                    statement_keys[3] = False

        if statement_keys[0]:
            player_pos[1] -= player_speed
            level.level_collision(player_pos)
        elif statement_keys[2]:
            player_pos[1] += player_speed
            level.level_collision(player_pos)
        if statement_keys[1]:
            player_pos[0] -= player_speed
            level.level_collision(player_pos)
        elif statement_keys[3]:
            player_pos[0] += player_speed
            level.level_collision(player_pos)

    pygame.quit()


# Functions
def display_background(window):
    background = (200, 200, 200)
    window.fill(background)


def spawn_player(screen, pos):
    square = pygame.Rect(pos[0], pos[1], 50, 50)
    player_color = (243, 0, 0)
    pygame.draw.rect(screen, player_color, square)


main()
