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
    def __init__(self):
        self.color = darkblue
        self.pos = (0,0,400,800)
        self.img = pygame.image.load("../assets/module.png").convert_alpha()

        # Credits
        self.my_credits_display = "Credits : 0"
        self.credit_font = pygame.font.Font('freesansbold.ttf', 32)
        self.credit_text = self.credit_font.render(self.my_credits_display, True, lightgrey, darkblue)
        self.credit_textRect = self.credit_text.get_rect()
        self.credit_textRect.center = (200, 200)

    def displayCredit(self, own_credit):
        self.my_credits_display = "Credits : " + str(own_credit)
        self.credit_text = self.credit_font.render(self.my_credits_display, True, lightgrey, darkblue)

class Production:
    nb_github = 0

    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.github = pygame.image.load("../assets/github.png").convert_alpha()
        self.git_text = self.font.render('X ', True, lightgrey, grey)
        self.git_rect = self.git_text.get_rect()
        self.git_rect.center = (650, 80)

        self.schoolboy  = pygame.image.load("../assets/schoolboy.png").convert_alpha()
        self.boy_text = self.font.render('X ', True, lightgrey, grey)
        self.boy_rect = self.boy_text.get_rect()
        self.boy_rect.center = (650, 200)

        self.aztec  = pygame.image.load("../assets/aztec.png").convert_alpha()
        self.aztec_text = self.font.render('X ', True, lightgrey, grey)
        self.aztec_rect = self.aztec_text.get_rect()
        self.aztec_rect.center = (650, 320)

        self.koala  = pygame.image.load("../assets/koala.png").convert_alpha()
        self.koala_text = self.font.render('X ', True, lightgrey, grey)
        self.koala_rect = self.koala_text.get_rect()
        self.koala_rect.center = (650, 440)

        self.monster  = pygame.image.load("../assets/monster.png").convert_alpha()
        self.monster_text = self.font.render('X ', True, lightgrey, grey)
        self.monster_rect = self.monster_text.get_rect()
        self.monster_rect.center = (650, 560)

        self.gourou  = pygame.image.load("../assets/gourou.png").convert_alpha()
        self.gourou_text = self.font.render('X ', True, lightgrey, grey)
        self.gourou_rect = self.gourou_text.get_rect()
        self.gourou_rect.center = (650, 680)

class Separators:
    color = lightgrey
    h_pos_1 = (400,0,15,750)
    h_pos_2 = (600,0,5,750)
    h_pos_3 = (800,0,5,750)
    h_pos_4 = (900,0,5,750)
    h_pos_5 = (1005,0,15,750)
