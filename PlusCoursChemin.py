import Grille
import DessinerGrille

#ici on va utiliser de la programmation dynamique pour retrouver UN plus cours chemin de manière optimale.

#relation de récurence: le plus cours chemin pour atteindre (i, j) != (1, 1)
    # - si i = 1 : le chemin de (i-1, j) + mur_gauche
    # - si j = 1 : le chemin de (i, j-1) + mur_haut
    # - sinon : on calcule le cout minimal entre cout_haut et cout_gauche,
    #     la réponse est : le chemin correspondant + mur_correspondant


n, m = 3, 4
G = Grille.creer_grille(n, m)


def minimum(dico):
    m=float('inf')
    for k in dico:
        if dico[k] < m:
            m=dico[k]
            i=k
    return i

def dijkstra_pred(G,s):
    D={} 
    d={k: float('inf') for k in G} 
    d[s]=0 
    P={}
    while len(d)>0: 
        k=minimum(d) 
        for mur in G[k]: 
            cel_v = G[k][mur][0]
            ep = G[k][mur][1]
            # cel_v, ep = G[k][mur]
            if cel_v not in D:
                if d[cel_v]>d[k]+ep:
                    d[cel_v]=d[k]+ep
                    P[cel_v]=k
        D[k]=d[k]
        del(d[k])
    return D, P

def plus_court_chemin(P, n, m):
    cel = (n, m)
    c = [cel]
    while cel != (1, 1):
        c.append(P[cel])
        cel = P[cel]
    c.reverse()

    return c

D = dijkstra_pred(G, (1, 1))[0]
P = dijkstra_pred(G, (1, 1))[1]
# print("energie minimale : ", D)
# print(P)
print(plus_court_chemin(P, n, m))


DessinerGrille.dessiner_grille(G, 3, 4, 70)

# d = {1: 12, 3:13, 5:14}
# for nb in d:
#     print(nb)
