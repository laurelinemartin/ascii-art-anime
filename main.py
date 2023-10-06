import sys
from bibli import liste
from time import sleep

def lignes(art):
	ligne = 0
	for l in art:
		ligne+=1
	return ligne

def dessiner(choix):
	l = lignes(liste[choix][0])
	retour = "\033[A"*l

	for _ in range(l):
		print()

	for tour in range(10):
		art_ligne = liste[choix][tour%2]
		print(retour+"{}".format("".join(art_ligne))+"")
		sleep(0.5)


if __name__ == "__main__":
	print("Liste d\'ASCII art : ")
	for cle in liste:
		print("- {}".format(cle))
	dessin = input("Que dessiner ? ")
	dessiner(dessin)
