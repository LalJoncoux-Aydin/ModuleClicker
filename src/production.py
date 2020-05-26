#!/usr/bin/env python3
import pygame, sys, time
import class_display
from pygame.locals import *

class Production:
    nb_github = 0

    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.upgrade = pygame.image.load("../assets/upgrade.png").convert_alpha()
        self.upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()

        self.github = pygame.image.load("../assets/github.png").convert_alpha()
        self.git_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.git_rect = self.git_text.get_rect()
        self.git_rect.center = (630, 70)
        self.git_prod = self.font.render('+ 1 prod', True, class_display.lightgrey, class_display.grey)
        self.git_prod_rect = self.git_prod.get_rect()
        self.git_prod_rect.center = (780, 70)

        self.schoolboy  = pygame.image.load("../assets/schoolboy.png").convert_alpha()
        self.boy_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.boy_prod = self.font.render(' + 1 prod ', True, class_display.lightgrey, class_display.grey)
        self.boy_rect = self.boy_text.get_rect()
        self.boy_rect.center = (630, 190)
        self.boy_prod_rect = self.boy_prod.get_rect()
        self.boy_prod_rect.center = (780, 190)

        self.aztec  = pygame.image.load("../assets/aztec.png").convert_alpha()
        self.aztec_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.aztec_prod = self.font.render(' + 1 prod ', True, class_display.lightgrey, class_display.grey)
        self.aztec_rect = self.aztec_text.get_rect()
        self.aztec_rect.center = (630, 315)
        self.aztec_prod_rect = self.aztec_prod.get_rect()
        self.aztec_prod_rect.center = (780, 315)

        self.koala  = pygame.image.load("../assets/koala.png").convert_alpha()
        self.koala_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.koala_prod = self.font.render(' + 1 prod ', True, class_display.lightgrey, class_display.grey)
        self.koala_rect = self.koala_text.get_rect()
        self.koala_rect.center = (630, 440)
        self.koala_prod_rect = self.koala_prod.get_rect()
        self.koala_prod_rect.center = (780, 440)

        self.monster  = pygame.image.load("../assets/monster.png").convert_alpha()
        self.monster_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.monster_prod = self.font.render(' + 1 prod', True, class_display.lightgrey, class_display.grey)
        self.monster_rect = self.monster_text.get_rect()
        self.monster_rect.center = (630, 570)
        self.monster_prod_rect = self.monster_prod.get_rect()
        self.monster_prod_rect.center = (780, 570)

        self.gourou  = pygame.image.load("../assets/gourou.png").convert_alpha()
        self.gourou_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.gourou_prod = self.font.render(' + 1 prod ', True, class_display.lightgrey, class_display.grey)
        self.gourou_rect = self.gourou_text.get_rect()
        self.gourou_rect.center = (630, 690)
        self.gourou_prod_rect = self.gourou_prod.get_rect()
        self.gourou_prod_rect.center = (780, 690)

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
