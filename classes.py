"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *

class Arene:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
	
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau
	
	
	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		mur = pygame.image.load(image_mur).convert()
		#depart = pygame.image.load(image_depart).convert()
		#arrivee = pygame.image.load(image_arrivee).convert_alpha()
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == '1':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == 'd':		   #d = Départ
					fenetre.blit(depart, (x,y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee, (x,y))
				num_case += 1
			num_ligne += 1
			
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

	def isMurD(self):
		if self.niveau.structure[self.case_y][self.case_x+1] != '1':
			return True
		return False
	
	def isMurG(self):
		if self.niveau.structure[self.case_y][self.case_x-1] != '1':
			return True
		return False
	def isMurA(self):
		if self.niveau.structure[self.case_y-1][self.case_x] != '1':
			return True
		return False
	def isMurR(self):
		if self.niveau.structure[self.case_y+1][self.case_x] != '1':
			return True
		return False	

	def avancer(self):
		if self.case_y > 0:
			if self.niveau.structure[self.case_y-1][self.case_x] != '1':
				self.case_y -= 1
				self.y = self.case_y * taille_sprite
		self.direction = self.haut
        
        
	def reculer(self):
		if self.case_y < (nombre_sprite_cote - 1):
		    if self.niveau.structure[self.case_y+1][self.case_x] != '1':
		        self.case_y += 1
		        self.y = self.case_y * taille_sprite
		self.direction = self.bas


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
