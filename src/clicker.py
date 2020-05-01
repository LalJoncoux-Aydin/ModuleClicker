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
    infobar = class_display.InfoBar()
    students = class_display.Students()

    # Display graphical elements
    pygame.draw.rect(win, module.color, module.pos)
    pygame.draw.rect(win, infobar.color, infobar.pos)
    pygame.draw.rect(win, students.color, students.pos)

    win.blit(module.img, (280,320))
    win.blit(infobar.text, infobar.textRect)
    win.blit(students.text, students.textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
        time.sleep(0.03)
        pygame.display.update()
    return

# ----------------------- #
main()
