#!/usr/bin/env python3
import pygame, sys, time
from pygame.locals import *

def displayModule(win, module):
    pygame.draw.rect(win, module.color, module.pos)
    pygame.draw.rect(win, module.progress_color, module.progress_pos)
    win.blit(module.img, (90,230))
    win.blit(module.progress, (60,550))
    win.blit(module.credit_text, module.credit_textRect)
    return

def displayStudents(win, game_students):
    pygame.draw.rect(win, game_students.stu1_color, game_students.stu1_pos)
    win.blit(game_students.coin, (1285,38))
    win.blit(game_students.stu1, game_students.stu1_rect)
    win.blit(game_students.stu1_price, game_students.stu1_price_rect)
    pygame.draw.rect(win, game_students.stu2_color, game_students.stu2_pos)
    win.blit(game_students.coin, (1285,168))
    win.blit(game_students.stu2, game_students.stu2_rect)
    win.blit(game_students.stu2_price, game_students.stu2_price_rect)
    pygame.draw.rect(win, game_students.stu3_color, game_students.stu3_pos)
    win.blit(game_students.coin, (1285,298))
    win.blit(game_students.stu3, game_students.stu3_rect)
    win.blit(game_students.stu3_price, game_students.stu3_price_rect)
    pygame.draw.rect(win, game_students.stu4_color, game_students.stu4_pos)
    win.blit(game_students.coin, (1285,428))
    win.blit(game_students.stu4, game_students.stu4_rect)
    win.blit(game_students.stu4_price, game_students.stu4_price_rect)
    pygame.draw.rect(win, game_students.stu5_color, game_students.stu5_pos)
    win.blit(game_students.coin, (1285,558))
    win.blit(game_students.stu5, game_students.stu5_rect)
    win.blit(game_students.stu5_price, game_students.stu5_price_rect)
    pygame.draw.rect(win, game_students.stu6_color, game_students.stu6_pos)
    win.blit(game_students.coin, (1285,678))
    win.blit(game_students.stu6, game_students.stu6_rect)
    win.blit(game_students.stu6_price, game_students.stu6_price_rect)
    return

def displayProduction(win, game_production):
    win.blit(game_production.github, (445,20))
    win.blit(game_production.git_upgrade_bonus, (900,30))
    win.blit(game_production.git_text, game_production.git_rect)
    win.blit(game_production.git_prod, game_production.git_prod_rect)

    win.blit(game_production.schoolboy, (445,130))
    win.blit(game_production.boy_upgrade_bonus, (900,150))
    win.blit(game_production.boy_text, game_production.boy_rect)
    win.blit(game_production.boy_prod, game_production.boy_prod_rect)

    win.blit(game_production.aztec, (440,245))
    win.blit(game_production.aztec_upgrade_bonus, (900,280))
    win.blit(game_production.aztec_text, game_production.aztec_rect)
    win.blit(game_production.aztec_prod, game_production.aztec_prod_rect)

    win.blit(game_production.koala, (435,375))
    win.blit(game_production.koala_upgrade_bonus, (900,400))
    win.blit(game_production.koala_text, game_production.koala_rect)
    win.blit(game_production.koala_prod, game_production.koala_prod_rect)

    win.blit(game_production.monster, (453,530))
    win.blit(game_production.monster_upgrade_bonus, (900,530))
    win.blit(game_production.monster_text, game_production.monster_rect)
    win.blit(game_production.monster_prod, game_production.monster_prod_rect)

    win.blit(game_production.gourou, (455,640))
    win.blit(game_production.gourou_upgrade_bonus, (900,650))
    win.blit(game_production.gourou_text, game_production.gourou_rect)
    win.blit(game_production.gourou_prod, game_production.gourou_prod_rect)
    return

def displaySeparators(win, separators):
    pygame.draw.rect(win, separators.color, separators.h_pos_1)
    pygame.draw.rect(win, separators.color, separators.h_pos_2)
    pygame.draw.rect(win, separators.color, separators.h_pos_3)
    pygame.draw.rect(win, separators.color, separators.h_pos_4)
    pygame.draw.rect(win, separators.color, separators.h_pos_5)
