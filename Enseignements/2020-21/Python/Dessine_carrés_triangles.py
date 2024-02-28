#!/usr/bin/python3
# coding: utf-8

# ------- CE SCRIPT DESSINE UNE LIGNE DE CARRÉS ALTERNÉS AVEC DES TRIANGLES,
#         DU MÊME CÔTÉ (DEMANDÉ À L'UTILISATEUR) ET AVEC COULEURS DIFFÉRENTES (DEMANDÉES À L'UTILISATEUR)

# ---------- MODULES -----------

from turtle import *

# ---------- FONCTIONS (remarquez lesquelles sont des procédures et lesquelles retournent des valeurs!) -----------

def welcome_and_datas(): # On dit salut à l'utilisateur et on lui demande les donnée qu'il souhaite

	print("\n-------\nSalut!\n-------\n")
	N = int(input("Longueur de la ligne de carrés/triangles = "))
	L = int(input("Longueur du côté des carrés = longueur du côté des triangles = "))
	C1 = input("Couleur carrés = ")
	C2 = input("Couleur triangles = ")
	return { "length_line":N , "length_side":L , "color_squares":C1 , "color_triangles":C2 }

def byebye(): # On dit au revoir à l'utilisateur

	q=input("\nAppuyer sur n'importe quelle touche pour quitter")
	print("\n-------\nCe script et la tortue te disent: bye bye :-)\n-------\n")
	

def reset_position(): # on retourne à la position (0,0) en ne pas laissant des traces
	up()
	goto(0,0)
	down()


def draw_side_of_square(L): # dessine côté long L et se tourne de 90 degrées
	forward(L)
	left(90)
	
	
def draw_side_of_triangle(L): # dessine côté long L et se tourne de 120 degrées
	forward(L)
	left(120)


def draw_square(L,C): # dessine carré de côté L avec couleur C
	
	color(C)
	
	for i in range(4):
		draw_side_of_square(L)
		
		
def draw_triangle(L,C): # dessine triangle de côté L avec couleur C
	
	color(C)
	
	for i in range(3):
		draw_side_of_triangle(L)
		
		
# ------- "VRAI" DÉBUT DU SCRIPT --------

USER_DATAS = welcome_and_datas() # On demande les données à l'utilisateur et on les mets dans un dictionnaire qu'on appelle USER_DATAS

for i in range(USER_DATAS["length_line"]): # on dessine USER_DATAS["length_line"] figures
	
	if (i%2==0):                           # si i est pair alors on fait les carrés (donc on commence par les carrés)
		draw_square(USER_DATAS["length_side"] , USER_DATAS["color_squares"])
	else:                                  # si i est impair on fait les triangles
		draw_triangle(USER_DATAS["length_side"] , USER_DATAS["color_triangles"])
	
	forward(USER_DATAS["length_side"])     # on se déplace pour être prèts à dessiner une nouvelle figure
		
reset_position()                           # on retourne à la position (0,0) (qui est la position initiale)
		
byebye()












