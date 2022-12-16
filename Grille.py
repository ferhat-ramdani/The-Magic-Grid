#ceci sera par la suite une classe portant le nom 'Grille"
#tu trouvera une autre manière (que je juge plus simple) de coder la class grille
#on utilisera un graph non orieté pondéré comme structure de donnée pour coder la dite "grille"
#les sommets du graphe seront les cellules de la grille, ils seront identifiés par leur position
#les aretes du graphe représentent les murs séparant les deux céllules, ces dérières corresponderant
#aux sommets adjacents de l'arete. Enfin le poids de chaque arete repésentera l'épaisseur du mur 
#correspondant

#on va respecter la structure d'une liste d'adjacence, la grille aura donc pour structure:
#un dictionnaire dont les atribus sont les sommets, et les valeurs sont les (aretes + poids), i.e:
# grille = { 
#     (1, 1): {
#         'g': [(1, 1), 1],
#         'h' : [(1, 1), 1],
#         'd' : [(1, 2), 5],
#         'b' : [(1, 5), 2]
#     },
#     (1, 2): {
#         'g': [(1, 1), 5],
#         'h' : [(1, 2), 2],
#         'd' : [(1, 3), 1],
#         'b' : [(1, 5), 3]
#     },
#     # { ... }
# }




from random import randint as rnd






def generer_ep():
    '''fonciton qui une épaisseur généré aléatoirement, entre 1 et 5'''
    return rnd(1, 5)








#n: nombre de lignes
#m: nombre de colonnes
def creer_grille(n, m):
    '''fonciton qui crée la grille et la retourne'''

    #initailisation du dictionnaire grille:
    grille = {}


    


    def ajouter_cel_à_grille(pos):
        '''fonction qui prépare la cellule courante sour forme d'un dicionnaire, et le rajoute à la grille'''
        
        cel = {}

        if pos[1] == 1:
            cel['g'] = [ pos, generer_ep() ]
        else:
            cel['g'] = [ (pos[0], pos[1] - 1), generer_ep() ]

        if pos[0] == 1:
            cel['h'] = [ pos, generer_ep() ]
        else:
            cel['h'] = [ (pos[0] - 1, pos[1]), generer_ep() ]

        if pos[1] == m:
            cel['d'] = [ pos, generer_ep() ]
        else:
            cel['d'] = [ (pos[0], pos[1] + 1), generer_ep() ]

        if pos[0] == n:
            cel['b'] = [ pos, generer_ep() ]
        else:
            cel['b'] = [ (pos[0] + 1, pos[1]), generer_ep() ]


        grille[pos] = cel
        return cel


    



    #parcourir les lignes, puis les colonnes de la grille:
    for l in range(1, n+1):
        for c in range(1, m+1):
            ajouter_cel_à_grille( (l, c) )
    return grille







#_________________parties tests_______________

# print(generer_ep())

# print(creer_grille(5, 10))
