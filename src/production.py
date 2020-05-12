#!/usr/bin/env python3
import pygame, sys, time
import class_display
from pygame.locals import *

class Production:
    nb_github = 0

    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.github = pygame.image.load("../assets/github.png").convert_alpha()
        self.git_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.git_rect = self.git_text.get_rect()
        self.git_rect.center = (650, 70)

        self.schoolboy  = pygame.image.load("../assets/schoolboy.png").convert_alpha()
        self.boy_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.boy_rect = self.boy_text.get_rect()
        self.boy_rect.center = (650, 190)

        self.aztec  = pygame.image.load("../assets/aztec.png").convert_alpha()
        self.aztec_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.aztec_rect = self.aztec_text.get_rect()
        self.aztec_rect.center = (650, 315)

        self.koala  = pygame.image.load("../assets/koala.png").convert_alpha()
        self.koala_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.koala_rect = self.koala_text.get_rect()
        self.koala_rect.center = (650, 440)

        self.monster  = pygame.image.load("../assets/monster.png").convert_alpha()
        self.monster_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.monster_rect = self.monster_text.get_rect()
        self.monster_rect.center = (650, 570)

        self.gourou  = pygame.image.load("../assets/gourou.png").convert_alpha()
        self.gourou_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.gourou_rect = self.gourou_text.get_rect()
        self.gourou_rect.center = (650, 690)

    def updateQuantity(self, game_students):
        git_cl_text = 'x ' + str(game_students.nbStudents1)
        self.git_text = self.font.render(git_cl_text, True, class_display.lightgrey, class_display.grey)

        boy_cl_text = 'x ' + str(game_students.nbStudents2)
        self.boy_text = self.font.render(boy_cl_text, True, class_display.lightgrey, class_display.grey)

        aztec_cl_text = 'x ' + str(game_students.nbStudents3)
        self.aztec_text = self.font.render(aztec_cl_text, True, class_display.lightgrey, class_display.grey)

        koala_cl_text = 'x ' + str(game_students.nbStudents4)
        self.koala_text = self.font.render(koala_cl_text, True, class_display.lightgrey, class_display.grey)

        monster_cl_text = 'x ' + str(game_students.nbStudents5)
        self.monster_text = self.font.render(monster_cl_text, True, class_display.lightgrey, class_display.grey)

        gourou_cl_text = 'x ' + str(game_students.nbStudents6)
        self.gourou_text = self.font.render(gourou_cl_text, True, class_display.lightgrey, class_display.grey)
