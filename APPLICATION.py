import Grille
import DessinerGrille
import PlusCoursChemin
import Enrichir_Grille
import Bonus
import turtle as t


#__________APPLICATION_Grille___________

# print( Grille.generer_ep() ) #test de la fonction generer_ep()
# n, m = 3, 4 #initialisatoin des dimensions de la grille

# #la suite est un test de la fonction creer_grille():
# grille = Grille.creer_grille(n, m)
# print('grille = {')
# for cel in grille:
#     if cel != (n, m):
#         print('   ', cel, ':', grille[cel], ',')
#     else:
#         print('   ', cel, ':', grille[cel])
# print('\n}')

# # exemple de sortie de l'appel grille(3, 4):

# # grille = {
# #     (1, 1) : {'g': [(1, 1), 5], 'h': [(1, 1), 5], 'd': [(1, 2), 3], 'b': [(2, 1), 2]},
# #     (1, 2) : {'g': [(1, 1), 3], 'h': [(1, 2), 2], 'd': [(1, 3), 3], 'b': [(2, 2), 2]},
# #     (1, 3) : {'g': [(1, 2), 3], 'h': [(1, 3), 4], 'd': [(1, 4), 2], 'b': [(2, 3), 4]},
# #     (1, 4) : {'g': [(1, 3), 2], 'h': [(1, 4), 5], 'd': [(1, 4), 4], 'b': [(2, 4), 4]},
# #     (2, 1) : {'g': [(2, 1), 2], 'h': [(1, 1), 2], 'd': [(2, 2), 1], 'b': [(3, 1), 5]},
# #     (2, 2) : {'g': [(2, 1), 1], 'h': [(1, 2), 2], 'd': [(2, 3), 3], 'b': [(3, 2), 1]},
# #     (2, 3) : {'g': [(2, 2), 3], 'h': [(1, 3), 4], 'd': [(2, 4), 3], 'b': [(3, 3), 4]},
# #     (2, 4) : {'g': [(2, 3), 3], 'h': [(1, 4), 4], 'd': [(2, 4), 5], 'b': [(3, 4), 3]},
# #     (3, 1) : {'g': [(3, 1), 4], 'h': [(2, 1), 5], 'd': [(3, 2), 1], 'b': [(3, 1), 3]},
# #     (3, 2) : {'g': [(3, 1), 1], 'h': [(2, 2), 1], 'd': [(3, 3), 3], 'b': [(3, 2), 1]},
# #     (3, 3) : {'g': [(3, 2), 3], 'h': [(2, 3), 4], 'd': [(3, 4), 5], 'b': [(3, 3), 3]},
# #     (3, 4) : {'g': [(3, 3), 5], 'h': [(2, 4), 3], 'd': [(3, 4), 2], 'b': [(3, 4), 4]}
# # }

# #fin de test de la fonction creer_grille()

#_____________APPLICATION_DessinerGrille_______________

# n, m = 3, 4
# grille = Grille.creer_grille(n, m)
# print( DessinerGrille.ep_mur(grille, (2, 2), 'v', n, m)) #test de 'ep_mur()' sur le mur gauche de la cellule (2, 2)
# DessinerGrille.ajoute_coor(t, n, m) #test de la fonction 'ajoute_coor()'
# DessinerGrille.dessiner_grille(t, grille, n, m) #test de la fonction 'dessiner_grille()'
# DessinerGrille.rid_t(t) #test de la fonction 'rid_t()'
# t.done()

#______________APPLICATION_PlusCoursChemin______________

# n, m = 3, 4
# grille = Grille.creer_grille(n, m)
# print('Dijkstra : \n')
# print(PlusCoursChemin.dijkstra(grille, (1, 1))) #test de la fonction 'dijkstra()'
# print('\nBellman-Ford : \n')
# print(PlusCoursChemin.bellman_ford(grille, (1, 1))) #test de la fonction 'bellman_ford()'
# print('\nChemin avec cout minimal : \n')
# print(PlusCoursChemin.plus_court_chemin(grille, n, m)) #test de la fonction 'plus_cours_chemin'

#______________APPLICATOIN_Enrichir_Grille______________

n, m = 3, 4
grille = Grille.creer_grille()
pcc = PlusCoursChemin.plus_court_chemin(grille, n, m)[0]
Enrichir_Grille.enrichir(grille, pcc) #test de la fonction 'enrichir()'
