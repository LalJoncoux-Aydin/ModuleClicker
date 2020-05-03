#!/usr/bin/env python3
import pygame, sys, time
from pygame.locals import *

# colors
blue = (0,0,255)
darkblue = (43, 40, 79)
violet = (67, 40, 79)
green = (0, 255, 0)
white = (255,255,255)

class Module:
    def __init__(self):
        self.color = blue
        self.pos = (0,0,400,800)
        self.img = pygame.image.load("module.jpg").convert_alpha()

class Students:
    def __init__(self):
        self.color = darkblue
        self.pos = (1000,0,800,800)
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # Player 1
        self.player1 = self.font.render('Githubber', True, green, darkblue)
        self.player1_Rect = self.player1.get_rect()
        self.player1_Rect.center = (1270, 100)

        # Player 2
        self.player2 = self.font.render('Etudiant lambda', True, green, darkblue)
        self.player2_Rect = self.player2.get_rect()
        self.player2_Rect.center = (1270, 220)

        # Player 3
        self.player3 = self.font.render('Etudiant motivé', True, green, darkblue)
        self.player3_Rect = self.player3.get_rect()
        self.player3_Rect.center = (1270, 340)

        # Player 4
        self.player4 = self.font.render('Etudiant déterminé', True, green, darkblue)
        self.player4_Rect = self.player4.get_rect()
        self.player4_Rect.center = (1270, 460)

        # Player 5
        self.player5 = self.font.render('Astek', True, green, darkblue)
        self.player5_Rect = self.player5.get_rect()
        self.player5_Rect.center = (1270, 570)

        # Player 6
        self.player6 = self.font.render('Monstre', True, green, darkblue)
        self.player6_Rect = self.player6.get_rect()
        self.player6_Rect.center = (1270, 680)
