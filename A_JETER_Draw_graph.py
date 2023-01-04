#classe pas du tout importante, 
#dans cette classe, j'éssaie d'écrire sur la consolle une structure de donnée, dont j'aurai besoin plus tard.

import Grille

G = Grille.creer_grille(2, 2)
for cel in G:
    print( "(" + str(cel[0]) + "," + str(cel[1]) + ")" )
for cel in G:
    for mur in G[cel]:
        print( "(" + str(cel[0]) + "," + str(cel[1]) + ") (" + str( G[cel][mur][0][0] ) + "," + str( G[cel][mur][0][1] ) + ") " + str( G[cel][mur][1] ) )