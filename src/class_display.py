#!/usr/bin/env python3
import pygame, sys, time
import student
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
violet = (85, 91, 110)

class Module:
    i = 52

    def __init__(self):
        self.color = darkblue
        self.pos = (0,0,400,800)
        self.img = pygame.image.load("../assets/module.png").convert_alpha()

        self.progress_color = white
        self.progress = pygame.image.load("../assets/progress.png").convert_alpha()
        self.progress_pos = (65, 550, 52, 44)

        # Credits
        self.my_credits_display = "Credits : 0"
        self.credit_font = pygame.font.Font('freesansbold.ttf', 32)
        self.credit_text = self.credit_font.render(self.my_credits_display, True, lightgrey, darkblue)
        self.credit_textRect = self.credit_text.get_rect()
        self.credit_textRect.center = (200, 130)

    def updateCredit(self, own_credit):
        self.my_credits_display = "Credits : " + str(own_credit)
        self.credit_text = self.credit_font.render(self.my_credits_display, True, lightgrey, darkblue)

    def updateProgressBar(self, to_add, game_player, game_students, game_production):
        self.progress_pos = (65, 550, self.i, 44)
        self.progress_color = grey
        self.i += to_add
        self.i += (game_students.nbStudents1 * game_production.git_nb_prod) + (game_students.nbStudents2 * game_production.boy_nb_prod) + (game_students.nbStudents3 * game_production.aztec_nb_prod) + (game_students.nbStudents4 * game_production.koala_nb_prod) + (game_students.nbStudents5 * game_production.monster_nb_prod) + (game_students.nbStudents5 * game_production.gourou_nb_prod)
        if self.i >= 290:
            self.i = 0
            game_player.credit += 1
        return game_player

class Separators:
    color = lightgrey
    h_pos_1 = (400,0,15,750)
    h_pos_2 = (570,0,5,750)
    h_pos_3 = (690,0,5,750)
    h_pos_4 = (875,0,5,750)
    h_pos_5 = (1005,0,15,750)
