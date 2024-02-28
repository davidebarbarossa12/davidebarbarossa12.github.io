#!/usr/bin/python3
# coding: utf-8

#------- CE PROGRAMME DEMANDE UNE EQUATION DE SECOND DEGRÉ ET DONNE SES SOLUTIONS ---------

# ----------------- MODULES -----------------------


from math import sqrt # On importe que la fonction qui s'appelle "sqrt" du module qui s'appelle "math"
                      # Évidemment il s'agit de la fonction "racine carrée" (SQare RooT en anglais)

# ----------------- FONCTIONS -----------------------


def insert_equation():  # on laisse l'utilisateur saisir l'équation

	negative = True
	while (negative): #  écrire juste "negative" est la même chose qu'écrire "negative == True"	
				      #  cette boucle sert pour s'assurer que "a" soit non nul		
		a = float(input("(a doit être non nul)\na= "))
		if (a != 0): negative = False # "!=" est la négation de "=="

	b = float(input("b = "))
	c = float(input("c = "))

	return [a,b,c]   # On retourne la liste des coefficients de l'équation que l'utilisateur a saisit


def print_eq(eq): # L'argument "eq" est censé être une liste de trois float
	print("L'équation que t'as saisis est:\n\n(%f)*x^2 + (%f)*x + (%f) = 0\n" %( eq[0] , eq[1] , eq[2] ) )
	

def print_sol(sol): # L'argument "sol" est censé être une liste de zero (la liste vide "[]"), un ou deux float
	
	number_sol = len(sol) 
	
	if( number_sol == 0 ):
		print("L'équation n'admet pas de solutions réelles")
		print("(mais tu peux toujours chercher les solutions complexes...)")
		
	else:
		if( number_sol == 1):
			print("L'équation admet un'unique solution, qui est:")	
	
		elif( number_sol == 2 ):
			print("L'équation admet deux solution distinctes, qui sont:")
	
		for i in range(number_sol):
			print("x%d = %f" %(i+1,sol[i]) )


def compute_sol(eq):                       # L'argument "eq" est censé être une list de trois float
					                       # On retournera les solutions de l'équation eq organisées en une liste	
					                       # (On sait comment résoudre une telle équation! Lire ligne 92 pour plus d'info)
	
	Delta = eq[1]**2 - 4*eq[0]*eq[2]       # Le discriminant Delta de l'équation est b^2-4ac
	
	if( Delta > 0 ):                       # Dans ce cas on a deux solutions distinctes,
	                                       # qui sont (-b+sqrt(Delta))/(2a) et (-b-sqrt(Delta))/(2a)
	    return [ (-eq[1]+sqrt(Delta))/(2*eq[0]) , (-eq[1]-sqrt(Delta))/(2*eq[0]) ] # et on les met dans une liste
	                
	elif( Delta == 0 ):                    # Dans ce cas on a exactement une solution,
		return [ -eq[1]/(2*eq[0]) ]        # qui est -b/(2a) et on le met dans une liste
	
	else:                                  # On est dans le "else" si et seulement si Delta < 0.
	                                       # Dans ce cas, l'équation n'a pas de solutions,
		return []                          # donc on retourne une liste vide
	                
	
# ------------- "VRAI" DEBUT DU PROGRAMME -------------------


print("""\nJe résous les équations du 2ème degré, écrites dans la forme:
a*x^2 + b*x + c = 0 (avec a != 0)\n
Saisis l'équation:\n""")

EQUATION = insert_equation()
print_eq( EQUATION )
print_sol( compute_sol( EQUATION ) ) # on fait ici une COMPOSITION de fonctions: print_sol est appelée sur 
                                     # le RÉSULTAT (l'output) de la fonction compute_sol appelée sur l'input EQUATION

#-------------------

# Est-ce que le code est organisé logiquement en faisant abstraction à travers des fonctions? Oui!
# Est-ce que dans le "vrai" corps du programme il n'y a pas trop d'operation complexes,
# mais plutôt des appels à des fonctions? Oui!
# Est-ce que le code est commenté? Oui (même trop)!
# Niquel alors!

#-------------------

# Vous connaissaiez bien, depuis l'école, la formule qui résout une équation du second degré.
# Si vous ne vous la rappellez pas, wikipedia a toute les informations:
# https://fr.wikipedia.org/wiki/%C3%89quation_du_second_degr%C3%A9#Discriminant



