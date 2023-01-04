import turtle as t
import Grille as G
import DessinerGrille as DG
import  PlusCoursChemin as PCC
import Enrichir_Grille as enrich
import Bonus as b

n, m = 3, 4
pas = 100
maGrille = G.creer_grille(n, m)
DG.dessiner_grille(t, maGrille, n, m, pas, 11)
pcc_bel, cout = PCC.plus_court_chemin(maGrille, n, m, 'bel')
pcc_djiks, cout2 = PCC.plus_court_chemin(maGrille, n, m, 'dij')
DG.DesssinerPCC(t, pcc_bel, maGrille, pas, "gray", cout, 11)
DG.DesssinerPCC(t, pcc_djiks, maGrille, pas, "white", cout2, 11)
DG.rid_t(t)