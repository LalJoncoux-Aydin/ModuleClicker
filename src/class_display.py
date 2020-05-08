#!/usr/bin/env python3
import pygame, sys, time
from pygame.locals import *

# colors
blue = (0,0,255)
darkblue = (61, 90, 128)
violet = (67, 40, 79)
grey = (83, 98, 113)
white = (255,255,255)
black = (0, 0, 0)
grey = (11, 20, 35)
lightgrey = (174, 174, 175)
select_lightgrey = (210, 208, 202)

class Module:
    my_credits = 0

    def __init__(self):
        self.color = darkblue
        self.pos = (0,0,400,800)
        self.img = pygame.image.load("../assets/module.png").convert_alpha()

        # Credits
        self.my_credits_display = "Credits : " + str(self.my_credits)
        self.credit_font = pygame.font.Font('freesansbold.ttf', 32)
        self.credit_text = self.credit_font.render(self.my_credits_display, True, lightgrey, darkblue)
        self.credit_textRect = self.credit_text.get_rect()
        self.credit_textRect.center = (200, 200)

    def addCredit(self):
        self.my_credits += 1
        self.my_credits_display = "Credits : " + str(self.my_credits)
        self.credit_font = pygame.font.Font('freesansbold.ttf', 32)
        self.credit_text = self.credit_font.render(self.my_credits_display, True, lightgrey, darkblue)

class Students:
    nbStudents1 = 0
    nbStudents2 = 0
    nbStudents3 = 0
    nbStudents4 = 0
    nbStudents5 = 0
    nbStudents6 = 0

    def __init__(self):
        self.color = darkblue
        self.selected_color = select_lightgrey
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # Students 1
        self.stu1 = self.font.render('Githubber', True, lightgrey, darkblue)
        self.stu1_selected = self.font.render('Githubber', True, lightgrey, select_lightgrey)
        self.stu1_rect = self.stu1.get_rect()
        self.stu1_rect.center = (1270, 60)
        self.stu1_pos = (1000,0,800,120)

        # Students 2
        self.stu2 = self.font.render('Etudiant', True, lightgrey, darkblue)
        self.stu2_selected = self.font.render('Etudiant', True, lightgrey, select_lightgrey)
        self.stu2_rect = self.stu2.get_rect()
        self.stu2_rect.center = (1270, 190)
        self.stu2_pos = (1000,130,800,120)

        # Students 3
        self.stu3 = self.font.render('Astek', True, lightgrey, darkblue)
        self.stu3_selected = self.font.render('Astek', True, lightgrey, select_lightgrey)
        self.stu3_rect = self.stu3.get_rect()
        self.stu3_rect.center = (1270, 320)
        self.stu3_pos = (1000,260,800,120)

        # Students 4
        self.stu4 = self.font.render('Koala', True, lightgrey, darkblue)
        self.stu4_selected = self.font.render('Koala', True, lightgrey, select_lightgrey)
        self.stu4_rect = self.stu4.get_rect()
        self.stu4_rect.center = (1270, 450)
        self.stu4_pos = (1000,390,800,120)

        # Students 5
        self.stu5 = self.font.render('Monstre', True, lightgrey, darkblue)
        self.stu5_selected = self.font.render('Monstre', True, lightgrey, select_lightgrey)
        self.stu5_rect = self.stu5.get_rect()
        self.stu5_rect.center = (1270, 580)
        self.stu5_pos = (1000,520,800,120)

        # Students 6
        self.stu6 = self.font.render('Gourou', True, lightgrey, darkblue)
        self.stu6_selected = self.font.render('Gourou', True, lightgrey, select_lightgrey)
        self.stu6_rect = self.stu6.get_rect()
        self.stu6_rect.center = (1270, 700)
        self.stu6_pos = (1000,650,800,120)

    def AddStudents1(self):
        self.nbStudents1 += 1
    def AddStudents2(self):
        self.nbStudents2 += 1
    def AddStudents3(self):
        self.nbStudents3 += 1
    def AddStudents4(self):
        self.nbStudents4 += 1
    def AddStudents5(self):
        self.nbStudents5 += 1
    def AddStudents6(self):
        self.nbStudents6 += 1

class Production:
    def __init__(self):
        self.github = pygame.image.load("../assets/github.png").convert_alpha()
        self.schoolboy  = pygame.image.load("../assets/schoolboy.png").convert_alpha()
        self.aztec  = pygame.image.load("../assets/aztec.png").convert_alpha()
        self.koala  = pygame.image.load("../assets/koala.png").convert_alpha()
        self.monster  = pygame.image.load("../assets/monster.png").convert_alpha()
        self.gourou  = pygame.image.load("../assets/gourou.png").convert_alpha()
