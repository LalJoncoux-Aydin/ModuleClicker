#!/usr/bin/env python3
import pygame, sys, time
import class_display
import player
import student
import display
import production
import select
from pygame.locals import *

def main():
    pygame.init()

    # Init screen
    win = pygame.display.set_mode((1500,750),0,32)
    pygame.display.set_caption('Module Clicker')

    # Init locals
    module = class_display.Module()
    separators = class_display.Separators()

    # Init game
    game_player = player.Player()
    game_students = student.Students()
    game_production = production.Production()
    to_add_module = 0

    while True:
        win.fill(class_display.grey)
        display.displayModule(win, module)
        display.displayStudents(win, game_students)
        display.displaySeparators(win, separators)
        display.displayProduction(win, game_production)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 90 and mx < 320 and my > 200 and my < 500:
                    to_add_module = 20
                    win.blit(module.credit_text, module.credit_textRect)
                else:
                    game_production = select.selectProduction(win, game_production, mx, my, game_player)
                    game_player = select.selectStudents(win, game_students, mx, my, game_player)
        time.sleep(0.1)
        pygame.display.update()

        game_students.redrawStudents(game_player)
        game_production.updateQuantity(game_students)
        game_production.updateProduction()
        game_production.updateUpgrade(game_player, game_students)
        module.updateCredit(game_player.credit)
        game_player = module.updateProgressBar(to_add_module, game_player, game_students, game_production)
        to_add_module = 0
    return

# ----------------------- #
if __name__ == "__main__":
    main()
