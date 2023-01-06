import DessinerGrille

def enrichir(grille, PCC):  #Fonction qui va enrichir notre Grille ajoutant une valeur True 
    for i in range(len(PCC) - 1):
        l, c = PCC[i] # Recupere la position de la cellule i du plus court chemin
        l_, c_ = PCC[i+1] # Recupere la position de la cellule i+1 du plus court chemin
        if l == l_ and c == c_ + 1: # Comparaison des coordonnées entres le deux cellules récuperes pour avoir le mur concerné
            # Si ligne identiques mais colonne de la cellule i+1 est differentes de +1 de la cellule i alors ce sont le murs gauche de la cellule i et le mur droit de le cellule i+1 qui sont concernées 
            grille[PCC[i]]['g'].append(True) # Ajout d'une valeur True au mur gauche de la cellule i en question dans notre dictionnaire correspondant à la grille
            grille[PCC[i+1]]['d'].append(True) #Ajout d'une valeur True au mur droit de la cellule i+1 en question dans notre dictionnaire correspondant à la grille
        elif l == l_ and c == c_ - 1:
            # Si ligne identiques mais colonne de la cellule i+1 est differentes de +1 de la cellule i alors ce sont le murs droit de la cellule i et le mur gauche de le cellule i+1 qui sont concernées 
            grille[PCC[i]]['d'].append(True) # Ajout d'une valeur True au mur droit de la cellule i en question dans notre dictionnaire correspondant à la grille
            grille[PCC[i+1]]['g'].append(True) #Ajout d'une valeur True au mur gauche de la cellule i+1 en question dans notre dictionnaire correspondant à la grille
        elif l == l_ + 1 and c == c_: 
            # Si colonne identiques mais ligne de la cellule i est differentes de +1 de la cellule i +1 alors ce sont le murs haut de la cellule i et le mur bas de le cellule i+1 qui sont concernées
            grille[PCC[i]]['h'].append(True) # Ajout d'une valeur True au mur haut de la cellule i en question dans notre dictionnaire correspondant à la grille
            grille[PCC[i+1]]['b'].append(True) # Ajout d'une valeur True au mur bas de la cellule i+1 en question dans notre dictionnaire correspondant à la grille
        elif l == l_ - 1 and c == c_: # Si colonne identiques mais ligne de la cellule i+1 est differentes de +1 de la cellule i  alors ce sont le murs bas de la cellule i et le mur haut de le cellule i+1 qui sont concernées
            grille[PCC[i]]['b'].append(True) # Ajout d'une valeur True au mur bas de la cellule i en question dans notre dictionnaire correspondant à la grille
            grille[PCC[i+1]]['h'].append(True) # Ajout d'une valeur True au mur haut de la cellule i+1 en question dans notre dictionnaire correspondant à la grille
    

# Fonction prenant en paraètres un mur un pas et une cellule qui retournera un angle à notre instance de turtle et une position (x,y) pour qu'elle se place ainsi qu'une pos afin de récuperer le mur voisin par la suite
def general(mur, pas, cel):  
    angle, pos = 0, '' # Initialisations des valeurs à renvoyés
    x, y = 0, 0 #Initialisation de la position de l'instance turtle
    if mur == 'g': # Si mur est gauche
        pos = 'd' # Mur Commun sera le mur droit de la cellule voisine
        angle = -90 # angle pour positionner l'instance afin de dessiner le mur vertical -90 pour qu'elle se positionne verticalement
        x = -750 + (cel[1] - 1) * pas #Position de la turtle des abcisses x décalés de l'origine + (nombre de colonne *pas) 
        y = 300 - (cel[0] - 1) * pas #Position de la turtle des ordonnées y décalés de l'origine + (nombre de ligne *pas)
    elif mur == 'd': # Si mur est droit
        pos ='g' # Mur Commun sera le mur gauche de la cellule voisine
        angle = -90 # angle pour positionner l'instance afin de dessiner le mur vertical -90 pour qu'elle se positionne verticalement
        x = pas -750 + (cel[1] - 1) * pas #Position de la turtle au niveau des abcisses x décalés de l'origine + (nombre de colonne *pas) 
        y = 300 - (cel[0] - 1) * pas  #Position de la turtle au niveau des ordonnées y décalés de l'origine + (nombre de ligne pas)
    elif mur == 'h': # Si mur est haut
        pos ='b'  # Mur Commun sera le mur bas de la cellule voisine
        angle = 0 # angle pour positionner l'instance afin de dessiner le mur horizontal 0 pour qu'elle se positionne horizontalement
        x = -750 + (cel[1] - 1) * pas #Position de la turtle au niveau des abcisses x décalés de l'origine + (nombre de colonne *pas) 
        y = 300 - (cel[0] - 1) * pas #Position de la turtle au niveau des ordonnées y décalés de l'origine + (nombre de ligne pas)
    else :
        pos ='h' # Mur Commun sera le mur haut de la cellule voisine
        angle = 0 # angle pour positionner l'instance afin de dessiner le mur horizontal 0 pour qu'elle se positionne horizontalement
        x = -750 + (cel[1] - 1) * pas #Position de la turtle au niveau des abcisses x décalés de l'origine + (nombre de colonne *pas) 
        y = - pas + 300 - (cel[0] - 1) * pas #Position de la turtle au niveau des ordonnées y décalés de l'origine + (nombre de ligne pas)
    return pos, angle, x, y 
    # Retourne la position du mur de la cellule voisine , l'angle pour dessiner horizontalement ou verticaleent et la position de notre turle (x,y)

def adapter_dessin(t, grille,  pcChemin, cout, algo, color = "white", pas = 100, emplacement = 2):
    t.bgcolor("black")  #on change le font de la fenêtre sur laquelle déssine la tortue vers le noir
    t.speed(11) #on change la vitesse de la tortue
    t.color(color) #On change la couleur de dessin par la valeur blanche par défaut ou une autre valeur
    t.up()
    t.goto(-750, 300) #on positionne la tortue à (-750, 300) en haut à gauche afin de dessiner sur la grille
    t.seth(0) # On change l'angle à O 
    for cel in grille: # Récuperation de la position de chaques cellules dans la grille
        for mur in grille[cel]: # Pour chaques murs de cette cellule recuperer 
            if len(grille[cel][mur]) == 3: 
            # Si l'un de ces murs possède un tableau d'une longueur de 3 cela indique qu'un attribut True à été ajouté donc que c'est un mur du PCC  
                pos, angle, x, y = general(mur, pas, cel)  # Récupere la position de son mur voisin , l'angle de notre turtle et sa position
                cel_rep = grille[cel][mur][0] # Récupere à l'aide du dictionnaire de la cellule voisine en question concerné par ce mur
                del(grille[cel_rep][pos][2]) #Supprime l'attribut True de cette cellule voisine en question pour ne pas dessiner deux fois 
                ep = grille[cel][mur][1] # Récupere l'épaisseur afin de dessiner celle-ci

                t.width(6 + (ep-1)*4) #on amplifie l'épaisseur à la l'aide de la transformation 6 + (ep-1)*4, puis on l'applique à la tortue
                t.seth(angle) #on oriente la tortue vers l'angle retourné qui est soit 0 ou -90
                t.goto(x, y) # On amène la tortue à la position x et y retourné preècedemment pour se trouver au bon endroit 
                t.down() #on commence à dessiner
                t.forward(pas/3) #on avance d'un tier de pas
                t.color("black") #on change la couleur vers 'noir' pour dessiner le trou dans le mur
                t.forward(pas/3) #on avance d'un tier de pas
                t.color(color) #on change la couleur de la tortue
                t.forward(pas/3) #on avance d'un tier de pas
                t.up() #on arrête de dessiner

    DessinerGrille.Ecrire_chemin_cout(t, pcChemin, cout, emplacement, algo) #on dessine le chemin minimisant le cout, ainsi que son cout