import pygame
from pygame.locals import *
from constantes import *
from Affichage import *
from Capteur import *
import random
import time
class Robot:
    """Classe permettant de créer un Robot"""
    def __init__(self, droite, gauche, haut, bas, niveau):
        #Sprites du personnage
        self.droite = pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        #Position du personnage en cases et en pixels
        self.case_x = 210
        self.case_y = 240
        self.angle = 0
        #Direction par défaut
        self.vitesse = 30
        self.direction = self.bas
        #Niveau dans lequel le personnage se trouve
        self.niveau = niveau
        self.capteur= Capteur(self.niveau)

    def autonome(self, affichage):
        self.affichage = affichage
        chiffre=random.randint(0, 3)
        if chiffre==0:
            while self.capteur.murD(self.case_x, self.case_y) >30:
                self.tourner(0)
                self.affichage.refresh(self)
                time.sleep(0.5)
        if chiffre==1:
            while self.capteur.murG(self.case_x, self.case_y)>30:
                self.tourner(1)
                self.affichage.refresh(self)
                time.sleep(0.5)
        if chiffre==2:
            while self.capteur.murA(self.case_x, self.case_y)>30:
                self.avancer()
                self.affichage.refresh(self)
                time.sleep(0.5)
        if chiffre==3:
            while self.capteur.murR(self.case_x, self.case_y)>30:
                self.reculer()
                self.affichage.refresh(self)
                time.sleep(0.5)


    def reculer(self):
        if self.niveau.pixel[self.case_y+30][self.case_x] != '1':
            self.case_y += 1*self.vitesse
            self.direction = self.bas

    def avancer(self):
        if self.niveau.pixel[self.case_y-30][self.case_x] != '1':
            self.case_y -= 1*self.vitesse
            self.direction = self.haut

    def tourner(self,s):

        if(s==0):
            if self.niveau.pixel[self.case_y][self.case_x+30] != '1':
                #Déplacement d'une case
                self.case_x += 1*self.vitesse
                #Image dans la bonne direction
                self.direction = self.droite

        if(s==1):
            if self.niveau.pixel[self.case_y][self.case_x-30] != '1':
                self.case_x -= 1*self.vitesse
                self.direction = self.gauche


    def gestionVitesse(self,v):
        #max = 30
        self.vitesse = v
