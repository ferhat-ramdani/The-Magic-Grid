import turtle as t
import Grille as G
import DessinerGrille as DG
import  PlusCoursChemin as PCC

n, m = 3, 4
maGrille = G.creer_grille(n, m)
DG.dessiner_grille(t, maGrille, n, m,100, 11)

# PS: il se peut que la grille soit mal déssinée
# que certains mur ont une épaisseurs différentes
# de celle inscrite sur la grille

# print(PCC.bellman_ford(maGrille, (1, 1)))
pcc = PCC.plus_court_chemin(maGrille, n, m, 'bel')
DG.DesssinerPCC(t, pcc, maGrille, 100)
t.done()