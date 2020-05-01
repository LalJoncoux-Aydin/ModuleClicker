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
        self.pos = (130,180,500,500)
        self.img = pygame.image.load("module.jpg").convert_alpha()

class InfoBar:
    def __init__(self):
        self.color = violet
        self.pos = (0,0,1500,100)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('Credits : ', True, green, violet)
        self.textRect = self.text.get_rect()
        self.textRect.center = (600, 50)

class Students:
    def __init__(self):
        self.color = darkblue
        self.pos = (800,100,800,800)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('Githubber', True, green, darkblue)
        self.textRect = self.text.get_rect()
        self.textRect.center = (1000, 200)
