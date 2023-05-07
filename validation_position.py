########################################################
################## Nom : TetWish #######################
######### Auteurs: Henri SU, Vidjay VELAYOUDAM #########
################## Fonction : Jeu ######################
########################################################

############################### fonction pour voir si nous pouvons mettre le bloc ############################

def valid_position(grid, bloc, ligne, col):
    ligne = ord(ligne)-97   # changer les lettres majuscules et minuscules en nombre
    col = ord(col)-65
    for i in range(4,-1,-1): # car bloc est une matrice de 5x5
        for j in range (5):
            if bloc[4-i][j]==1:     # nous allons nous intéresser seulement dans les cas où le bloc correspondant possède un 1
                if grid[ligne-i][col+j]==2 or grid[ligne-i][col+j]==0:
                    return False
    return True

################################## fonction pour mettre dans la grille ###################################
def emplace_bloc(grid, bloc, i, j):
    i2 = ord(i)-97          # changer les lettres majuscules et minuscules en nombre
    j2 = ord(j)-65
    for ii in range(len(bloc)):
        for jj in range(len(bloc[0])):
            if bloc[(len(bloc)-1)-jj][ii]==1:                # nous allons juste regarder que lorsque le bloc possède un 1 nous allons le placer à l'endroit de la grille - la position 
                grid[i2-jj][j2+ii]=2                         #du bloc car nous commençons de en bas à gauche pour remonter