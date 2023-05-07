########################################################
################## Nom : TetWish #######################
######### Auteurs: Henri SU, Vidjay VELAYOUDAM #########
################## Fonction : Jeu ######################
########################################################

############################# fonction permettant de voir si nous pouvons enlever la ligne ##############################
def row_state(grid,i):              
    for valeur in grid[i]:      # i va être plus tard les indices de chaque lignes pour vérifier s'il y a une ligne pleine
        if valeur==1:
            return False
    return True

############################# fonction permettant de voir si nous pouvons enlever la colonne ##############################
def col_state(grid,j):
    for i in grid:              # j va être plus tard les indices de chaque colonnes pour vérifier s'il y a une colonne pleine
        if i[j]==1:
            return False
    return True

############################# fonction permettant de clear une ligne et faire descendre les blocs au-dessus de la ligne #############################
def row_clear(grid, i):
    if i >= 0:          
        for col in range(len(grid[0])):
            if grid[i][col] != 0:
                grid[i][col] = 1       # on remplace tous les blocs par des 1 et on ne touche pas aux 0 
                for lig in range(i+1):      # permet de faire descendre de une ligne vers le bas tous les blocs ( 2 ) au-dessus de a ligne et remplace à leurs positions initiales des 1
                    if grid[i - lig][col] == 2:
                        grid[i - lig][col] = 1
                        grid[i - lig + 1][col] = 2

########################### fonction permettant de clear une colonne ##################################
def col_clear(grid,j):
    if j >= 0:
        for e in grid:
            if e[j]!=0:         # on remplace tous les blocs par des 1 et on ne touche pas aux 0 
                e[j]=1
