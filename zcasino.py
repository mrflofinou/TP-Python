#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################
#
# Coder un jeu de roulette simplifié
#
#####################################

# Règles du jeu:
#
# 1)
# Le jouer mise sur un chiffre compris entre 0 et 49
# En choisissant son numéro il y dépose la somme qu'il souhaite miser
#
# 2)
# Les numéros pairs sont noirs et les niméros impairs sont rouge
# Le numéro est tiré au hasard et si il correspond au numéro misé on gangne. On remporte 3xnotre miser
# Si le numéro tiré au hasard n'est pas le bon, mais que le numéro misé est de la même couleur que le numéro sorti: On remporte la moitié de notre mise
# Si notre numéro n'est pas sortit et qu'il n'a pas la même couler que le numéro sorti : on perd

import random
import math

# Demander au joueur d'indiquer combien il a d'argent
wallet = input("\nCombien avez-vous d'argent dans votre porte monnaie ?: ")
wallet = float(wallet)
continue_game = True

while continue_game == True:

    number = -1
    while number<0 or number>49:    # boucle de vérification de la saisie des valeurs
        # Demander au joeur le numéro (entre 0 et 49) sur lequel il veut miser
        number = input("\nChoisissez un nombre entre 0 et 49: ")
        try:
            number = int(number)
        except ValueError:
            print("Vous n'avez pas saisie de nombre entier")
            number = -1
            continue
        if number<0:
            print("Le chiffre que vous avez tapez est négatif")
        if number>49:
            print("Le chiffre que vous avez tapez est supérieur à 49")

    mise = 0
    while mise <= 0 or mise > wallet:    # boucle de vérification de la saisie des valeurs
        # Demander au joueur de miser (faire une condition comparant la somme misée à son porte monnaie)
        mise = input("\nCombien voullez-vous miser ?: ")
        try:
            mise = float(mise)
        except ValueError:
            print("Vous n'avez pas saisie de nombre")
            mise = 0
            continue
        if mise<=0:
            print("Tu ne peux pas miser de des valeurs négatives")
        if mise>wallet:
            print("Me prend pas pour un jambon !")
    wallet -= mise

    number_win = random.randrange(50)
    print("\nVoici le numéro gagnant !\n")
    print("====",number_win,"====\n")

    # On utilise le modulo de 2 pour savoir si un nombre est pair ou non. En effet si un nombre est pair sont modulo sera 0 alors que si il est impar son modulo sera 1
    #modulo_number_win = number_win % 2
    #modulo_number = number % 2

    if number_win == number:
        price = mise + 3*mise
        wallet += price
        print("TU AS GANE LE JACKPOT !!! \n")
        print("Tu as gagné la somme de", price,"$\n")
        print("Tu as maintenant", wallet,"$ dans ton porte-monnaie")
    elif number_win%2 == number%2:                                          # On compare les modulo pour savoir si les deux numéros sont de la même parité
        price = math.ceil(mise + math.ceil(mise/2))
        wallet += price
        print("Tu n'as pas gagné le Jackpot mais dit merci à la couleur",color,"!!! \n")
        print("Tu as gagné la somme de", price,"$\n")
        print("Tu as maintenant", wallet,"$ dans ton porte-monnaie")
    else:
        print("Vraiment pas de bol !\n")
        print("Tu as maintenant", wallet,"$ dans ton porte-monnaie")

    if wallet <= 0:
        print("\nVous êtes complétement ruiné ! Vous devez partir maintenant")
        continue_game = False
    else:
        end = input("\nVoulez-vous devenir riche en refaisant une partie ?(o/n) ")
        if end == "n" or end == "N":
            print("\nA bientôt !")
            continue_game = False
