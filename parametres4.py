from random import *
"""
Cette configuration prend des valeurs aléatoires en configuration
"""

r_taille = randint(50,200)
r_initial = randint(1,20)
r_p_infe = randint(1,100)
r_nbs_j_guer = randint(1,14)
r_tx_mort = randint(1,50)
r_nbs_j_imm = randint(1,21)


LONG = r_taille
HAUT = r_taille
P0 = r_initial
P_INFECT = r_p_infe
NBS_J_GUER = r_nbs_j_guer
TX_MORT = r_tx_mort
NBS_J_IMM = r_nbs_j_imm