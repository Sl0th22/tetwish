########################################################
################## Nom : TetWish #######################
######### Auteurs: Henri SU, Vidjay VELAYOUDAM #########
################## Fonction : Jeu ######################
########################################################

############################## fonction pour les formes de grilles ############################

def triangle():                 #nous demandons un nombre impair afin de créer un fichier .txt avec le triangle à l'intérieur et nous allons return le fichier car la fonction read_grid() prend en argument un fichier .txt
    n = int(input("Entrer un nombre impair entre 21 et 26 : "))
    while (n % 2 == 0) or (n < 21 or n > 26):
        n = int(input("Entrer un nombre impair entre 21 et 26 : "))
    n -= 2
    chaine = ""
    cpt = (n - 1) // 2
    for i in range(1, n + 1, 2):
        chaine += "0 " * cpt + "1 " * i + "0 " * cpt + "\n"
        cpt -= 1
    with open("triangle.txt", "w") as f1:
        f1.write(chaine)
    return "triangle.txt"


def losange():                    #nous demandons un nombre impair afin de créer un fichier .txt avec le losange à l'intérieur et nous allons return le fichier car la fonction read_grid() prend en argument un fichier .txt
    n = int(input("Entrer un nombre impair entre 21 et 26 : "))
    while (n % 2 == 0) or (n < 21 or n > 26):
        n = int(input("Entrer un nombre impair entre 21 et 26 : "))
    n -= 2
    chaine = ""
    cpt = (n - 1) // 2
    for i in range(1, n + 1, 2):
        chaine += "0 " * cpt + "1 " * i + "0 " * cpt + "\n"
        cpt -= 1
    cpt = 0
    for j in range(n, 0, -2):
        if j != n:
            chaine += "0 " * cpt + "1 " * j + "0 " * cpt + "\n"
        cpt += 1
    with open("losange.txt", "w") as f2:
        f2.write(chaine)
    return "losange.txt"


def cercle():                     #nous demandons un nombre impair afin de créer un fichier .txt avec le cercle à l'intérieur et nous allons return le fichier car la fonction read_grid() prend en argument un fichier .txt
    n = int(input("Entrer un nombre impair entre 21 et 26 : "))
    while (n % 2 == 0) or (n < 21 or n > 26):
        n = int(input("Entrer un nombre impair entre 21 et 26 : "))
    chaine = ""
    trou = n // 5
    zone = n - (trou * 2)
    trou_reel = trou
    zone_reel = zone
    while trou_reel > 0:
        chaine += trou_reel * "0" + zone_reel * "1" + trou_reel * "0" + "\n"
        trou_reel -= 1
        zone_reel += 2
    for i in range(zone):
        chaine += n * "1" + "\n"
    while trou_reel < trou:
        trou_reel += 1
        zone_reel -= 2
        chaine += trou_reel * "0" + zone_reel * "1" + trou_reel * "0" + "\n"
    with open("cercle.txt", "w") as f1:
        f1.write(chaine)
    return "cercle.txt"