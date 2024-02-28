#!/usr/bin/python3

# Avec la ligne d'avant je dis à la machine d'aller chercher l'interpréteur 'python3' pour interpreter les lignes suivantes du code

# coding: utf-8

# CE PROGRAMME DESSINE DEUX CARRÉS

# Dans tout le code, attention aux tabulations (et dans le fonctions et dans les boucles): ça fait partie de la syntaxe!

# Modules que je utiliserai --------------

from turtle import *

# Fonctions que je définis --------------

def welcome_user(): # Faire coucou à l'utilisateur
	print("Coucou!")


def draw_square(L): # Dessiner un carré de longueur L

	for i in range(4):
		forward(L)
		left(90)


def talk_to_user(QUESTION): # Interaction avec l'utilisateur: poser question + renvoyer réponse

	print("Je vais te poser une petite question: ")
	return input(QUESTION)


# C'est ici que l'interpréteur commencera l'exécution --------------

welcome_user()

L1=int(talk_to_user("Côté du premier carré = "))
L2=int(talk_to_user("Côté du deuxième carré = "))
# J'aurait pu utiliser int(input(blablabla)), mais comme ça on voit des fonctions que renvoient des valeurs

for i in range(2): # i=0,1
# Je choisis la longueur L du côté du carré
	if (i==0):
		L=L1
	else:
		L=L2
# Je le dessine
	draw_square(L)

q=input("Entrer une touche pour quitter")
