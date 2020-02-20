import pygame
from pygame.locals import *
from constantes import *
from Arene import *

class Capteur:
    def __init__(self, niveau):
        self.niveau = niveau

    """retourne le nombre de case avant un obstacle a droite"""
    def murD(self, case_x , case_y):
        i=1
        while self.niveau.structure[case_y][case_x+i] != '1':
            i=i+1
        return i

    """retourne le nombre de case avant un obstacle a gauche"""
    def murG(self, case_x , case_y):
        i=1
        while self.niveau.structure[case_y][case_x-i] != '1':
            i=i+1
        return i

    """retourne le nombre de case avant un obstacle en haut"""
    def murA(self, case_x , case_y):
        i=1
        while self.niveau.structure[case_y-i][case_x] != '1':
            i=i+1
        return i

    """retourne le nombre de case avant un obstacle en bas"""
    def murR(self, case_x , case_y):
        i=1
        while self.niveau.structure[case_y+i][case_x] != '1':
            i=i+1
        return i
