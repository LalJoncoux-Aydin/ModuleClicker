#!/usr/bin/env python3
import pygame, sys, time
from pygame.locals import *

# colors
blue = (0,0,255)
darkblue = (61, 90, 128)
grey = (83, 98, 113)
white = (255,255,255)
black = (0, 0, 0)
grey = (11, 20, 35)
lightgrey = (174, 174, 175)
select_lightgrey = (210, 208, 202)
violet = (131, 52, 113)

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

    def updateCredit(self, own_credit):
        self.my_credits_display = "Credits : " + str(own_credit)
        self.credit_text = self.credit_font.render(self.my_credits_display, True, lightgrey, darkblue)

class Separators:
    color = lightgrey
    h_pos_1 = (400,0,15,750)
    h_pos_2 = (575,0,5,750)
    h_pos_3 = (730,0,5,750)
    h_pos_4 = (875,0,5,750)
    h_pos_5 = (1005,0,15,750)
