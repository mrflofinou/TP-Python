def mot_hasard(nbr_hasard, liste_mots):
    """
    Cette fonction à pour but de déterminer un mot au hasard dans une liste de mots prédéfinie.
    Un nombre tiré au hasard nous servira d'indice pour récupérer un mot dans la liste.
    Cependant le mot dans la liste est une chaîne de caractère, nous le transformons en liste
    afin de pouvoir faire des comparaison avec d'autres listes
    Cette fonction renvoie le mot au hasard à deviner sous forme de liste
    """
    for i, mot in enumerate(liste_mots):
        if i==nbr_hasard:
            mot_hasard = mot
    mot_hasard = list(mot_hasard)         # transforme la chaine de caractère en liste afin de pouvoir faire des comparaison avec la liste mot_trouve
    return mot_hasard

def recherche_mot(mot_hasard, compteur):
    """
    Cette fonction sert à chercher le mot.
    On créé une liste qui sera le mot trouvé. Cette liste sera comparé au mot au hasard
    Cette liste sera aussi remplie des lettre trouvées au fur et à mesure de la partie
    La fonction renvoie le mot trouvé sous forme de liste
    """

    mot_trouve = []                       # On initialise la variable mot_trouve comme une liste
    entree = str()

    for lettre in mot_hasard:
        mot_trouve.append("*")            # On rempli la liste mot_trouve par des étoiles pour l'affichage
    affichage = "".join(mot_trouve)       # Afin que l'affichage soit propre on affiche une chaine de caractère
    print("Le mot recherché contient {} lettres:\n{}".format(len(mot_hasard), affichage.center(30)))

    while mot_trouve != mot_hasard:           # Tant que les deux liste ne sont pas égale c'est qu'on a pas trouvé le mot, alors on continue
        entree = input("\nTapez une lettre: ")
        entree = entree.lower()
        for i, lettre in enumerate(mot_hasard):
            if entree == lettre:
                mot_trouve[i] = mot_hasard[i]   # Si la lettre entrée correspond à une lettre du mot alors elle est enregistrée dans le tableau mot_trouve
        affichage = "".join(mot_trouve)         # Cette affichage permet de montrer uniquement les lettres trouvées dans le mot
        print ("\n",affichage.center(30))
        compteur-= 1                            # Le compteur permet permet de compter le nombre de tentatives restantes
        if compteur == 0:                       # Si le compteur est à 0 c'est qu'on épuisé toutes nos tetative
            break                               # Du coup on casse la boucle
        else:                                   # Sinon on affiche le nombre de tentatives restantes
            print("\nil te reste encore {} essais".format(compteur))
    return mot_trouve

def affichage_resultat(mot_hasard, mot_trouve):
    """
    Cette fonction à pour but d'afficher le résultat
    Elle compare si le mot renvoyé par la fonction "recherche_mot" correspond au mot choisi au hasard
    renvoyé par la fonction "mot_hasard" et affiche un texte en fonction des cas
    """
    
    if mot_trouve == mot_hasard:
        print("\nBravo ! tu as trouvé le mot '{}'".format("".join(mot_hasard)))
    else:
        print("\nTu as épuisé toutes tes tentatives, tu as perdu !!!")
        print("Le mot à trouver était '{}'".format("".join(mot_hasard)))
