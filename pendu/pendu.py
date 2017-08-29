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
mot_trouve = fonctions.recherche_mot(mot_hasard, compteur)
fonctions.affichage_resultat(mot_hasard, mot_trouve)
