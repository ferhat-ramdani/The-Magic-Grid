def minimum(dico):
    m=float('inf')
    for k in dico:
        if dico[k] < m:
            m=dico[k]
            i=k
    return i


def dijkstra(G,s):
    D={} 
    d={k: float('inf') for k in G} 
    d[s]=0 
    P={}
    while len(d)>0: 
        k=minimum(d) 
        for mur in G[k]: 
            cel_v, ep = G[k][mur]
            if cel_v not in D:
                if d[cel_v]>d[k]+ep:
                    d[cel_v]=d[k]+ep
                    P[cel_v]=k
        D[k]=d[k]
        del(d[k])
    return D, P


def bellman_ford(G, s):
    d={k: float('inf') for k in G}  
    P={}
    d[s]=0   
    fini=False
    while not fini:
        fini=True
        for cel in G:
            for mur in G[cel]:
                cel_v, ep = G[cel][mur]  
                if d[cel]+ep < d[cel_v]:
                    d[cel_v] = d[cel]+ep
                    P[cel_v]=cel
                    fini=False
    return d, P


def plus_court_chemin(G, n, m, algo='dij'):
    if algo == 'bel':
        d, P = bellman_ford(G, (1, 1))
    else:
        d, P = dijkstra(G, (1, 1))
    
    cout = d[(n, m)]
    cel = (n, m)
    c = [cel]
    while cel != (1, 1):
        c.append(P[cel])
        cel = P[cel]
    c.reverse()
    return c, cout
