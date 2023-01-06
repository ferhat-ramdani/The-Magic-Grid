#pos commence de (1, 1) et correspand à la position de la tortue
def ep_mur(grille, pos, dir, n, m): #n: nombre de lignes  #m: nombre de colonnes
    '''fonction qui prend en paramètre une grille, la position de la tortue et la 
    direction : horizontale ou verticale, et retourne l'épaisseur du mur à dessiner'''
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
    '''Fonction prenant en paramètre une instance du module 'turtle', 
    une épaisseur et défini une ceraine couleur pour t'''
    #les choix des couleurs sont pris arbitrairement
    if ep == 1: #si l'épaisseur est 1
        t.color("blue") #on met la couleur de la tortue au blue
    elif ep == 2:  #si l'épaisseur est 2
        t.color("skyblue") #on met la couleur de la tortue au blue ciel
    elif ep == 3:  #si l'épaisseur est 3
        t.color("lime") #on met la couleur de la tortue au vert
    elif ep == 4:  #si l'épaisseur est 4
        t.color("red") #on met la couleur de la tortue au rouge
    elif ep == 5:  #si l'épaisseur est 5
        t.color("yellow") #on met la couleur de la tortue au jaune











    
def ajoute_coor(t, n, m, pas=100):
    '''Fonction qui dessine les coordonnées sous la forme (ligne, colonnes) au centre 
    de chaque cellule de la grille'''
    t.color("red") #on change la couleur vers le rouge
    t.up() #on empeche la tortue de dessiner dérière elle
    t.goto(-700 + pas/2, 300 - pas/2) #on met la tortue à la position initiale (-700, 300), puis on la décale de 'pas/2' pour la centrer
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


















def dessiner_grille(t, grille, n, m, pas=100, speed=11):
    '''Fonction qui dessine la grille, les paramètres 'pas' et 'speed' sont optionnelles, 
    ils décident des dimentions de la cellule et de la vitesse de la tortue '''
    t.speed(speed) #on change la vitesse de la tortue
    t.shape("turtle") #on change la forme de la tortue
    t.bgcolor("black") #on change le font de la fenêtre sur laquelle déssine la tortue vers le noir
    t.up() #on empêche la tortue de dessiner dérière elle
    t.goto(-700, 300) #on positionne la tortue à (-700, 300)
    t.down() #la tortue désormais trace le chemin dérière elle
    wn = t.Screen()
    wn.title("GRILLE MAGIQUE")
    wn.setup(1.0, 1.0) #on ajuste les dimensions de la fenetre pour remplir l'écran

    #DESSIN DES MURS HORIZONTAUX
    for l in range(1, n+2): #parcours des lignes de la grille
        for c in range(1, m+1): #parcours des colonnes de la grille
            ep = ep_mur(grille, (l, c), 'h', n, m) #on stoque l'épaisseur du mur haut de la cellule courante
            colorer_mur(t, ep) #on ajuste la couleur
            t.width(6 + (ep-1)*4) #on amplifie l'épaisseur à la l'aide de la transformation 6 + (ep-1)*4, puis on l'applique à la tortue
            t.forward(pas) #on trace le mur haut
        t.up() #on arrete de dessiner
        t.backward(m*pas) #on recule de m pas, pour démarer le dessin de la ligne prochaine
        t.right(90) #on tourne vers le bas
        t.forward(pas) #on avance vers la ligne prochaine
        t.left(90) #on tourne à droite
        t.down() #on commence à tracer

    t.up() #on arrête de tracer
    t.right(90) #on tourne vers le bas
    t.backward((n+1)*pas) #on recule de n+1 pas, pour retourner vers la position de départ en haut à gauche
    t.down() #on commence à tracer

    # DESSIN DES MURS VERTICAUX
    for c in range(1, m+2):
        for l in range(1, n+1):
            ep = ep_mur(grille, (l, c), 'v', n, m)
            colorer_mur(t, ep)
            t.width(6 + (ep-1)*4)
            t.forward(pas)
        t.up()
        t.backward(n*pas)
        t.left(90)
        t.forward(pas)
        t.right(90)
        t.down()

    ajoute_coor(t, n, m, pas) #on dessine les coordonnées des cellules
    t.color("white") #on change la couleur vers 'blache'
    t.up() #on arrête de dessiner




def DesssinerPCC(t, PCC, Gr, pas, color, cout, algo, speed=11, emplacement = 1):
    '''Fonction qui trace le murs percés'''
    t.speed(speed) #on ajuste la vitesse de la tortue
    t.up() #on arrête de dessiner
    t.goto(-700, 300) #on positionne la tortue à (-700, 300)
    t.seth(0) #on oriente la tortue vers la droite
    for i in range(len(PCC) - 1): #on parcours les cellules jusqu'à l'avant dérnière
        ep = 0 #initialisation
        x, y = 0, 0 #initialisation
        l1, c1 = PCC[i] #on sauvegarde la ligne et colonne de la cellule courante dans les variables 'l1' et 'c1'
        l2, c2 = PCC[i+1] #on refait la même chose pour la cellule suivante
        if l1 == l2 and c1 == c2 + 1: #si la cellule suivante se trouve à gauche de la courante
            ep = Gr[PCC[i]]['g'][1] #on récupère l'épaisseur du mur gacuhe de la cellule courante
            x = -700 + (c1 - 1) * pas #on avance de c1-1 pas de la position initiale (-700)
            y = 300 - (l1 - 1) * pas #on avance (vers le bas) de l1-1 pas de la position initiale (300)
            t.width(6 + (ep-1)*4) #on ajuste l'épaisseur du traçage
            t.seth(-90) #on dirige la tortue vers le bas
        elif l1 == l2 + 1 and c1 == c2: #si la cellule suivante se trouve au dessus de la courante
            ep = Gr[PCC[i]]['h'][1]
            x = -700 + (c1 - 1) * pas 
            y = 300 - (l1 - 1) * pas
            t.width(6 + (ep-1)*4)
            t.seth(0)
        elif l1 == l2 and c1 == c2 - 1: #si la cellule suivante se trouve à la droite de la courante
            ep = Gr[PCC[i]]['d'][1]
            x = pas -700 + (c1 - 1) * pas
            y = 300 - (l1 - 1) * pas
            t.width(6 + (ep-1)*4)
            t.seth(-90)
        elif l1 == l2 - 1 and c1 == c2: #si la cellule suivante se trouve en dessous de la courante
            ep = Gr[PCC[i]]['b'][1]
            x = -700 + (c1 - 1) * pas
            y = - pas + 300 - (l1 - 1) * pas
            t.width(6 + (ep-1)*4)
            t.seth(0)
        t.goto(x, y) #on positionne la tortue à la position (x, y)
        t.down() #on commence à dessiner
        t.color(color) #on modifie la couleur de la tortue
        t.forward(pas/3) #on avance d'un tier de pas
        t.color("black") #on change la couleur vers 'noir' pour dessiner le trou dans le mur
        t.forward(pas/3) #on avance d'un tier de pas
        t.color(color) #on change la couleur de la tortue
        t.forward(pas/3) #on avance d'un tier de pas
        t.up() #on arrête de dessiner
    Ecrire_chemin_cout(t, PCC, cout, emplacement, algo) #on dessine le chemin minimisant le cout, ainsi que son cout
    rid_t(t)


def Ecrire_chemin_cout(t, PCC, cout, pos_i, algo):
    '''Fonction qui écrit sur la fenêtre de dessin le chemin minimisant le cout, 
    ainsi que le cout correspondant, pos_i sert à spécifier l'emplacement où 
    on veux écrire'''
    if pos_i == 1: #emplacement 1
        t.up() #on ne dessine pas
        t.color("white") #on met la couleur à 'blanche'
        t.goto(-710, 375) #on se place à (-710, 375)
        t.write("Chemin (" + algo + ") : ", move=True, align='left', font=('Georgia', 15, 'bold')) #on écrit 'chemin : ' sur la fenêtre
        for cel in PCC: #on parcourt les cellules de la grille
            text = str(cel) + "  " #on prépare le texte à afficher
            t.write(text , move=True,align='left',font=('Georgia',15,'bold')) #on écrit la position de la cellule courante
        t.goto(-710, 355) #on se place à (_710, 355)
        t.write("Cout : " + str(cout), move=True, align='left', font=('Georgia', 15, 'bold')) #on écrit 'cout : ' sur la fenêtre
    else: #emplacement 2
        t.up()
        t.color("white")
        t.goto(-710, 335) #on se un peu plus bas
        t.write("Chemin (" + algo + ") : ", move=True, align='left', font=('Georgia', 15, 'bold'))
        for cel in PCC:
            text = str(cel) + "  "
            t.write(text , move=True,align='left',font=('Georgia',15,'bold'))
        t.up()
        t.goto(-710, 315) #on se place plus bas que l'emplacement 1
        t.write("Cout : " + str(cout), move=True, align='left', font=('Georgia', 15, 'bold'))
    rid_t(t)

def rid_t(t):
    '''Fonction qui éloigne la tortue de la grille déssinée, en la place 
    tout en haut à gauche'''
    t.up() #on arrête de dessiner
    t.goto(-750, 400) #on se place en haut à gauche