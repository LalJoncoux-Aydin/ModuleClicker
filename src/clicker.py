#!/usr/bin/env python3
import pygame, sys, time
from pygame.locals import *

class Rectangle:
    color = ()
    pos = ()

class Module:
    # Variables
    # Methods
    def __init__(self):
        self.color = (67, 40, 79)
        self.pos = (0,0,1500,100)
        self.img = pygame.image.load("module.jpg").convert_alpha()

def makeModule():
    module = Rectangle()
    module.color = (0,0,255)
    module.pos = (130,180,500,500)
    module.img = pygame.image.load("module.jpg").convert_alpha()
    return module

def makeInfoBar():
    infobar = Rectangle()
    infobar.color = (67, 40, 79)
    infobar.pos = (0,0,1500,100)

    infobar.font = pygame.font.Font('freesansbold.ttf', 32)
    green = (0, 255, 0)
    blue =  (67, 40, 79)
    infobar.text = infobar.font.render('Credits : ', True, green, blue)
    infobar.textRect = infobar.text.get_rect()
    infobar.textRect.center = (600, 50)
    return infobar

def makeStudents():
    students = Rectangle()
    students.color = (43, 40, 79)
    students.pos = (800,100,800,800)

    students.font = pygame.font.Font('freesansbold.ttf', 32)
    green = (0, 255, 0)
    blue =  (67, 40, 79)
    students.text = students.font.render('Githubber', True, green, blue)
    students.textRect = students.text.get_rect()
    students.textRect.center = (1000, 200)
    return students

def main():
    pygame.init()

    win = pygame.display.set_mode((1500,750),0,32)
    white = (255,255,255)
    win.fill(white)
    pygame.display.set_caption('Module Clicker')

    module = makeModule()
    infobar = makeInfoBar()
    students = makeStudents()

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
