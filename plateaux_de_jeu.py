########################################################
################## Nom : TetWish #######################
######### Auteurs: Henri SU, Vidjay VELAYOUDAM #########
################## Fonction : Jeu ######################
########################################################


###############################fonction afin read la grille du txt ############################
def read_grid(path1):
    with open(path1, "r") as f1:
        grille = f1.readlines()

    liste = [[] for i in range(len(grille))]
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] != " " and grille[i][j] != "\n":
                liste[i].append(int(grille[i][j]))
    return liste




############################### fonction afin de sauvegarder la nouvelle grille dans le fichier .txt ############################
def save_grid(path, grid):
    ligne = ""
    for e in grid:
        for ee in e:
            ligne += str(ee) + " "
        ligne += "\n"
    with open(path, "w") as f1:
        f1.write(ligne)
    return ligne


############################### fonction pour afficher la grille ############################

def print_grid(grid):
    ligne = "   "  # on a mis 3 espaces car il y a un espace de 3 entre le A et le a
    if len(grid[-1]) == len(grid):  # on vérifie si on a affaire à un losange ou un triangle ou autre
        for i in range(len(grid)):
            ligne += str(chr(65 + i)) + " "  # afin de mettre les lettres en majuscules et un espace
        ligne += "\n"  # sauter la ligne pour que les "=" et les lettres ne soient pas à la même ligne
        ligne += " ┌ "
        for ii in range(len(grid)):
            ligne += "= "
        ligne += "˥\n"
        for e in range(len(grid)):
            ligne += str(chr(97 + e)) + "| "  # mettre tout d'abord le miniscule puis le |
            for ee in range(len(grid[e])):      # permet de créer un grille esthétique avec des blancs si ce n'est pas dans le plateau de jeu, des points si c'est une case vide et un carré s'il y a un bloc 
                if grid[e][ee] == 0:
                    ligne += "  "
                elif grid[e][ee] == 1:
                    ligne += ". "
                elif grid[e][ee] == 2:
                    ligne += "■ "
            ligne += "|\n"
        ligne += " L "                        # permet de fermer la grille de jeu et le rendre plus esthétique
        for ii in range(len(grid)):
            ligne += "= "
        ligne += "˩"
        print(ligne)
    else:                                      #même principe que au-dessus mais nous allons le multiplier par 2 car c'est un triangle donc la longueur du triangle sera deux fois plus petite 
        for i in range(len(grid) * 2 - 1):
            ligne += str(chr(65 + i)) + " "
        ligne += "\n"
        ligne += " ┌ "
        for ii in range(len(grid) * 2 - 1):
            ligne += "= "
        ligne += "˥\n"
        for e in range(len(grid)):
            ligne += str(chr(97 + e)) + "| "
            for ee in range(len(grid[e])):
                if grid[e][ee] == 0:
                    ligne += "  "
                elif grid[e][ee] == 1:
                    ligne += ". "
                elif grid[e][ee] == 2:
                    ligne += "■ "
            ligne += " | \n"
        ligne += " L "
        for ii in range(len(grid) * 2 - 1):
            ligne += "= "
        ligne += "˩"
        print(ligne)
