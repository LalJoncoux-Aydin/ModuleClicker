#!/usr/bin/env python3
import pygame, sys, time
import class_display
from pygame.locals import *

def displayModule(win, module):
    pygame.draw.rect(win, module.color, module.pos)
    win.blit(module.img, (90,320))
    win.blit(module.credit_text, module.credit_textRect)
    return

def displayStudents(win, students):
    pygame.draw.rect(win, students.color, students.stu1_pos)
    win.blit(students.stu1, students.stu1_rect)
    pygame.draw.rect(win, students.color, students.stu2_pos)
    win.blit(students.stu2, students.stu2_rect)
    pygame.draw.rect(win, students.color, students.stu3_pos)
    win.blit(students.stu3, students.stu3_rect)
    pygame.draw.rect(win, students.color, students.stu4_pos)
    win.blit(students.stu4, students.stu4_rect)
    pygame.draw.rect(win, students.color, students.stu5_pos)
    win.blit(students.stu5, students.stu5_rect)
    pygame.draw.rect(win, students.color, students.stu6_pos)
    win.blit(students.stu6, students.stu6_rect)
    return


def displayProduction(win, students, production):
    if students.nbStudents1 > 0:
        win.blit(production.github, (450,20))
    if students.nbStudents2 > 0:
        win.blit(production.schoolboy, (450,140))
    if students.nbStudents3 > 0:
        win.blit(production.aztec, (450,250))
    if students.nbStudents4 > 0:
        win.blit(production.koala, (450,380))
    if students.nbStudents5 > 0:
        win.blit(production.monster, (450,550))
    if students.nbStudents6 > 0:
        win.blit(production.gourou, (450,650))
    return

def selectStudents(win, students, mx, my):
    if mx > 1000 and my < 120:
        pygame.draw.rect(win, students.selected_color, students.stu1_pos)
        win.blit(students.stu1_selected, students.stu1_rect)
        students.AddStudents1()
    if mx > 1000 and my > 120 and my < 250:
        pygame.draw.rect(win, students.selected_color, students.stu2_pos)
        win.blit(students.stu2_selected, students.stu2_rect)
        students.AddStudents2()
    if mx > 1000 and my > 250 and my < 380:
        pygame.draw.rect(win, students.selected_color, students.stu3_pos)
        win.blit(students.stu3_selected, students.stu3_rect)
        students.AddStudents3()
    if mx > 1000 and my > 380 and my < 510:
        pygame.draw.rect(win, students.selected_color, students.stu4_pos)
        win.blit(students.stu4_selected, students.stu4_rect)
        students.AddStudents4()
    if mx > 1000 and my > 510 and my < 640:
        pygame.draw.rect(win, students.selected_color, students.stu5_pos)
        win.blit(students.stu5_selected, students.stu5_rect)
        students.AddStudents5()
    if mx > 1000 and my > 640 and my < 770:
        pygame.draw.rect(win, students.selected_color, students.stu6_pos)
        win.blit(students.stu6_selected, students.stu6_rect)
        students.AddStudents6()
    return

def main():
    pygame.init()

    # Init screen
    win = pygame.display.set_mode((1500,750),0,32)
    win.fill(class_display.grey)
    pygame.display.set_caption('Module Clicker')

    # Init Module clicking part
    module = class_display.Module()
    displayModule(win, module)

    # Init and draw Students buying part
    students = class_display.Students()
    displayStudents(win, students)

    # Init and draw Students displaying part
    production = class_display.Production()
#    displayProduction(win, students, production)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 90 and mx < 320 and my > 320 and my < 550:
                    module.addCredit()
                    win.blit(module.credit_text, module.credit_textRect)
                selectStudents(win, students, mx, my)
        pygame.display.update()
        time.sleep(0.1)
        displayStudents(win, students)
        displayProduction(win, students, production)
        pygame.display.update()
    return

# ----------------------- #
if __name__ == "__main__":
    main()
