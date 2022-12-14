from parametres import *


def voisines_contam(G, n, m):
    """
    Entrée:
    La grille et la position de la cellule
    Sortie:
    Le nombre de cellules contaminées autour d'elles
    """
    nbs_voisines_contam = 0
    for i in range(n - 1, n + 2):
        for j in range(m - 1, m + 2):
            if i != n or j != m:  # On ne prend pas en compte la cellule principale
                if 0 <= i <= len(G) - 1 and 0 <= j <= len(G[i]) - 1:
                    if G[i][j]["etat"] == "contaminee":  # On regarde si les cellules autour sont contaminées
                        nbs_voisines_contam += 1
    return nbs_voisines_contam # On retourne le nb de cellules contaminées


def transition(G, p_infect=P_INFECT, nbs_j_guer=NBS_J_GUER, tx_mort=TX_MORT, nbs_j_imm=NBS_J_IMM):
    """
    Entrée:
    La grille, la probabilitée d'infection, le nombre de jours nécessaires à la guérison, le taux de mortalité, le nombre
    de jours nécessaires à l'immunisation
    Sortie:
    Une nouvelle grille ayant évolué avec les différents paramètres
    """
    G_next = [[{"etat": "saine", "valeur": 0} for _ in range(len(G[i]))] for i in range(len(G))]  # On creer une grille
    for i in range(len(G)):
        for j in range(len(G[i])):  # On creer deux boucles pour parcourir toute la grille
            if G[i][j]["etat"] == "contaminee":  # On regarde si la cellule est contaminée
                prob = randint(1, 100)  # On tire au sort un nombre entre 1 et 100
                if prob <= tx_mort:  # On regarde si le nombre est inférieur au taux de mortalité
                    G_next[i][j]["etat"] = "decedee"
                    G_next[i][j]["valeur"] = 0  # On détérmine donc la cellule comme morte
                elif G[i][j]["valeur"] == nbs_j_guer:  # On regarde si le nb de jours de la cellule est égale au nb de
                    # jours pour une guérision
                    G_next[i][j]["etat"] = "immunisee"  # On détérmine donc la cellule comme immunisée
                    G_next[i][j]["valeur"] = 0
                else:
                    G_next[i][j]["etat"] = "contaminee"  # Sinon on détérmine la cellule comme contaminée
                    G_next[i][j]["valeur"] = G[i][j]["valeur"] + 1  # On rajoute 1 au nb de jours

            elif G[i][j]["etat"] == "saine":  # On regarde si la cellule est saine
                contamines = voisines_contam(G, i, j)
                if contamines > 0:
                    for m in range(contamines):  # On fait une boucle pour indice le nb de cellules contaminées autour
                        nbs = randint(1, 100) # Cela permet d'augmenter la proba d'infection
                        if nbs <= p_infect:
                            G_next[i][j]["etat"] = "contaminee"
                            G_next[i][j]["valeur"] = 0
                        else:
                            G_next[i][j]["valeur"] = G[i][j]["valeur"] + 1
                else:
                    G_next[i][j]["valeur"] = G[i][j]["valeur"] + 1

            elif G[i][j]["etat"] == "decedee":  # On regarde si la cellule est décédée
                G_next[i][j]["etat"] = "decedee"  # Son état ne change donc pas
                G_next[i][j]["valeur"] = G[i][j]["valeur"] + 1

            elif G[i][j]["etat"] == "immunisee":  # On regarde si la cellule est immunisée
                if G[i][j]["valeur"] == nbs_j_imm:
                    G_next[i][j]["etat"] = "saine"  # Si son nb de jour immunisés est atteint
                    G_next[i][j]["valeur"] = 0  # elle redevient saine et on réinitialise le nombre de jours
                else:
                    G_next[i][j]["etat"] = "immunisee"  # Sinon elle reste immunisée et on rajoute 1 au nombre de jours.
                    G_next[i][j]["valeur"] = G[i][j]["valeur"] + 1

    return G_next  # On retourne la nouvelle grille


def statistiques(G, saine=0, contaminee=0, immunisee=0, decedee=0):
    """
    Entrée:
    La grille et les variables qui consitituent les états de toutes les cellules.
    Sortie:
    Un dictionnaire contenant toutes les statistiques de la grille
    """
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j]["etat"] == "saine":
                saine += 1  # Si la cellule est saine, on rajoute 1 aux statistiques des cellules saines
            elif G[i][j]["etat"] == "contaminee":
                contaminee += 1  # Si la cellule est contaminée, on rajoute 1 aux statistiques des cellules contaminées
            elif G[i][j]["etat"] == "immunisee":
                immunisee += 1  # Si la cellule est immunisée, on rajoute 1 aux statistiques des cellules immunisées
            elif G[i][j]["etat"] == "decedee":
                decedee += 1  # Si la cellule est décédée, on rajoute 1 aux statistiques des cellules décédées
    return {"saine": saine, "contaminee": contaminee, "immunisee": immunisee, "decedee": decedee}


def evolution(Stats, PastStats, tour):
    """
    Entrée:
    Les statistiques de la grille, les statistiques de la grille précédente et le nombre de jours passés depuis le
    début de l'épidémie
    Sortie:
    Un dictionnaire conantenat la différence entre les statistiques de la nouvelle grille et de la grille précédente
    """
    return {"tour": tour + 1, "dif_saine": Stats["saine"] - PastStats["saine"],
            "dif_contaminee": Stats["contaminee"] - PastStats["contaminee"],
            "dif_immunisee": Stats["immunisee"] - PastStats["immunisee"],  # On soustrait le nombre des états des
            "dif_decedee": Stats["decedee"] - PastStats["decedee"]}  # nouvelles cellules avec les anciennes


