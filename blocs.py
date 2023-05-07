########################################################
################## Nom : TetWish #######################
######### Auteurs: Henri SU, Vidjay VELAYOUDAM #########
################## Fonction : Jeu ######################
########################################################

from random import randint
import numpy 

######################################### liste complète de tous les blocs possibles ###################################################

block = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]],
         [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 1, 1, 1, 0]],
         [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]],
         [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]],
         [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 1, 1, 1, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0]],
         [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]],
         [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0]],
         [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0]],
         [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0]]]

########################################### indices des blocs de chaque grilles ################################################
dico = {"cercle": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31],
        "losange": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 32, 33, 34, 35, 36, 37, 38,
                    39,
                    40, 41, 42, 43, 44, 45],
        "triangle": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 46, 47, 48, 49, 50, 51, 52,
                     53, 54, 55, 56]}



############################### fonction afin de print tous les blocs pour la grille de notre choix ############################

def print_bloc(b):                      
    for e in dico[b]:               # e va être le bloc entier 
        for i in range(5):         # i correspond ici aux lignes
            for j in range(5):      # j correspond ici aux colonnes

                if block[e][i][j] == 0:     # permet d'afficher chaque bloc de façon plus esthétique
                    print("  ", end=" ")
                elif block[e][i][j] == 1:
                    print("■ ", end=" ")
                else:
                    print("", end=" ")
            print()
        print()


############################### fonctions afin de choisir le bloc aléatoire ############################


def affichage_ligne(ligne):              # fonction permettant d'afficher le bloc correspondant de manière plus esthétique
    r = ""
    for i in range(len(ligne)):
        if ligne[i] == 1:
            r += "■ "
        else:
            r += ". "
    return r
    
def select_bloc(n):                      # fonction permettant de choisir 3 blocs selon la grille et return le bloc choisit entre les 3 par l'utilisateur
    if n == "losange.txt":                    # dans le cas où la grille est un losange nous allons prendre des indices correspondant à des nombres  ( qui correspondent aux indices de blocs ) du dico de losange
        a = randint(0, 56)
        while (19 < a < 31) or 39 < a:
            a = randint(0, 55)

        b = randint(0, 56)
        while (19 < b < 31) or 39 < b:
            b = randint(0, 55)

        c = randint(0, 56)
        while 19 < c < 31 or 39 < c:
            c = randint(0, 55)

    if n == "cercle.txt":                   # dans le cas où la grille est un cercle nous allons prendre des indices correspondant à des nombres ( qui correspondent aux indices de blocs ) du dico de cercle
        a = randint(0, 56)
        while a > 31:
            a = randint(0, 56)

        b = randint(0, 56)
        while b > 31:
            b = randint(0, 56)

        c = randint(0, 56)
        while c > 31:
            c = randint(0, 56)

    if n == "triangle.txt":                 # dans le cas où la grille est un triangle nous allons prendre des indices correspondant à des nombres ( qui correspondent aux indices de blocs ) du dico de triangle
        a = randint(0, 56)
        while 19 < a < 46:
            a = randint(0, 56)

        b = randint(0, 56)
        while 19 < b < 46:
            b = randint(0, 56)

        c = randint(0, 56)
        while 19 < c < 46:
            c = randint(0, 56)

    print("BLOC A :       BLOC B :      BLOC C : ".rjust(150))          # .rjust permet de décaler vers la droite l'affichage
    for i in range(5):
        print(affichage_ligne(block[a][i]).rjust(127), end="     ")     
        print(affichage_ligne(block[b][i]), end="     ")
        print(affichage_ligne(block[c][i]))

    question = str(input("Saisir un soit le Bloc A soit le Bloc B soit le Bloc C : "))
    while question.upper() != "A" and question.upper() != "B" and question.upper() != "C":
        question = str(input("Saisir un soit le Bloc A soit le Bloc B soit le Bloc C : "))
    if question.upper() == "A":
        return block[a]
    elif question.upper() == "B":
        return block[b]
    else:
        return block[c]

################################## rotate les blocs #######################################


def arranger_bloc(bloc):            # fonction qui permet de mettre le bloc en bas à gaucha de la matrice, affiche sa nouvelle forme et return le nouveau bloc
    longueur=list()
    for i in range(5):              # permet de savoir de combien de case il faut déplacer vers la gauche car nous allons prendre ensuite le plus petit écart
        taille = 0
        for j in range(5):
            if bloc[i][j]!=1:           
                taille+=1
            else:
                longueur.append(taille)
        
    hauteur = list()               # permet de savoir de combien de case il faut déplacer vers le bas  car nous allons prendre ensuite le plus petit écart
    for ii in range(5):
        taille = 0
        for jj in range(4,-1,-1):
            if bloc[jj][ii]!=1:
                taille += 1
            else:
                hauteur.append(taille)

    ligne,colonne= min(longueur),min(hauteur) 

    if ligne!=0:
            for lig in range(5):
                for col in range(5):
                    if bloc[lig][col]==1:
                        bloc[lig][col], bloc[lig][col-ligne]  = bloc[lig][col-ligne] , bloc[lig][col]       # on permute la valeur avec la valeur moins l'écart
    if colonne!=0:
            for lig2 in range(4,-1,-1):
                for col2 in range(4,-1,-1):
                    if bloc[lig2][col2]==1:
                        bloc[lig2][col2] , bloc[lig2+colonne][col2]  = bloc[lig2+colonne][col2] , bloc[lig2][col2]  # on permute la valeur avec la valeur du bas moins l'écart

    print("NOUVEAU BLOC : ".rjust(150))             # permet d'afficher avec style le nouveau bloc
    for i in range(5):
        print(affichage_ligne(bloc[i]).rjust(150))
    return bloc


def rotate_bloc(bloc,dir):
    liste2=list()
    if dir == True:    # pour le faire tourner dans le sens horaire
        liste2=numpy.rot90(bloc,-1).tolist()

    else:               # pour le faire tourner dans le sens anti-horaire
        liste2=numpy.rot90(bloc).tolist()
    return arranger_bloc(liste2)

        