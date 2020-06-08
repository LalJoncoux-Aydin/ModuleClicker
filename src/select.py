#!/usr/bin/env python3
import pygame, sys, time
from pygame.locals import *

def selectStudents(win, game_students, mx, my, game_player):
    if mx > 1000 and my < 120 and game_player.credit >= game_students.price1:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu1_pos)
        win.blit(game_students.stu1_selected, game_students.stu1_rect)
        game_students.AddStudents1()
        game_player.credit -=  game_students.price1
    if mx > 1000 and my > 120 and my < 250 and game_player.credit >= game_students.price2:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu2_pos)
        win.blit(game_students.stu2_selected, game_students.stu2_rect)
        game_students.AddStudents2()
        game_player.credit -= game_students.price2
    if mx > 1000 and my > 250 and my < 380 and game_player.credit >= game_students.price3:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu3_pos)
        win.blit(game_students.stu3_selected, game_students.stu3_rect)
        game_students.AddStudents3()
        game_player.credit -= game_students.price3
    if mx > 1000 and my > 380 and my < 510 and game_player.credit >= game_students.price4:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu4_pos)
        win.blit(game_students.stu4_selected, game_students.stu4_rect)
        game_students.AddStudents4()
        game_player.credit -= game_students.price4
    if mx > 1000 and my > 510 and my < 640 and game_player.credit >= game_students.price5:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu5_pos)
        win.blit(game_students.stu5_selected, game_students.stu5_rect)
        game_students.AddStudents5()
        game_player.credit -= game_students.price5
    if mx > 1000 and my > 640 and my < 770 and game_player.credit >= game_students.price6:
        pygame.draw.rect(win, game_students.selected_color, game_students.stu6_pos)
        win.blit(game_students.stu6_selected, game_students.stu6_rect)
        game_students.AddStudents6()
        game_player.credit -= game_students.price6
    return game_player

def selectProduction(win, game_production, mx, my, game_player):
    if mx > 900 and mx < 980 and my < 120 and game_production.git_upgradable == True:
        game_production.git_nb_prod += 1
        game_player.credit -= 1
    if mx > 900 and mx < 980 and my > 120 and my < 250 and game_production.git_upgradable == True:
        game_production.boy_nb_prod += 1
        game_player.credit -= 2
    if mx > 900 and mx < 980 and my > 250 and my < 380 and game_production.git_upgradable == True:
        game_production.aztec_nb_prod += 1
        game_player.credit -= 3
    if mx > 900 and mx < 980 and my > 380 and my < 510 and game_production.git_upgradable == True:
        game_production.koala_nb_prod += 1
        game_player.credit -= 4
    if mx > 900 and mx < 980 and my > 510 and my < 640 and game_production.git_upgradable == True:
        game_production.monster_nb_prod += 1
        game_player.credit -= 5
    if mx > 900 and mx < 980 and my > 640 and my < 770 and game_production.git_upgradable == True:
        game_production.gourou_nb_prod += 1
        game_player.credit -= 6
    return game_production
