#!/usr/bin/python3
# -*- coding: Utf-8 -*


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
while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_fond).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	
	choix='terrain1'
	#on vérifie que le joueur a bien fait un choix du terrain
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un terrain à partir d'un fichier
		niveau = Arene(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création du robot
		dk = Robot("images/robot_droite.png", "images/robot_gauche.png", 
		"images/robot_haut.png", "images/robot_bas.png", niveau)

				
	#BOUCLE DE JEU
	while continuer_jeu:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
		
			elif event.type == KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == K_ESCAPE:
					continuer_jeu = 0
					
				#Touches de déplacement du robot
				elif event.key == K_RIGHT:
					dk.tourner(0)
				elif event.key == K_LEFT:
					dk.tourner(1)
				elif event.key == K_UP:
					dk.avancer()
				elif event.key == K_DOWN:
					dk.reculer()			
			
		#Affichages aux nouvelles positions
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
		pygame.display.flip()

		"""#Victoire -> Retour à l'accueil
		if niveau.structure[dk.case_y][dk.case_x] == 'a':
			continuer_jeu = 0"""
