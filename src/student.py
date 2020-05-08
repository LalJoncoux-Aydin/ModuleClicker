#!/usr/bin/env python3
import pygame, sys, time
import class_display
from pygame.locals import *

class Students:
    nbStudents1 = 0
    nbStudents2 = 0
    nbStudents3 = 0
    nbStudents4 = 0
    nbStudents5 = 0
    nbStudents6 = 0

    def __init__(self):
        self.color = class_display.darkblue
        self.selected_color = class_display.select_lightgrey
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # Students 1
        self.stu1 = self.font.render('Githubber', True, class_display.lightgrey, class_display.darkblue)
        self.stu1_selected = self.font.render('Githubber', True, class_display.lightgrey, class_display.select_lightgrey)
        self.stu1_rect = self.stu1.get_rect()
        self.stu1_rect.center = (1270, 60)
        self.stu1_pos = (1020,0,800,120)

        # Students 2
        self.stu2 = self.font.render('Etudiant', True, class_display.lightgrey, class_display.darkblue)
        self.stu2_selected = self.font.render('Etudiant', True, class_display.lightgrey, class_display.select_lightgrey)
        self.stu2_rect = self.stu2.get_rect()
        self.stu2_rect.center = (1270, 190)
        self.stu2_pos = (1020,130,800,120)

        # Students 3
        self.stu3 = self.font.render('Astek', True, class_display.lightgrey, class_display.darkblue)
        self.stu3_selected = self.font.render('Astek', True, class_display.lightgrey, class_display.select_lightgrey)
        self.stu3_rect = self.stu3.get_rect()
        self.stu3_rect.center = (1270, 320)
        self.stu3_pos = (1020,260,800,120)

        # Students 4
        self.stu4 = self.font.render('Koala', True, class_display.lightgrey, class_display.darkblue)
        self.stu4_selected = self.font.render('Koala', True, class_display.lightgrey, class_display.select_lightgrey)
        self.stu4_rect = self.stu4.get_rect()
        self.stu4_rect.center = (1270, 450)
        self.stu4_pos = (1020,390,800,120)

        # Students 5
        self.stu5 = self.font.render('Monstre', True, class_display.lightgrey, class_display.darkblue)
        self.stu5_selected = self.font.render('Monstre', True, class_display.lightgrey, class_display.select_lightgrey)
        self.stu5_rect = self.stu5.get_rect()
        self.stu5_rect.center = (1270, 580)
        self.stu5_pos = (1020,520,800,120)

        # Students 6
        self.stu6 = self.font.render('Gourou', True, class_display.lightgrey, class_display.darkblue)
        self.stu6_selected = self.font.render('Gourou', True, class_display.lightgrey, class_display.select_lightgrey)
        self.stu6_rect = self.stu6.get_rect()
        self.stu6_rect.center = (1270, 700)
        self.stu6_pos = (1020,650,800,120)

    def AddStudents1(self):
        self.nbStudents1 += 1
        return 1
    def AddStudents2(self):
        self.nbStudents2 += 2
        return 2
    def AddStudents3(self):
        self.nbStudents3 += 3
        return 3
    def AddStudents4(self):
        self.nbStudents4 += 4
        return 4
    def AddStudents5(self):
        self.nbStudents5 += 5
        return 5
    def AddStudents6(self):
        self.nbStudents6 += 6
        return 6
