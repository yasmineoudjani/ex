#!/usr/bin/python3
# -*- coding: Utf-8 -*


import pygame
from pygame.locals import *

from Robot import *
from Arene import *
from constantes import *


choix='terrain2'
niveau = Arene(choix)
niveau.generer()
affichage=Affichage()
robot= Robot("images/dk_droite.png", "images/dk_gauche.png","images/dk_haut.png", "images/dk_bas.png", niveau)

affichage.chargement(niveau,robot)
while True:
	#Limitation de vitesse de la boucle
	pygame.time.Clock().tick(30)
	robot.autonome(affichage)
	affichage.refresh(robot)
