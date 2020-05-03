#!/usr/bin/env python3
import pygame, sys, time
import class_display
from pygame.locals import *

def main():
    pygame.init()

    # Init screen
    win = pygame.display.set_mode((1500,750),0,32)
    win.fill(class_display.black)
    pygame.display.set_caption('Module Clicker')

    # Init Module clicking part
    module = class_display.Module()
    pygame.draw.rect(win, module.color, module.pos)
    win.blit(module.img, (90,320))
    win.blit(module.credit_text, module.credit_textRect)

    # Init and draw Students buying part
    students = class_display.Students()
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

    # Init and draw Students displaying part

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
        time.sleep(0.03)
        pygame.display.update()
    return

# ----------------------- #
main()
