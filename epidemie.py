from affichage import *
from creation_config import *
from mise_a_jour import *
from import_export import *


def boucle_finale():
    """
    Sortie:
    La grille avec un nombre de tours donné et des statistiques liées aux changements
    """
    tours = int(input("Combien voulez vous faire de tours ? "))
    if input("Voulez vous récupérer la grille de la dernière partie ? Y ou N") == "Y":
        G = imp() # Si l'utilisateur le souhaite, la grille utilisée sera celle de la dernière éxécution
        if not G:
            print("Il n'y a pas de précédente sauvegarde, nous allons donc générer une grille:")
            G = generer()
    else:
        G = generer()
    afficher(G)
    cpt = 0
    print("Veuillez appuyer sur n'importe quelle touche pour continuer la simulation et S pour l'arreter au prochain tour")
    while cpt < tours:  # La boucle tant que permet d'arreter la boucle si l'utilisateur a envie
        cont = input()
        if cont == "S":
            cpt = tours  # Si l'utilisateur a envie d'arreter le code, cpt sera egal a tours, ce qui fera arreter la
            # boucle
        stats1 = statistiques(G)  # On enregistre les statistiques de la grille
        G = transition(G)
        afficher(G)
        stats2 = statistiques(G)  # On enregistre les statistiques de la grille suivante
        print(stats2)  # On affiche les statistiques de la dernière grille
        print(evolution(stats2, stats1, cpt))  # On affichage la différence entre la grille précédente et la nouvelle
        cpt += 1  # On ajoute 1 au compteur pour simuler le nombre de jours
    exp(G)


boucle_finale()



