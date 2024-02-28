#!/usr/bin/python3
# coding: utf-8

# ------- SOLUTION TP3 EXO 1, MAIS SENS LA DERNIÈRE QUESTIONS
#         (CELLE DU SAPIN DE NÖEL, QUE JE VOUS LAISSE FAIRE PAR VOUS MÊMES) --------

# --------------------- Fonctions -----------------------------

def affiche_blancs_puis_etoiles(B,E): # on l'a vue ensemble en TP
	print(" "*B+"*"*E)
	
# Même si le corps de cette fonction (qui est une procédure!) consiste juste en un "print", maintenant que l'on dispose de cette fonction on a "fait ABSTRACTION DE L'IMPLEMENTATION de l'affichage des espaces et des étoiles": c'est bien, ça nous plait! En fait tout ce qui nous intéresse c'est de savoir qu'on PEUT faire cet affichage, mais pas COMMENT on a décidé de le faire réellement.


def dessine_rectangle_etoiles_avec_transposition(HAUT,LARG): # on fait aussi un contrôle pour que l'utilisateur
                                                             # écrit bien ce qu'il veut, juste pour compliquer un peu

	FLAG_pas_compris=True # varaible booléenne (on dit que c'est un "drapeau"): si True alors on n'as pas compris ce que l'utilisateur a dit, si False alors on a compris
	while(FLAG_pas_compris):
	
		TRANSPOSER = input("Veux-tu transposer le rectangle? (écris 0 pour 'non' et 1 pour 'oui') ")
		FLAG_pas_compris = False # normalement là on a compris
		
		if (TRANSPOSER=="0"):
		
			for i in range(HAUT): # on fait un rectangle en pas transposé
				affiche_blancs_puis_etoiles(0,LARG) 
				
		elif (TRANSPOSER=="1"):
		
			for i in range(LARG): # on fait un rectangle en transposé
				affiche_blancs_puis_etoiles(0,HAUT) 
				
		else: # si on rentre dans ce bloc "else" c'est que l'utilisateur a écrit n'importe quoi (c.à.d. ni "0" ni "1"). On lui communique qu'on n'a pas compris et on change le drapeau à "je n'ai pas compris" (c.à.d. True)
		
			print("Je ne comprends pas ce que tu racontes:")
			FLAG_pas_compris = True # Comme ça on rentre dans la boucle while à nouveau

# ---- Pour les prochaines fonctions, essayez d'abord de les faire par vous mêmes
#      et après regardez si vous avez fait comme moi! (Faut réflechir un moment)  ----

def dessine_triangle_etoiles_gauche(HAUT):
	for i in range(HAUT):
		affiche_blancs_puis_etoiles(0,i+1)
		
		
def dessine_triangle_etoiles_gauche_envers(HAUT):
	for i in range(HAUT):
		affiche_blancs_puis_etoiles(0,HAUT-i)


def dessine_triangle_etoiles_droit_envers(HAUT):

	for i in range(HAUT):
		affiche_blancs_puis_etoiles(i,HAUT-i)
		
		
def dessine_triangle_etoiles_droit(HAUT):

	for i in range(HAUT):
		affiche_blancs_puis_etoiles(HAUT-i-1,i+1)

		
def dessine_triangle_isocele(HAUT):

	for i in range(HAUT):
		affiche_blancs_puis_etoiles(HAUT-i-1,2*i+1)
#      parce que en deuxième arguement c'est i+1+i


def dessine_triangle_isocele_envers(HAUT):

	for i in range(1,HAUT+1):
		affiche_blancs_puis_etoiles(i-1,2*HAUT-2*i+1)
#             parce que c'est (HAUT-(HAUT-i)-1,2*(HAUT-i)+1)
#         (c.à.d. comme pour isocele mais avec HAUT-i au lieu de i)


# ------ "Vrai" début du programme --------

dessine_rectangle_etoiles_avec_transposition(int(input("Hauteur rectangle? ")),int(input("Largeur rectangle? ")))

dessine_triangle_etoiles_droit(int(input("Hauteur triangle angle à droit? ")))
	
dessine_triangle_etoiles_droit_envers(int(input("Hauteur triangle angle à droite et à l'envers? ")))

dessine_triangle_etoiles_gauche_envers(int(input("Hauteur triangle angle à gauche et à l'envers? ")))

dessine_triangle_etoiles_gauche(int(input("Hauteur triangle angle à gauche? ")))

dessine_triangle_isocele(int(input("Hauteur triangle insocele? ")))

dessine_triangle_isocele_envers(int(input("Hauteur triangle insocele à l'envers? ")))
	
	
	
