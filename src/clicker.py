#!/usr/bin/env python3
import pygame, sys, time
import class_display
import player
import student
import display
from pygame.locals import *

def selectStudents(win, game_students, mx, my):
    if mx > 1000 and my < 120:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu1_pos)
        win.blit(game_students.stu1_selected, game_students.stu1_rect)
        game_students.AddStudents1()
    if mx > 1000 and my > 120 and my < 250:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu2_pos)
        win.blit(game_students.stu2_selected, game_students.stu2_rect)
        game_students.AddStudents2()
    if mx > 1000 and my > 250 and my < 380:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu3_pos)
        win.blit(game_students.stu3_selected, game_students.stu3_rect)
        game_students.AddStudents3()
    if mx > 1000 and my > 380 and my < 510:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu4_pos)
        win.blit(game_students.stu4_selected, game_students.stu4_rect)
        game_students.AddStudents4()
    if mx > 1000 and my > 510 and my < 640:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu5_pos)
        win.blit(game_students.stu5_selected, game_students.stu5_rect)
        game_students.AddStudents5()
    if mx > 1000 and my > 640 and my < 770:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu6_pos)
        win.blit(game_students.stu6_selected, game_students.stu6_rect)
        game_students.AddStudents6()
    return

def main():
    pygame.init()

    # Init screen
    win = pygame.display.set_mode((1500,750),0,32)
    pygame.display.set_caption('Module Clicker')

    # Init graphic
    game_player = player.Player()
    module = class_display.Module()
    game_students = student.Students()
    separators = class_display.Separators()
    production = class_display.Production()

    while True:
        # if game_player.stu_ready == True:
        #     game_player.addCredit(students.to_add_total)

        win.fill(class_display.grey)
        display.displayModule(win, module)
        display.displayStudents(win, game_students)
        display.displaySeparators(win, separators)
        display.displayProduction(win, game_students, production)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 90 and mx < 320 and my > 320 and my < 550:
                    game_player.addCredit(1)
                    module.displayCredit(game_player.credit)
                    win.blit(module.credit_text, module.credit_textRect)
                selectStudents(win, game_students, mx, my)
        pygame.display.update()
        time.sleep(0.1)
        pygame.display.update()
    return

# ----------------------- #
if __name__ == "__main__":
    main()
