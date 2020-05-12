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

    while True:
        # if game_player.stu_ready == True:
        #     game_player.addCredit(students.to_add_total)
        game_students.redrawStudents(game_player)
        game_students.updateTotal()
        game_production.updateQuantity(game_students)
        module.updateCredit(game_player.credit)
        game_player = module.updateProgressBar(game_students.totalNbStudents, game_player)

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
                    module.updateProgressBar(20, game_player)
                    win.blit(module.credit_text, module.credit_textRect)
                else:
                    game_player = selectStudents(win, game_students, mx, my, game_player)
        time.sleep(0.1)
        pygame.display.update()
    return

# ----------------------- #
if __name__ == "__main__":
    main()
