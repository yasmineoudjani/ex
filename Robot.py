import pygame
from pygame.locals import *
from constantes import *
from Affichage import *
from Capteur import *
import random
import time
class Robot:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 7
		self.case_y = 8
		self.x = 210
		self.y = 240

		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve
		self.niveau = niveau
		self.capteur= Capteur(self.niveau)

	def autonome(self, affichage):
		self.affichage = affichage
		chiffre=random.randint(0, 3)
		print(chiffre)
		if chiffre==0:
			while self.capteur.murD(self.case_x, self.case_y) >1:
				self.tourner(0)
				self.affichage.refresh(self)
				time.sleep(0.5)
		if chiffre==1:
			while self.capteur.murG(self.case_x, self.case_y)>1:
				self.tourner(1)
				self.affichage.refresh(self)
				time.sleep(0.5)
		if chiffre==2:
			while self.capteur.murA(self.case_x, self.case_y)>1:
				self.avancer()
				self.affichage.refresh(self)
				time.sleep(0.5)
		if chiffre==3:
			while self.capteur.murR(self.case_x, self.case_y)>1:
				self.reculer()
				self.affichage.refresh(self)
				time.sleep(0.5)


	def reculer(self):
		if self.case_y < (nombre_sprite_cote - 1):
		    if self.niveau.structure[self.case_y+1][self.case_x] != '1':
		        self.case_y += 1
		        self.y = self.case_y * taille_sprite
		self.direction = self.bas

	def avancer(self):
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != '1':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut

	def tourner(self,s):

		if(s==0):
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != '1':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite

		if(s==1):
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != '1':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche


	def gestionVitesse(self,v):
	# v est le paramètre de la vitesse. 0 , 1 ou 2.
		self.vitesse = v
