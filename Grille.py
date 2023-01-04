from random import randint as rnd




def generer_ep():
    '''fonction qui retourne une épaisseur généré aléatoirement, entre 1 et 5'''
    return rnd(1, 5)









def creer_grille(n, m): #n: nombre de lignes  #m: nombre de colonnes
    '''fonction qui crée la grille et la retourne'''
    grille = {} #initailisation du dictionnaire grille:

    def ajouter_cel_à_grille(pos): #on considère que 'pos' est un couple (ligne, colonne), on commence par 1
        '''fonction qui prends la position d'une cellule, et rajoute la valeur de la cellule correspondante à la grille'''
        cel = {} #on ititialise la cellue 'cel' à ajouter à 'grille'

        if pos[1] == 1: #si on est en première colonne
            cel['g'] = [ pos, generer_ep() ] #on ajoute le mur gauche à 'cel', ayant la forme: [position, épaisseur]
        else: #s'il ne s'agit pas de la première colonne
            pos_g = (pos[0], pos[1] - 1) #'pos_g' est la position de la cellule à gauche de 'pos'
            cel['g'] = [ pos_g, grille[pos_g]['d'][1] ] #le mur gauche aura pour position 'cel_g', et pour ép. celle du mur droit de 'cel_g'

        if pos[0] == 1: #si on est en première ligne
            cel['h'] = [ pos, generer_ep() ] # on ajoute le mur du haut à 'cel'
        else: #sinon
            pos_h = (pos[0] - 1, pos[1]) #'pos_b' est la position de la cellule au dessus de 'pos'
            cel['h'] = [ pos_h, grille[pos_h]['b'][1] ] # le mur du haut aura pour position 'cel_b', et pour ép. celle du mur du bas de 'cel_b'

        if pos[1] == m: #si on est en dérnière colonne
            cel['d'] = [ pos, generer_ep() ] #on ajoute le mur droit à 'cel'
        else:
            cel['d'] = [ (pos[0], pos[1] + 1), generer_ep() ] #le mur droit aura la position de la cellule à droite, et une épaisseur générée

        if pos[0] == n: #si on est en dérnière ligne
            cel['b'] = [ pos, generer_ep() ] #on ajoute le mur du bas à 'cel'
        else:
            cel['b'] = [ (pos[0] + 1, pos[1]), generer_ep() ] #le mur du bas aura la position de la cellule en bas, et une épaisseur générée


        grille[pos] = cel #on ajoute la cellule 'cel' à la 'grille'
        return cel #on retourne la cellule

    for l in range(1, n+1): #on parcours les lignes de la grille
        for c in range(1, m+1): #on parcours les colonnes de la grille
            ajouter_cel_à_grille( (l, c) ) #on ajoute la cellule dont la position sur la grille est '(l, c)'
    return grille #on retourne la grille




#_________________parties tests_______________

# print(generer_ep())

# print(creer_grille(3, 4))

# exemple de sortie de l'appel grille(3, 4):

# grille = {
#     (1, 1) : {'g': [(1, 1), 5], 'h': [(1, 1), 5], 'd': [(1, 2), 3], 'b': [(2, 1), 2]},
#     (1, 2) : {'g': [(1, 1), 3], 'h': [(1, 2), 2], 'd': [(1, 3), 3], 'b': [(2, 2), 2]},
#     (1, 3) : {'g': [(1, 2), 3], 'h': [(1, 3), 4], 'd': [(1, 4), 2], 'b': [(2, 3), 4]},
#     (1, 4) : {'g': [(1, 3), 2], 'h': [(1, 4), 5], 'd': [(1, 4), 4], 'b': [(2, 4), 4]},
#     (2, 1) : {'g': [(2, 1), 2], 'h': [(1, 1), 2], 'd': [(2, 2), 1], 'b': [(3, 1), 5]},
#     (2, 2) : {'g': [(2, 1), 1], 'h': [(1, 2), 2], 'd': [(2, 3), 3], 'b': [(3, 2), 1]},
#     (2, 3) : {'g': [(2, 2), 3], 'h': [(1, 3), 4], 'd': [(2, 4), 3], 'b': [(3, 3), 4]},
#     (2, 4) : {'g': [(2, 3), 3], 'h': [(1, 4), 4], 'd': [(2, 4), 5], 'b': [(3, 4), 3]},
#     (3, 1) : {'g': [(3, 1), 4], 'h': [(2, 1), 5], 'd': [(3, 2), 1], 'b': [(3, 1), 3]},
#     (3, 2) : {'g': [(3, 1), 1], 'h': [(2, 2), 1], 'd': [(3, 3), 3], 'b': [(3, 2), 1]},
#     (3, 3) : {'g': [(3, 2), 3], 'h': [(2, 3), 4], 'd': [(3, 4), 5], 'b': [(3, 3), 3]},
#     (3, 4) : {'g': [(3, 3), 5], 'h': [(2, 4), 3], 'd': [(3, 4), 2], 'b': [(3, 4), 4]}
# }

#_______________fin tests__________________