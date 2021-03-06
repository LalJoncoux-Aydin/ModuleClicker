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
        self.git_rect.center = (620, 70)
        self.git_nb_prod = 1
        git_nb_prod_str = "+ " + str(self.git_nb_prod) + " prod"
        self.git_prod = self.font.render(git_nb_prod_str, True, class_display.lightgrey, class_display.grey)
        self.git_prod_rect = self.git_prod.get_rect()
        self.git_prod_rect.center = (780, 70)
        self.git_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
        self.git_upgradable = False

        self.schoolboy  = pygame.image.load("../assets/schoolboy.png").convert_alpha()
        self.boy_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.boy_rect = self.boy_text.get_rect()
        self.boy_rect.center = (620, 190)
        self.boy_nb_prod = 2
        boy_nb_prod_str = "+ " + str(self.boy_nb_prod) + " prod"
        self.boy_prod = self.font.render(boy_nb_prod_str, True, class_display.lightgrey, class_display.grey)
        self.boy_prod_rect = self.boy_prod.get_rect()
        self.boy_prod_rect.center = (780, 190)
        self.boy_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
        self.boy_upgradable = False

        self.aztec  = pygame.image.load("../assets/aztec.png").convert_alpha()
        self.aztec_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.aztec_rect = self.aztec_text.get_rect()
        self.aztec_rect.center = (620, 315)
        self.aztec_nb_prod = 3
        aztec_nb_prod_str = "+ " + str(self.aztec_nb_prod) + " prod"
        self.aztec_prod = self.font.render(aztec_nb_prod_str, True, class_display.lightgrey, class_display.grey)
        self.aztec_prod_rect = self.aztec_prod.get_rect()
        self.aztec_prod_rect.center = (780, 315)
        self.aztec_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
        self.aztec_upgradable = False

        self.koala  = pygame.image.load("../assets/koala.png").convert_alpha()
        self.koala_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.koala_rect = self.koala_text.get_rect()
        self.koala_rect.center = (620, 440)
        self.koala_nb_prod = 4
        koala_nb_prod_str = "+ " + str(self.koala_nb_prod) + " prod"
        self.koala_prod = self.font.render(koala_nb_prod_str, True, class_display.lightgrey, class_display.grey)
        self.koala_prod_rect = self.koala_prod.get_rect()
        self.koala_prod_rect.center = (780, 440)
        self.koala_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
        self.koala_upgradable = False

        self.monster  = pygame.image.load("../assets/monster.png").convert_alpha()
        self.monster_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.monster_rect = self.monster_text.get_rect()
        self.monster_rect.center = (620, 570)
        self.monster_nb_prod = 5
        monster_nb_prod_str = "+ " + str(self.monster_nb_prod) + " prod"
        self.monster_prod = self.font.render(monster_nb_prod_str, True, class_display.lightgrey, class_display.grey)
        self.monster_prod_rect = self.monster_prod.get_rect()
        self.monster_prod_rect.center = (780, 570)
        self.monster_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
        self.monster_upgradable = False

        self.gourou  = pygame.image.load("../assets/gourou.png").convert_alpha()
        self.gourou_text = self.font.render('x 0', True, class_display.lightgrey, class_display.grey)
        self.gourou_rect = self.gourou_text.get_rect()
        self.gourou_rect.center = (620, 690)
        self.gourou_nb_prod = 6
        gourou_nb_prod_str = "+ " + str(self.gourou_nb_prod) + " prod"
        self.gourou_prod = self.font.render(gourou_nb_prod_str, True, class_display.lightgrey, class_display.grey)
        self.gourou_prod_rect = self.gourou_prod.get_rect()
        self.gourou_prod_rect.center = (780, 690)
        self.gourou_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
        self.gourou_upgradable = False

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

    def updateProduction(self):
        git_nb_prod_str = "+ " + str(self.git_nb_prod) + " prod"
        self.git_prod = self.font.render(git_nb_prod_str, True, class_display.lightgrey, class_display.grey)

        boy_nb_prod_str = "+ " + str(self.boy_nb_prod) + " prod"
        self.boy_prod = self.font.render(boy_nb_prod_str, True, class_display.lightgrey, class_display.grey)

        aztec_nb_prod_str = "+ " + str(self.aztec_nb_prod) + " prod"
        self.aztec_prod = self.font.render(aztec_nb_prod_str, True, class_display.lightgrey, class_display.grey)

        koala_nb_prod_str = "+ " + str(self.koala_nb_prod) + " prod"
        self.koala_prod = self.font.render(koala_nb_prod_str, True, class_display.lightgrey, class_display.grey)

        monster_nb_prod_str = "+ " + str(self.monster_nb_prod) + " prod"
        self.monster_prod = self.font.render(monster_nb_prod_str, True, class_display.lightgrey, class_display.grey)

        gourou_nb_prod_str = "+ " + str(self.gourou_nb_prod) + " prod"
        self.gourou_prod = self.font.render(gourou_nb_prod_str, True, class_display.lightgrey, class_display.grey)

    def updateUpgrade(self, game_player, game_students):
        if game_player.credit >= 1 and game_students.nbStudents1 > 0:
            self.git_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus_selected.png").convert_alpha()
            self.git_upgradable = True
        else:
            self.git_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
            self.git_upgradable = False

        if game_player.credit >= 2 and game_students.nbStudents2 > 0:
            self.boy_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus_selected.png").convert_alpha()
            self.boy_upgradable = True
        else:
            self.boy_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
            self.boy_upgradable = False

        if game_player.credit >= 3 and game_students.nbStudents3 > 0:
            self.aztec_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus_selected.png").convert_alpha()
            self.aztec_upgradable = True
        else:
            self.aztec_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
            self.aztec_upgradable = False

        if game_player.credit >= 4 and game_students.nbStudents4 > 0:
            self.koala_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus_selected.png").convert_alpha()
            self.koala_upgradable = True
        else:
            self.koala_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
            self.koala_upgradable = False

        if game_player.credit >= 5 and game_students.nbStudents5 > 0:
            self.monster_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus_selected.png").convert_alpha()
            self.monster_upgradable = True
        else:
            self.monster_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
            self.monster_upgradable = False

        if game_player.credit >= 6 and game_students.nbStudents6 > 0:
            self.gourou_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus_selected.png").convert_alpha()
            self.gourou_upgradable = True
        else:
            self.gourou_upgrade_bonus = pygame.image.load("../assets/upgrade_bonus.png").convert_alpha()
            self.gourou_upgradable = False
