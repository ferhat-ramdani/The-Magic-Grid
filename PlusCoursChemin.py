def minimum(dico): # Fonction retourant la valeur minimale d'un dictionnaire
    m=float('inf') # On initialise m= ∞
    for k in dico: # Pour chaques clés dans le dictionnaire 
        if dico[k] < m: # On compare la valeur de la clé correspondante avec la valeur de m 
            m=dico[k] # Si Valeur de la clé inférieur à m , on affecte m à cette nouvelle valeur 
            i=k # On note l'indice de la clé correspondant à cette nouvelle valeur inférieur à m
    return i # On retourne l'indice de la clé avec la plus petite valeur du dictionnaire 


def dijkstra(G,s):
    D={} # Initialisation d'un dictionnaire qui retournera les distances départ-sommet les plus courts
    d={k: float('inf') for k in G}  # Initialisation d'un dictionnaire avec pour clé la position de chaques cellules et pour valeur ∞
    d[s]=0 # On affecte la valeur 0 à la valeur de la clé correspondant au sommet de départ
    P={} # Initialisation d'un dictionnaire qui correspondra aux prédecesseurs de chaques cellules
    while len(d)>0: 
        k=minimum(d) # On récupere la clé du minimum de notre dictionnaire d correspondant à la position d'une cellule
        for mur in G[k]: # Consultation dans la grille G de chaque mur de la position de la cellule récuperer dans k 
            cel_v, ep = G[k][mur] # Récupère la cellule voisine ainsi que l'épaisseur correspondante
            if cel_v not in D: #On vérifie que cette cellule n'a pas été traité , n'est pas encore dans Le dicitionnaire D
                if d[cel_v]>d[k]+ep: #Si la distance de la cellule voisine est supérieur à la distance de la cellule k + épaisseur 
                    d[cel_v]=d[k]+ep # On à trouvé chemin + court on affecte cette nouvelle valeur à la clé de la cellule voisine dans le dictionnaire d  
                    P[cel_v]=k # On affecte à notre dictionnaire P le prédecesseur de la cellule voisine qui correspond à la cellule k 
        D[k]=d[k] # On affecte a la clé correspondant à k de notre dictionnaire D la nouvelle valeur trouvé
        del(d[k]) # On supprime la clé correspondant à k dans notre dictionnaire d 
    return D, P # On retourne le dictionnaire D qui aura comme clé la position de chaque sommet et pour valeur la distance la plus court avec le sommet de départ


def bellman_ford(G, s):
    d={k: float('inf') for k in G} #distances initiales
    P={} #on initialise la liste des prédécesseurs
    d[s]=0 #sommet de départ
    fini=False #bouléen utilisé pour terminer la boucle while
    while not fini: 
        fini=True #on met fini à True, on le remet à False uniquement si on met à jour les distances
        for cel in G: #parcours des cellules de la grille
            for mur in G[cel]: #parcours des murs de chaque cellule
                cel_v, ep = G[cel][mur] #on récupère la pos de la cellule adjacente, et l'épaisseur du mur
                if d[cel]+ep < d[cel_v]: #si la nouvelle distance est meilleur
                    d[cel_v] = d[cel]+ep #on met à jour la liste des distances
                    P[cel_v]=cel #on met à jour la liste des prédécesseurs
                    fini=False #on remet fini à Fasle pour continuer les itérations
    return d, P #on retourne la liste d des distances, et P des prédécesseurs


def plus_court_chemin(G, n, m, algo='dij'):
    if algo == 'bel': # Si l'algo chosis en paramètre est celui de belman ford
        d, P = bellman_ford(G, (1, 1)) # Application de l'algo Belman-Ford qui retourne la liste de distance et la liste de prédecesseurs
    else: #Sinon c'est celui de Dijkstra 
        d, P = dijkstra(G, (1, 1)) # Application de l'algo Dijkstra qui retourne la liste de distance et la liste de prédecesseurs
    cout = d[(n, m)] # On recupere le cout du chemin en accédant à la derniere cellule de notre tableau d 
    cel = (n, m) #On recupere la derniere cellule de notre Grille
    c = [cel] # Création d'un Tableau avec comme premier élement la derniere cellule 
    while cel != (1, 1): # Tant que la cellule courante est differente de la premiere cellule (1,1)
        c.append(P[cel]) # On ajoute le prédecesseur de la cellule courante dans notre tableau c 
        cel = P[cel] # On actualise la cellule courante avec le predecesseur de l'ancienne cellule
    c.reverse() # On retourne la liste inverse car elle contient la liste du chemins dans le sens inverse (de predecesseur en predecesseur)
    return c, cout # On retourne la liste du chemin optimal ainsi que le cout 
