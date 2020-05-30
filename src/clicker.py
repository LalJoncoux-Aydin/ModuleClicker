#!/usr/bin/env python3
import pygame, sys, time
import class_display
import player
import student
import display
import production
from pygame.locals import *

def selectStudents(win, game_students, mx, my, game_player):
    if mx > 1000 and my < 120 and game_player.credit >= game_students.price1:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu1_pos)
        win.blit(game_students.stu1_selected, game_students.stu1_rect)
        game_students.AddStudents1()
        game_player.credit -=  game_students.price1
    if mx > 1000 and my > 120 and my < 250 and game_player.credit >= game_students.price2:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu2_pos)
        win.blit(game_students.stu2_selected, game_students.stu2_rect)
        game_students.AddStudents2()
        game_player.credit -= game_students.price2
    if mx > 1000 and my > 250 and my < 380 and game_player.credit >= game_students.price3:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu3_pos)
        win.blit(game_students.stu3_selected, game_students.stu3_rect)
        game_students.AddStudents3()
        game_player.credit -= game_students.price3
    if mx > 1000 and my > 380 and my < 510 and game_player.credit >= game_students.price4:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu4_pos)
        win.blit(game_students.stu4_selected, game_students.stu4_rect)
        game_students.AddStudents4()
        game_player.credit -= game_students.price4
    if mx > 1000 and my > 510 and my < 640 and game_player.credit >= game_students.price5:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu5_pos)
        win.blit(game_students.stu5_selected, game_students.stu5_rect)
        game_students.AddStudents5()
        game_player.credit -= game_students.price5
    if mx > 1000 and my > 640 and my < 770 and game_player.credit >= game_students.price6:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu6_pos)
        win.blit(game_students.stu6_selected, game_students.stu6_rect)
        game_students.AddStudents6()
        game_player.credit -= game_students.price6
    return game_player

def selectProduction(win, game_production, mx, my, game_player):
    if mx > 900 and mx < 980 and my < 120:
        game_production.git_nb_prod += 1
    if mx > 900 and mx < 980 and my > 120 and my < 250:
        game_production.boy_nb_prod += 1
    if mx > 900 and mx < 980 and my > 250 and my < 380:
        game_production.aztec_nb_prod += 1
    if mx > 900 and mx < 980 and my > 380 and my < 510:
        game_production.koala_nb_prod += 1
    if mx > 900 and mx < 980 and my > 510 and my < 640:
        game_production.monster_nb_prod += 1
    if mx > 900 and mx < 980 and my > 640 and my < 770:
        game_production.gourou_nb_prod += 1
    return game_production

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
                    game_production = selectProduction(win, game_production, mx, my, game_player)
                    game_player = selectStudents(win, game_students, mx, my, game_player)
        time.sleep(0.1)
        pygame.display.update()

        game_students.redrawStudents(game_player)
        game_production.updateQuantity(game_students)
        game_production.updateProduction()
        module.updateCredit(game_player.credit)
        game_player = module.updateProgressBar(to_add_module, game_player, game_students, game_production)
        to_add_module = 0
    return

# ----------------------- #
if __name__ == "__main__":
    main()
