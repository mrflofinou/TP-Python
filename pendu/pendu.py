#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import donnees
import fonctions
#import scores

################
#
# Jeu du pendu
#
################

# En début de parti le joueur entre son nom afin de pouvoir enregistrer son score (dans un fichier)
# Calcul des scores:
# On prend le score courant (0 si c'est la première fois que e joueur joue) et à chaque partie, on lui ajoute le nombre de point équivalent au nombre d'éssais restant.

liste_mots = donnees.liste_mot
compteur = donnees.nombre_chances                           # nombre de tentatives autorisées
nbr_hasard = random.randrange(len(donnees.liste_mot))
mot_hasard = fonctions.mot_hasard(nbr_hasard, liste_mots)

mot_trouve = []                       # On initialise la variable mot_trouve comme une liste
entree = str()                        # On initialise la variable entree comme une chaine de caractères.
for lettre in mot_hasard:
    mot_trouve.append("*")            # On rempli la liste mot_trouve avec des étoiles pour l'affichage
affichage = "".join(mot_trouve)       # Afin que l'affichage soit propre on affiche une chaine de caractère
print("Le mot recherché contient {} lettres:\n{}".format(len(mot_hasard), affichage.center(30)))

while mot_trouve != mot_hasard:           # Tant que les deux liste ne sont pas égale c'est qu'on a pas trouvé le mot, alors on continue
    entree = fonctions.choix_lettre()
    for i, lettre in enumerate(mot_hasard):
        if entree == lettre:
            mot_trouve[i] = mot_hasard[i]   # Si la lettre entrée correspond à une lettre du mot alors elle est enregistrée dans le tableau mot_trouve
    affichage = "".join(mot_trouve)         # Cette affichage permet de montrer uniquement les lettres trouvées dans le mot
    print ("\n",affichage.center(30))

    if entree in mot_hasard:                # Si la lettre est dans le mot alors le compteur ne change pas
        compteur = compteur
    else:
        compteur-= 1                        # Le compteur permet permet de compter le nombre de tentatives restantes

    if compteur == 0:                       # Si le compteur est à 0 c'est qu'on épuisé toutes nos tetative
        break                               # Du coup on casse la boucle
    else:                                   # Sinon on affiche le nombre de tentatives restantes
        print("\nil te reste encore {} essais".format(compteur))

fonctions.affichage_resultat(mot_hasard, mot_trouve)
