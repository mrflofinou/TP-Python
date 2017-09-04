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

def choix_lettre():
    """
    Cette fonction permet de récupérer la lettre choisie par le joueur
    """
    entree = input("\nTapez une lettre: ")
    entree = entree.lower()
    if len(entree)>1 or not entree.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return choix_lettre()
    else:
        return entree

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
