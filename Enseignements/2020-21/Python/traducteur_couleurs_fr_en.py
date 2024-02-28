#!/usr/bin/python3
# coding: utf-8


# ----------- FONCTIONS ----------- 


def welcome(): # on fait coucou
	print("\nCoucou, je traduis des mots du français à l'anglais et enversement!\n")

# ----

def salutations(): # on dit au revoir
	print("\nBon à la prochaine du coup, byebye! :-)\n")

# ----

def créer_dict(): # on renvoie un dictionnaire fr <-> en
                  # avec certaines tradutctions de base
	return {"blanc":"white", "noir":"black", "rouge":"red", "bleu":"blue", "jaune":"yellow", "vert":"green"}

# ----

def mettre_a_jour(D, MOT): # D est censé être un dictionnaire.
                           # Cette fonction ajoute le mot MOT avec sa traduction à D

	print("Le mot '",MOT,"' c'est quelle langue déjà?!")
	LANGUE = input("(saisis 'fr' ou 'en') ")
	
	if ( (not LANGUE == 'fr') and (not LANGUE == 'en') ):
		print("Je t'avais demandé d'écrire soit 'fr' soit 'en'!")
		print("Bon bah comme qui m'a programmé n'avait pas envie de faire une boucle while je vais juste oublier ce mot et je vais continuer comme si de ne rien était :P")
		return D
	
	TRADUCTION = input("Et c'est quoi ça traduction dans l'autre langue? ")
	
	if (LANGUE == 'fr'): D[MOT] = TRADUCTION
	elif (LANGUE == 'en'): D[TRADUCTION] = MOT
	
	return D # On retourne D mis à jour

# ----

def cherche_clef(D, MOT): # D est censé être un dictionnaire.
                          # Cette fonction retourne une chaine de caractères:
                          # la clef de D où se trouve MOT, si elle existe;
                          # la chaine vide "" sinon (c.à.d. si MOT n'est pas dans les 
                          #                                              valeurs de D)
	for clef in D:
		if ( D[clef] == MOT ): return clef

	return ""

# ----
	
def lancer_dict(D): # D est censé être un dictionnaire
		
		while(True): # ATTENTION, possible boucle infinie
		             # (faut donc bien faire le choses)!
			
			MOT = input("Mot à traduire? (saisis 'quitter' pour quitter le dictionnaire)\n")
			
			if ( MOT == "quitter" ): return # on sort de la fonction en ne rien retournant... 
			                                # c'est tout à fait possible (ça aurait été mieux
			                                # d'utiliser la commande 'break')
			                                
			else: # pas nécessaire d'écrire "else" ici (pourquoi?),
			      # mais je le mets quand même comme ça c'est plus clair
				
				if ( MOT in D ):
					print("Le mot '",MOT,"' est français et se traduit en anglais avec:")
					print(D[MOT])
					
				else:
					TRADUCTION = cherche_clef( D, MOT )
					if ( not (TRADUCTION == "") ): # voir le commentaire de la fonction 
					                               # cherche_clef
						print("Le mot '",MOT,"' est anglais et se traduit en français avec:")
						print(TRADUCTION)
			    
					else: # si on rentre dans ce 'else' c'est parce que
					      # il ne connait pas le mot dans aucune des deux langues
						print("\nDésolé je ne connais pas ce mot :(")
						D = mettre_a_jour(D, MOT)
						print("Merci pour cette mise à jour :) On reprend...\n")


# ----------- "VRAI" DÉBUT DE L'EXÉCUTION ----------- 


welcome()
lancer_dict(créer_dict())
salutations()

