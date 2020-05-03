#!/usr/bin/env python3
import pygame, sys, time
from pygame.locals import *

# colors
blue = (0,0,255)
darkblue = (43, 40, 79)
violet = (67, 40, 79)
green = (0, 255, 0)
white = (255,255,255)
black = (0, 0, 0)

class Module:
    my_credits = 0

    def __init__(self):
        self.color = blue
        self.pos = (0,0,400,800)
        self.img = pygame.image.load("module.jpg").convert_alpha()

        # Credits
        self.my_credits_display = "Credits : " + str(self.my_credits)
        self.credit_font = pygame.font.Font('freesansbold.ttf', 32)
        self.credit_text = self.credit_font.render(self.my_credits_display, True, green, blue)
        self.credit_textRect = self.credit_text.get_rect()
        self.credit_textRect.center = (200, 200)

    def addCredit(self):
        self.my_credits += 1
        self.my_credits_display = "Credits : " + str(self.my_credits)
        self.credit_font = pygame.font.Font('freesansbold.ttf', 32)
        self.credit_text = self.credit_font.render(self.my_credits_display, True, green, blue)

class Students:
    def __init__(self):
        self.color = darkblue
        self.selected_color = white
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # Students 1
        self.stu1 = self.font.render('Githubber', True, green, darkblue)
        self.stu1_rect = self.stu1.get_rect()
        self.stu1_rect.center = (1270, 60)
        self.stu1_pos = (1000,0,800,120)

        # Students 2
        self.stu2 = self.font.render('Etudiant lambda', True, green, darkblue)
        self.stu2_rect = self.stu2.get_rect()
        self.stu2_rect.center = (1270, 190)
        self.stu2_pos = (1000,130,800,120)

        # Students 3
        self.stu3 = self.font.render('Etudiant motivé', True, green, darkblue)
        self.stu3_rect = self.stu3.get_rect()
        self.stu3_rect.center = (1270, 320)
        self.stu3_pos = (1000,260,800,120)

        # Students 4
        self.stu4 = self.font.render('Etudiant déterminé', True, green, darkblue)
        self.stu4_rect = self.stu4.get_rect()
        self.stu4_rect.center = (1270, 450)
        self.stu4_pos = (1000,390,800,120)

        # Students 5
        self.stu5 = self.font.render('Astek', True, green, darkblue)
        self.stu5_rect = self.stu5.get_rect()
        self.stu5_rect.center = (1270, 580)
        self.stu5_pos = (1000,520,800,120)

        # Students 6
        self.stu6 = self.font.render('Monstre', True, green, darkblue)
        self.stu6_rect = self.stu6.get_rect()
        self.stu6_rect.center = (1270, 700)
        self.stu6_pos = (1000,650,800,120)
