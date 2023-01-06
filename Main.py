import turtle as t
import Grille
import DessinerGrille
import  PlusCoursChemin
import Enrichir_Grille
import Bonus

n, m = 6,7 
pas = 80
maGrille = Grille.creer_grille(n, m)
DessinerGrille.dessiner_grille(t, maGrille, n, m, pas, 11)
# pcc_bel, cout_bel = PlusCoursChemin.plus_court_chemin(maGrille, n, m, 'bel')
# Enrichir_Grille.enrichir(maGrille, pcc_bel)
# Enrichir_Grille.adapter_dessin(t, maGrille, pcc_bel, cout_bel, "bel", 'white' , pas, 1)
pcc_dij, cout_dij = PlusCoursChemin.plus_court_chemin(maGrille, n, m, 'dij')
Enrichir_Grille.enrichir(maGrille, pcc_dij)
Enrichir_Grille.adapter_dessin(t, maGrille, pcc_dij, cout_dij, "dij", 'white' , pas, 1)
pcc_bonus, cout_bonus = Bonus.efficace_pas_opti(maGrille, n, m)
DessinerGrille.DesssinerPCC(t, pcc_bonus, maGrille, pas, "gray", cout_bonus, "bonus", 11, 2)

t.done()