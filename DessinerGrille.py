import Grille

#pos commence de (1, 1) et correspand à la position de la tortue
def ep_mur(grille, pos, dir, n, m): #n: nombre de lignes  #m: nombre de colonnes
    '''fonction qui prend en paramètre une grille, la position de la tortue et la direction : horizontale ou verticale, 
    et retourne l'épaisseur du mur à dessiner'''
    if dir == 'h': #si la direction est horizontale
        if pos[0] == n+1: #si la tortue se trouve à la ligne n+1
            return grille[(n, pos[1])]['b'][1] #on retourne l'épaisseur du mur du bas de la cellule de la dérnière ligne et même colonne que la tortue
        else: #sinon
            return grille[pos]['h'][1] #on retourne l'épaisseur du mur du haut à la même position que celle de la tortue
    elif dir == 'v': #si la direction est verticale
        if pos[1] == m+1: #si la tortue se trouve à la colonne m+1
            return grille[(pos[0], m)]['d'][1] #on retourne l'épaisseur du mur droit de la cellule de la dérnière colonne et ayant la même ligne que la tortue
        else: #sinon
            return grille[pos]['g'][1] #on retourne l'épaisseur du mur gauche à la même position que celle de la tortue







def colorer_mur(t, ep):
    '''Fonction prenant en paramètre une instance du module 'turtle', une épaisseur et défini une ceraine couleur pour t'''
    #les choix des couleurs sont pris arbitrairement
    if ep == 1: #si l'épaisseur est 1
        t.color("red") #on met la couleur de la tortue au rouge
    elif ep == 2:  #si l'épaisseur est 2
        t.color("lime") #on met la couleur de la tortue au vert citron
    elif ep == 3:  #si l'épaisseur est 3
        t.color("skyblue") #on met la couleur de la tortue au blue ciel
    elif ep == 4:  #si l'épaisseur est 4
        t.color("blue") #on met la couleur de la tortue au blue
    elif ep == 5:  #si l'épaisseur est 5
        t.color("yellow") #on met la couleur de la tortue au jaune











    
def ajoute_coor(t, n, m, pas=100):
    '''Fonction qui dessine les coordonnées sous la forme (ligne, colonnes) au centre de chaque cellule de la grille'''
    t.color("red") #on change la couleur vers le rouge
    t.up() #on empeche la tortue de dessiner dérière elle
    t.goto(-750 + pas/2, 300 - pas/2) #on met la tortue à la position initiale (-750, 300), puis on la décale de 'pas/2' pour la centrer
    t.seth(0) #on dirige la tortue vers la gauche
    for l in range(1, n+1): #on parcours les lignes de la grille
        for c in range(1, m+1): #on parcours les colonnes de la grille
            pos = "(" + str(l) + "," + str(c) + ")" #on prépare le texte : '(ligne, colonne)'
            t.write(pos , move=False,align='center',font=('Arial',8,'bold')) #on écrit le texte
            t.forward(pas) #on avance d'un pas
        t.backward((m)*pas) #une fois la ligne finie, on recule de m pas
        t.right(90) #on tourne vers la droite (direction vers le bas)
        t.forward(pas) #on avance d'un pas
        t.left(90) #on tourne vers la gauche (direction vers la droite)


















def dessiner_grille(t, grille, n, m, pas=100, speed=5):
    '''Fonction qui dessine la grille, les paramètres 'pas' et 'speed' sont optionnelles, ils décident des dimentions de la cellule et de la vitesse de la tortue '''
    t.speed(speed) #on change la vitesse de la tortue
    t.shape("turtle") #on change la forme de la tortue
    t.bgcolor("black") #on change le font de la fenêtre sur laquelle déssine la tortue vers le noir
    t.up() #on empêche la tortue de dessiner dérière elle
    t.goto(-750, 300) #on positionne la tortue à (-750, 300)
    t.down() #la tortue désormais trace le chemin dérière elle

    #DESSIN DES MURS HORIZONTAUX
    for l in range(1, n+2): #parcours des lignes de la grille
        for c in range(1, m+1): #parcours des colonnes de la grille
            ep = ep_mur(grille, (l, c), 'h', n, m) #on stock l'épaisseur du mur haut de la cellule courante
            colorer_mur(t, ep) #on ajuste la couleur
            t.width(6 + (ep-1)*4) #on amplifie l'épaisseur à la l'aide de la transformation 6 + (ep-1)*4, puis on l'applique à la tortue
            t.forward(pas) #on trace le mur haut
        t.up() #on arrete de dessiner
        t.backward(m*pas) #on recule de m pas, pour démarer le dessin de la ligne prochaine
        t.right(90) #on tourne vers le bas
        t.forward(pas) #on avance vers la ligne prochaine
        t.left(90) #on tourne à droite
        t.down() #on commence à tracer

    #DESSIN DES MURS HORIZONTAUX
    t.up() #on arrête de tracer
    t.right(90) #on tourne vers le bas
    t.backward((n+1)*pas) #on recule de n+1 pas, pour retourner vers la position de départ en haut à gauche
    t.down() #on commence à tracer


    for c in range(1, m+2): #parcours de colonnes
        for l in range(1, n+1): #parcours de lignes
            ep = ep_mur(grille, (l, c), 'v', n, m) #
            colorer_mur(t, ep)
            t.width(6 + (ep-1)*4)
            t.forward(pas)
        t.up()
        t.backward(n*pas)
        t.left(90)
        t.forward(pas)
        t.right(90)
        t.down()

    ajoute_coor(t, n, m, pas)
    t.color("white")
    t.up()
    t.color("white")




def DesssinerPCC(t, PCC, Gr, pas, color, cout, speed=1,):
    t.speed(speed)
    t.up()
    t.goto(-750, 300)
    t.seth(0)
    for i in range(len(PCC) - 1):
        ep = 0
        x, y = 0, 0
        l1, c1 = PCC[i]
        l2, c2 = PCC[i+1]
        if l1 == l2 and c1 == c2 + 1:
            ep = Gr[PCC[i]]['g'][1]
            x = -750 + (PCC[i][1] - 1) * pas
            y = 300 - (PCC[i][0] - 1) * pas 
            t.width(6 + (ep-1)*4)
            t.seth(-90)
        elif l1 == l2 + 1 and c1 == c2:
            ep = Gr[PCC[i]]['h'][1]
            x = -750 + (PCC[i][1] - 1) * pas 
            y = 300 - (PCC[i][0] - 1) * pas
            t.width(6 + (ep-1)*4)
            t.seth(0)
        elif l1 == l2 and c1 == c2 - 1:
            ep = Gr[PCC[i]]['d'][1]
            x = pas -750 + (PCC[i][1] - 1) * pas
            y = 300 - (PCC[i][0] - 1) * pas
            t.width(6 + (ep-1)*4)
            t.seth(-90)
        elif l1 == l2 - 1 and c1 == c2:
            ep = Gr[PCC[i]]['b'][1]
            x = -750 + (PCC[i][1] - 1) * pas
            y = - pas + 300 - (PCC[i][0] - 1) * pas
            t.width(6 + (ep-1)*4)
            t.seth(0)
        t.goto(x, y)
        t.down()
        t.color(color)
        t.forward(pas/3)
        t.color("black")
        t.forward(pas/3)
        t.color(color)
        t.forward(pas/3)
        t.up()
    Ecrire_chemin_cout(t, PCC, cout, 2)


def Ecrire_chemin_cout(t, PCC, cout, pos_i):
    if pos_i == 1:
        t.up()
        t.color("white")
        t.goto(-710, 375)
        t.write("Chemin : ", move=True, align='left', font=('Georgia', 15, 'bold'))
        for cel in PCC:
            text = str(cel) + "  "
            t.write(text , move=True,align='left',font=('Georgia',15,'bold'))
        t.up()
        t.goto(-710, 355)
        t.write("Cout : " + str(cout), move=True, align='left', font=('Georgia', 15, 'bold'))
    else:
        t.up()
        t.color("white")
        t.goto(-710, 335)
        t.write("Chemin : ", move=True, align='left', font=('Georgia', 15, 'bold'))
        for cel in PCC:
            text = str(cel) + "  "
            t.write(text , move=True,align='left',font=('Georgia',15,'bold'))
        t.up()
        t.goto(-710, 315)
        t.write("Cout : " + str(cout), move=True, align='left', font=('Georgia', 15, 'bold'))

def rid_t(t):
    '''éloigner la tortue de la grille'''
    t.up()
    t.goto(-750, 400)
    t.done()

#____________partie_tests___________________
# print( ep_mur(grille, (1, 5), 'v', 3, 4) )
# ajoute_coor(3, 4, 70)
# n, m = 3, 4
# Gr = Grille.creer_grille(n, m)
# dessiner_grille(Gr, n, m, 70)
#______________end_tests___________________




