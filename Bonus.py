def efficace_pas_opti(grille, n, m): #Fonction utilisant Strategie Gloutonne prenant le mur localement optimal
    Chemin_dir = [(1, 1)] #Tableau correspondant au chemin commence de (1,1) correspondant à la première cellule et va jusqu'à la derniere cellule (n,m)
    coût_dir = 0 # Cout du chemin dans le sens direct qui sera incrémenté à chaque epaisseur du mur de rencontré de la cellule (1,1) jusqu'a la cellule (n,m)
    Chemin_indir = [(n, m)] #Tableau correspondant chemin commence de (n,m) correspondant à la derniere cellule et va jusqu'à la premiere cellule (1,1)
    coût_indir = 0 # Cout du chemin dans le sens indirect qui sera incrémenté à chaque épaisseur rencontré de la cellule (n,m) jusqu'a la cellule (1,1)
    fin = False #Variable booléenne initialisé à False et qui indiquera le fait qu'on soit arrivé sur la derniere case

    #chemin loc_opt_dir
    while not fin: # Tant que fin est different de True c'est à dire qu'on a pas parcourut tout le chemin
        l, c = Chemin_dir[-1] #On récupère la derniere case de notre Tableau Chemin_dir qui indique ou on se trouve actuellement
        if l == n and c == m: # On verifie si on est sur la derniere cellule de la grille
            fin = True # Si c'est le cas on affecte True à notre Variable 
        elif l == n: #Sinon on verifie si on est sur la derniere ligne , on continue notre chemin uniquement à droite
            Chemin_dir.append( (l, c+1) ) # On ajoute dans notre Tableau de chemin parcourut la cellule voisine droite car on ne peut passer que par la droite  
            coût_dir += grille[(l, c)]['d'][1] # On incrémente le cout du chemin avec l'epaisseur du mur de de la cellule droite
        elif c == m: #Sinon on verifie si on est sur la derniere colonne , on continue notre chemin uniquement en bas
            Chemin_dir.append( (l+1, c) ) # On ajoute dans notre Tableau de chemin parcourut la cellule voisine du bas car on ne peut passer que par le bas
            coût_dir += grille[(l, c)]['b'][1] # On incrémente le cout du chemin avec l'epaisseur du mur de de la cellule du bas
        else:
            if grille[(l, c)]['d'][1] < grille[(l, c)]['b'][1]: # Sinon on compare le mur de droit avec le mur du bas et on prend la valeur la moins epaisse
                Chemin_dir.append( grille[(l, c)]['d'][0] ) #On ajoute le choix localement optimal ici dans notre cas la cellule droite
                coût_dir += grille[(l, c)]['d'][1]  # On incrémente le cout direct avec l'epaisseur du mur de la cellule droite
            else:
                Chemin_dir.append( grille[(l, c)]['b'][0] ) # Sinon On ajoute la cellule du bas dans le tableau de Chemin_dir
                coût_dir += grille[(l, c)]['b'][1] # On incrémente le cout direct avec l'epaisseur du mur de la cellule du bas

    fin = False
    #On répète ce processus pour le chemin indirect 
    while not fin: # Tant que fin est different de True c'est à dire qu'on a pas parcourut tout le chemin
        l, c = Chemin_indir[-1] #On récupère la derniere case de notre Tableau Chemin_indir qui indique ou on se trouve actuellement
        if l == 1 and c == 1: # On verifie si on est sur la premiere cellule de la grille
            fin = True # Si c'est le cas on affecte True à notre Variable 
        elif l == 1: #Sinon on verifie si on est sur la premiere ligne , on continue notre chemin uniquement à gauche
            Chemin_indir.append( (l, c-1) )  # On ajoute dans notre Tableau de chemin parcourut la cellule voisine gauche car on ne peut passer que par la gauche
            coût_indir += grille[(l, c)]['g'][1] # On incrémente le cout indirect du chemin avec l'epaisseur du mur de de la cellule gauche
        elif c == 1: #Sinon on verifie si on est sur la premiere colonne , on continue notre chemin uniquement en haut
            Chemin_indir.append( (l-1, c) ) # On ajoute dans notre Tableau de chemin parcourut la cellule voisine du haut car on ne peut passer que par le haut
            coût_indir += grille[(l, c)]['h'][1] # On incrémente le cout indirect avec l'epaisseur du mur de la cellule du haut

        else:
            if grille[(l, c)]['g'][1] < grille[(l, c)]['h'][1]: # Sinon on compare le mur de gauche avec le mur du haut et on prend la valeur la moins epaisse
                Chemin_indir.append( grille[(l, c)]['g'][0] ) #On ajoute le choix localement optimal ici dans notre cas la cellule gauche 
                coût_indir += grille[(l, c)]['g'][1] # On incrémente le cout indirect avec l'epaisseur du mur de la cellule gauche
            else:
                Chemin_indir.append( grille[(l, c)]['h'][0] ) # Sinon On ajoute la cellule du haut dans le tableau de Chemin_indir
                coût_indir += grille[(l, c)]['h'][1] # On incrémente le cout indirect avec l'epaisseur du mur de la cellule du haut
    
    if coût_dir < coût_indir: # On compare le cout direct avec le cout indirect pour avoir le meilleur cout
        return Chemin_dir, coût_dir # Si le cout direct est moindre que le cout indirect on retourne le chemin direct et le cout direct
    else:
        return Chemin_indir, coût_indir # Sinon on retourne le chemin indirect et le cout indirect