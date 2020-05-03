#!/usr/bin/env python3
import pygame, sys, time
import class_display
from pygame.locals import *

def main():
    pygame.init()

    # Init screen
    win = pygame.display.set_mode((1500,750),0,32)
    win.fill(class_display.white)
    pygame.display.set_caption('Module Clicker')

    # Init graphical elements
    module = class_display.Module()
    students = class_display.Students()

    # Display graphical elements
    pygame.draw.rect(win, module.color, module.pos)
    pygame.draw.rect(win, students.color, students.pos)

    win.blit(module.img, (90,320))
    win.blit(students.player1, students.player1_Rect)
    win.blit(students.player2, students.player2_Rect)
    win.blit(students.player3, students.player3_Rect)
    win.blit(students.player4, students.player4_Rect)
    win.blit(students.player5, students.player5_Rect)
    win.blit(students.player6, students.player6_Rect)

    credits = 0
    credit_font = pygame.font.Font('freesansbold.ttf', 32)
    credits_display = "Credits : " + str(credits)
    credit_text = credit_font.render(credits_display, True, class_display.green, class_display.blue)
    credit_textRect = credit_text.get_rect()
    credit_textRect.center = (200, 200)
    win.blit(credit_text, credit_textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 90 and mx < 320 and my > 320 and my < 550:
                    credits += 1
                    credits_display = "Credits : " + str(credits)
                    credit_text = credit_font.render(credits_display, True, class_display.green, class_display.blue)
                    win.blit(credit_text, credit_textRect)
        time.sleep(0.03)
        pygame.display.update()
    return

# ----------------------- #
main()
