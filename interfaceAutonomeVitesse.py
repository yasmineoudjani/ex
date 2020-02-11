#!/usr/bin/python3
# -*- coding: Utf-8 -*

import random 
import time
import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)

#BOUCLE PRINCIPALE
continuer = 1
menu = 1
while menu==1:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			#Si l'utilisateur presse Echap ici, on revient seulement au menu
			if event.key == K_a:
				vitesse = 1
				menu=0
			elif event.key == K_z:
				vitesse = 0.5
				menu=0
			elif event.key == K_e:
				vitesse = 0.2
				menu=0	
while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_fond).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	
	choix='terrain2'
	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Arene(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création de Donkey Kong
		dk = Robot("images/dk_droite.png", "images/dk_gauche.png", 
		"images/dk_haut.png", "images/dk_bas.png", niveau)
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
		pygame.display.flip()		
	#BOUCLE DE JEU
	while continuer_jeu:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
		
		chiffre=random.randint(0, 3)
		if chiffre==0:
			while dk.isMurD():
				dk.tourner(0)
				dk.gestionVitesse()
				fenetre.blit(fond, (0,0))
				niveau.afficher(fenetre)
				fenetre.blit(dk.direction, (dk.x, dk.y)) 
				pygame.display.flip()
				time.sleep(vitesse)
		if chiffre==1:
			while dk.isMurG():
				dk.tourner(1)
				dk.gestionVitesse()
				fenetre.blit(fond, (0,0))
				niveau.afficher(fenetre)
				fenetre.blit(dk.direction, (dk.x, dk.y)) 
				pygame.display.flip()
				time.sleep(vitesse)
		if chiffre==2:
			while dk.isMurA():
				dk.avancer()
				dk.gestionVitesse()
				fenetre.blit(fond, (0,0))
				niveau.afficher(fenetre)
				fenetre.blit(dk.direction, (dk.x, dk.y)) 
				pygame.display.flip()
				time.sleep(vitesse)
		if chiffre==3:
			while dk.isMurR():
				dk.reculer()
				dk.gestionVitesse()
				fenetre.blit(fond, (0,0))
				niveau.afficher(fenetre)
				fenetre.blit(dk.direction, (dk.x, dk.y)) 
				pygame.display.flip()
				time.sleep(vitesse)
		
		
			
		#Affichages aux nouvelles positions
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
		pygame.display.flip()

		"""#Victoire -> Retour à l'accueil
		if niveau.structure[dk.case_y][dk.case_x] == 'a':
			continuer_jeu = 0"""
