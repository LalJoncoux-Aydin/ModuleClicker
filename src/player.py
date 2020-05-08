#!/usr/bin/env python3
import pygame, sys, time
from pygame.locals import *

class Player:
    credit = 0

    def spendCredit(self, to_spend):
        self.credit -= to_spend

    def addCredit(self, to_add):
        self.credit += to_add
