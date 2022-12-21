import turtle as t
import Grille



#exemple
grille = {
    (1, 1): {'g': [(1, 1), 4], 'h': [(1, 1), 4], 'd': [(1, 2), 5], 'b': [(2, 1), 2]},
    (1, 2): {'g': [(1, 1), 2], 'h': [(1, 2), 1], 'd': [(1, 3), 5], 'b': [(2, 2), 2]}, 
    (1, 3): {'g': [(1, 2), 1], 'h': [(1, 3), 4], 'd': [(1, 4), 2], 'b': [(2, 3), 5]}, 
    (1, 4): {'g': [(1, 3), 5], 'h': [(1, 4), 3], 'd': [(1, 4), 1], 'b': [(2, 4), 5]}, 
    (2, 1): {'g': [(2, 1), 1], 'h': [(1, 1), 1], 'd': [(2, 2), 3], 'b': [(3, 1), 3]}, 
    (2, 2): {'g': [(2, 1), 4], 'h': [(1, 2), 2], 'd': [(2, 3), 1], 'b': [(3, 2), 3]}, 
    (2, 3): {'g': [(2, 2), 2], 'h': [(1, 3), 1], 'd': [(2, 4), 4], 'b': [(3, 3), 4]}, 
    (2, 4): {'g': [(2, 3), 5], 'h': [(1, 4), 3], 'd': [(2, 4), 5], 'b': [(3, 4), 1]}, 
    (3, 1): {'g': [(3, 1), 5], 'h': [(2, 1), 4], 'd': [(3, 2), 3], 'b': [(3, 1), 5]}, 
    (3, 2): {'g': [(3, 1), 2], 'h': [(2, 2), 2], 'd': [(3, 3), 1], 'b': [(3, 2), 3]}, 
    (3, 3): {'g': [(3, 2), 3], 'h': [(2, 3), 4], 'd': [(3, 4), 1], 'b': [(3, 3), 2]}, 
    (3, 4): {'g': [(3, 3), 2], 'h': [(2, 4), 5], 'd': [(3, 4), 3], 'b': [(3, 4), 5]}
}

#pos commence de (1, 1) et correspand à la position de la tortue à l'instant t
def ep_mur(grille, pos, dir, n, m):
    '''fonction qui prend en paramètre une grille, la position de la tortue et la direction : horizontale ou verticale, 
    et retourne l'épaisseur du mur à dessiner'''
    if dir == 'h':
        if pos[0] == n+1:
            return grille[(n, pos[1])]['b'][1]
        else:
            return grille[pos]['h'][1]
    elif dir == 'v':
        if pos[1] == m+1:
            return grille[(pos[0], m)]['b'][1]
        else:
            return grille[pos]['g'][1]

def colorer_mur(ep):
    if ep == 1:
        t.color("red")
    elif ep == 2:
        t.color("lime")
    elif ep == 3:
        t.color("skyblue")
    elif ep == 4:
        t.color("blue")
    elif ep == 5:
        t.color("yellow")









    
def ajoute_coor(n, m, pas):
    t.color("red")
    t.up()
    t.goto(-300 + pas/2, 300 - pas/2)
    t.left(90)
    for l in range(1, n+1):
        for c in range(1, m+1):
            pos = "(" + str(l) + "," + str(c) + ")"
            t.write(pos , move=False,align='center',font=('Arial',8,'bold'))
            t.forward(pas)
        t.backward((m)*pas)
        t.right(90)
        t.forward(pas)
        t.left(90)















def ajoute_coor(n, m, pas):
    t.color("red")
    t.up()
    t.goto(-300 + pas/2, 300 - pas/2)
    t.left(90)
    for l in range(1, n+1):
        for c in range(1, m+1):
            pos = "(" + str(l) + "," + str(c) + ")"
            t.write(pos , move=False,align='center',font=('Arial',8,'bold'))
            t.forward(pas)
        t.backward((m)*pas)
        t.right(90)
        t.forward(pas)
        t.left(90)






def dessiner_grille(n, m, pas):
    grille = Grille.creer_grille(n, m)
    #dessiner les murs horizontaux
    for l in range(1, n+2):
        for c in range(1, m+1):
            ep = ep_mur(grille, (l, c), 'h', n, m)
            colorer_mur(ep)
            t.width(6 + (ep-1)*4)
            t.forward(pas)
        t.up()
        t.backward(m*pas)
        t.right(90)
        t.forward(pas)
        t.left(90)
        t.down()

    t.up()
    t.right(90)
    t.backward((n+1)*pas)
    t.down()

    for c in range(1, m+2):
        for l in range(1, n+1):
            ep = ep_mur(grille, (l, c), 'v', n, m)
            colorer_mur(ep)
            t.width(6 + (ep-1)*4)
            t.forward(pas)
        t.up()
        t.backward(n*pas)
        t.left(90)
        t.forward(pas)
        t.right(90)
        t.down()

    ajoute_coor(n, m, pas)
    t.color("white")
    t.up()
    ajoute_coor(n, m, pas)



#____________partie_tests___________________
# print( ep_mur(grille, (1, 5), 'v', 3, 4) )
# ajoute_coor(3, 4, 70)
dessiner_grille(7, 7, 70)
#______________end_tests___________________

t.color("white")
t.up()
t.done()