#!/usr/bin/python3
# coding: utf-8

# Modules que j'utiliserai -------------

from turtle import *

#----------------------------------------

# Fonctions que je définis -------------

def welcome_user(): 

# Ici on met le corps de cette fonction (avec les tabulations!)
	
	print("\n---- Salut! Ce programme dessine plein de carrés ----\n")

# Fin du code de welcome_use
# On dit qu'il s'agit d'une "procedure" car elle ne retourne pas de valeurs au programme qui l'appelle.


def draw_squares(N,LENGTH,DELTA): # N, LENGTH et DELTA doivent être des entiers, sinon on aura une erreur!

# Ici on met le corps de cette fonction (avec les tabulations!)

	print("\nCoucou, là je travaille dans la procedure 'draw_squares'...\n")
	
	L=LENGTH
	for j in range(N): # On dessinne d'abord le premier carré, après le deuxième ecc
		
		draw_square(L)  # On appelle une autre fonction qui fera le boulot
		L=L+DELTA          # Comme "syntactic sugar" on peut écrire: L+=DELTA (c'est juste plus rapide, si on a la flemme...)
		
	q=input("Appuyer sur une touche quelconque pour fermer le dessin")
	print("La tortue te dit: Bye bye! :-)")
	
# Fin du code de draw_squares


def draw_square(L): # Dessiner un carré de longueur L

# Ici on met le corps de cette fonction (avec les tabulations!)

	for i in range(4):
		forward(L)
		left(90)

# On dit que le 3 fonctions précédentes SONT des "procedures" car elles NE retournent PAS de valeurs au programme qui l'appelle.
		

def talk_to_user(QUESTION): # Interaction avec l'utilisateur: poser question + renvoyer réponse

# Ici on met le corps de cette fonction (avec les tabulations!)

	return input(QUESTION)

# Cette fonction N'est PAS une "procedure", car elle RENVOIE une valeur au programme qui l'appelle (il y a le mot-clef "return")

#----------------------------------------

# "Vrai" code de mon petit programme -----------

welcome_user()

draw_squares(int(talk_to_user("Combien de carré veux-tu écrire? ")),int(talk_to_user("Longuer du premier carré? ")),int(talk_to_user("Incrementation du côté à chaque carré? ")))

print("\n---Fin du programme ---")

# FIN DU CODE -------------------------------

