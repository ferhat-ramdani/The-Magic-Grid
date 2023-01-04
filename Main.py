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
#DG.DesssinerPCC(t, pcc_bel, maGrille, 40, "gray", cout, 11)
#DG.DesssinerPCC(t, pcc_djiks, maGrille, 40, "white", cout2, 11)enrich.enrichir(maGrille,pcc_djiks)
enrich.enrichir(maGrille,pcc_djiks)
enrich.adapter_dessin(t,maGrille)
pcc_non_opt, cout_non_opt = b.efficace_pas_opti(maGrille, n, m)
DG.DesssinerPCC(t, pcc_non_opt, maGrille, 70, "gray", cout_non_opt, 11)
DG.rid_t(t)

"""Tu retrouveras ici des tests que j'ai essayé de faire mais qui ne fonctionne pas le problème 
vien peut etre de l'importation des classe bBonus ou de Enrichir_Grille ?"""
