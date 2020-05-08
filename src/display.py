#!/usr/bin/env python3
import pygame, sys, time
from pygame.locals import *

def displayModule(win, module):
    pygame.draw.rect(win, module.color, module.pos)
    win.blit(module.img, (90,320))
    win.blit(module.credit_text, module.credit_textRect)
    return

def displayStudents(win, game_students):
    pygame.draw.rect(win, game_students.color, game_students.stu1_pos)
    win.blit(game_students.stu1, game_students.stu1_rect)
    pygame.draw.rect(win, game_students.color, game_students.stu2_pos)
    win.blit(game_students.stu2, game_students.stu2_rect)
    pygame.draw.rect(win, game_students.color, game_students.stu3_pos)
    win.blit(game_students.stu3, game_students.stu3_rect)
    pygame.draw.rect(win, game_students.color, game_students.stu4_pos)
    win.blit(game_students.stu4, game_students.stu4_rect)
    pygame.draw.rect(win, game_students.color, game_students.stu5_pos)
    win.blit(game_students.stu5, game_students.stu5_rect)
    pygame.draw.rect(win, game_students.color, game_students.stu6_pos)
    win.blit(game_students.stu6, game_students.stu6_rect)
    return

def displayProduction(win, students, production):
    win.blit(production.github, (450,20))
    win.blit(production.git_text, production.git_rect)

    win.blit(production.schoolboy, (450,140))
    win.blit(production.boy_text, production.boy_rect)

    win.blit(production.aztec, (450,250))
    win.blit(production.aztec_text, production.aztec_rect)

    win.blit(production.koala, (450,380))
    win.blit(production.koala_text, production.koala_rect)

    win.blit(production.monster, (450,550))
    win.blit(production.monster_text, production.monster_rect)

    win.blit(production.gourou, (450,650))
    win.blit(production.gourou_text, production.gourou_rect)
    return

def displaySeparators(win, separators):
    pygame.draw.rect(win, separators.color, separators.h_pos_1)
    pygame.draw.rect(win, separators.color, separators.h_pos_2)
    pygame.draw.rect(win, separators.color, separators.h_pos_3)
    pygame.draw.rect(win, separators.color, separators.h_pos_4)
    pygame.draw.rect(win, separators.color, separators.h_pos_5)
