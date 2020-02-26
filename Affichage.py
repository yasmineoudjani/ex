import pygame
from pygame.locals import *
from constantes import *
class Affichage:
    def __init__(self):
        pygame.init()

        #Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
        self.fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
        #Icone
        self.icone = pygame.image.load(image_icone)
        pygame.display.set_icon(self.icone)
        #Titre
        pygame.display.set_caption(titre_fenetre)

    def chargement(self, niveau, robot):

        self.robot = robot
        self.niveau= niveau
        #Chargement et affichage de l'écran d'accueil
        self.accueil = pygame.image.load(image_fond).convert()
        self.fenetre.blit(self.accueil, (0,0))
    	#Rafraichissement
        pygame.display.flip()
        self.fond = pygame.image.load(image_fond).convert()

        self.fenetre.blit(self.fond, (0,0))
        niveau.afficher(self.fenetre)
        self.fenetre.blit(self.robot.direction, (self.robot.case_x, self.robot.case_y))
        pygame.display.flip()

    def refresh(self, robot):
        self.robot = robot
        self.fenetre.blit(self.fond, (0,0))
        self.niveau.afficher(self.fenetre)
        self.fenetre.blit(self.robot.direction, (self.robot.case_x, self.robot.case_y)) #self.robot.direction = l'image dans la bonne direction
        pygame.display.flip()
