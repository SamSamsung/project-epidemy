from parametres import *


def afficher(G, long=LONG, haut=HAUT):
    """
    Entrée:
    La grille, la taille et la hauteur
    Sortie:
    Un affichage visible et compréhensible de la grille
    """
    for i in range(long):
        for j in range(haut):  # On accède aux éléments de la liste grace aux deux boucles
            # On affiche un rond, coloré en fonction de leur état
            if G[i][j]["etat"] == "saine":
                if G[i][j]["valeur"] == 0:
                    print("\033[4m●\033[0m", end="  ")
                else:
                    print("●", end="  ")
            elif G[i][j]["etat"] == "contaminee":
                if G[i][j]["valeur"] == 0:
                    print("\033[4m\033[31m●\033[0m", end="  ")  # Le changement d'état chez la cellule se vera car
                    # elle sera soulignée
                else:
                    print("\033[1m\033[31m●\033[0m", end="  ")
            elif G[i][j]["etat"] == "immunisee":
                if G[i][j]["valeur"] == 0:
                    print("\033[4m\033[36m●\033[0m", end="  ")
                else:
                    print("\033[1m\033[36m●\033[0m", end="  ")
            elif G[i][j]["etat"] == "decedee":
                if G[i][j]["valeur"] == 0:
                    print("\033[4m\033[30m●\033[0m", end="  ")
                else:
                    print("\033[1m\033[30m●\033[0m", end="  ")
        print()
    print()
