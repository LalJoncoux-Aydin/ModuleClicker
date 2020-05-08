#!/usr/bin/env python3
import pygame, sys, time
import class_display
from pygame.locals import *

class Production:
    nb_github = 0

    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.github = pygame.image.load("../assets/github.png").convert_alpha()
        self.git_text = self.font.render('X ', True, class_display.lightgrey, class_display.grey)
        self.git_rect = self.git_text.get_rect()
        self.git_rect.center = (650, 80)

        self.schoolboy  = pygame.image.load("../assets/schoolboy.png").convert_alpha()
        self.boy_text = self.font.render('X ', True, class_display.lightgrey, class_display.grey)
        self.boy_rect = self.boy_text.get_rect()
        self.boy_rect.center = (650, 200)

        self.aztec  = pygame.image.load("../assets/aztec.png").convert_alpha()
        self.aztec_text = self.font.render('X ', True, class_display.lightgrey, class_display.grey)
        self.aztec_rect = self.aztec_text.get_rect()
        self.aztec_rect.center = (650, 320)

        self.koala  = pygame.image.load("../assets/koala.png").convert_alpha()
        self.koala_text = self.font.render('X ', True, class_display.lightgrey, class_display.grey)
        self.koala_rect = self.koala_text.get_rect()
        self.koala_rect.center = (650, 440)

        self.monster  = pygame.image.load("../assets/monster.png").convert_alpha()
        self.monster_text = self.font.render('X ', True, class_display.lightgrey, class_display.grey)
        self.monster_rect = self.monster_text.get_rect()
        self.monster_rect.center = (650, 560)

        self.gourou  = pygame.image.load("../assets/gourou.png").convert_alpha()
        self.gourou_text = self.font.render('X ', True, class_display.lightgrey, class_display.grey)
        self.gourou_rect = self.gourou_text.get_rect()
        self.gourou_rect.center = (650, 680)
