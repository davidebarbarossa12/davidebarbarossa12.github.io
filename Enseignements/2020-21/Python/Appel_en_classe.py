#!/usr/bin/python3
# coding: utf-8

# --------------- CE SCRIPT FAIT L'APPEL! --------------------

# ------------ Fonctions --------------


def faire_appel(ÉTUD,RÉP): # on fait l'appel des élèves dans la liste ÉTUD et on mémorise les réponses dans la liste RÉP

	print("\nOn fait l'appel!\n")
	for LIGNE in range(len(ÉTUD)):  # "len" est une fonction de base de python3 qui calcule la longueur d'une liste
	                     
  		print(ÉTUD[LIGNE],", présent?") # lire le nom
  		RÉP_DONNÉE = input("(écrire 'oui' ou 'non') ") # écouter la réponse
  		
  		if(RÉP_DONNÉE == "oui"):
  			RÉP[LIGNE] = True # cocher présent
  		else:
  			RÉP[LIGNE] = False # cocher absent

	return RÉP # On retourne la liste des réponses mis à jour suite à l'appel

#----

def cherche_dans_liste(ÉTUD, RÉP, BOOL): # Cette fonction suppose que RÉP soit une liste de booléens (True/False)
                                      # et BOOL soit un booléen (True/False). ÉTUD peut être n'importe quelle liste.
                                      # La fonction renvoie une liste LISTE_CHERCHÉE qui contient que les étudiants 
                                      # qui sont tels que leurs éléments corréspondants dans RÉP valent BOOL.
                                      # C.à.d. les présent si Bool == True, les absent sinon.

	LISTE_CHERCHÉE = [] # on initialise la liste cherchée à la liste vide ("[]") 
	
	for LIGNE in range(len(ÉTUD)): 
		if ( RÉP[LIGNE] == BOOL): # si à la ligne LIGNE on a la réponse cherchée (c.à.d. Bool), alors
			LISTE_CHERCHÉE = LISTE_CHERCHÉE + [ ÉTUD[LIGNE] ] # on ajoute l'élément corréspondant à la LISTE_CHERCHÉE.
                            # Remarquez qu'on a utilisé le "+" sur les listes, c.à.d. la concatenation de listes.
	return LISTE_CHERCHÉE  

#---

def affiche_liste(LISTE): 
	for élément in LISTE: print(élément) # on print chaque élément de la liste


# -------- "Vrai" début de l'execution ------------


ÉTUDIANTS = ["Bobo", "Coco", "Lolo", "Mimi", "Toto", "Zaza"] # liste des étudiants en classe
RÉPONSES = [False,  False,  False,  False,  False,  False ] # liste des réponses: avant de l'appel personne est là

RÉPONSES = faire_appel(ÉTUDIANTS , RÉPONSES) # on fait l'appel et on met à jour la liste des réponses

PRÉSENTS = cherche_dans_liste(ÉTUDIANTS, RÉPONSES, True) # on calcule les présents
print("\nPrésents:\n")
affiche_liste(PRÉSENTS) # on affiche les présents

ABSENTS = cherche_dans_liste(ÉTUDIANTS, RÉPONSES, False) # on calcule les absents
print("\nAbsents:\n")
affiche_liste(ABSENTS) # on affiche les absents

#--- FIN
