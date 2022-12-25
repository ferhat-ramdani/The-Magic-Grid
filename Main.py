import turtle as t
import Grille as G
import DessinerGrille as DG
import  PlusCoursChemin as PCC

n, m = 3, 4
maGrille = G.creer_grille(n, m)
DG.dessiner_grille(t, maGrille, n, m,100, 11)
pcc_bel, cout = PCC.plus_court_chemin(maGrille, n, m, 'bel')
DG.DesssinerPCC(t, pcc_bel, maGrille, 100, "gray", cout, 11)
DG.rid_t(t)