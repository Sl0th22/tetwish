########################################################
################## Nom : TetWish #######################
######### Auteurs: Henri SU, Vidjay VELAYOUDAM #########
################## Fonction : Jeu ######################
########################################################



########################### Les imports #############################
import time                                                          #importation des modules et des fichiers nécessaires pour faire fonctionner le jeu
from regles import regles
from colored import fg
from pyfiglet import figlet_format as fig
import os
from map1 import *
from blocs import *
from verification_clear import *
from validation_position import *
from plateaux_de_jeu import *

#####################################################################


def test():                                                          #fonction principale qui fait tourner le jeu et réunissant les autres fonctions
    score = 0
    a = str(input("A: losange    B:triangle    C:cercle : "))        #choix de la forme
    while a.upper() != "A" and a.upper() != "B" and a.upper() != "C":
        a = str(input("A: losange    B:triangle    C:cercle : "))
    os.system('cls')                                                 #commande permettant d'effacer la console
    if a.upper() == "A":
        path = "losange"
        b=losange()
    elif a.upper() == "B":
        path = "triangle"
        b=triangle()
    else:
        path = "cercle"
        b=cercle()
    os.system('cls')
    compteur = 0
    grille = read_grid(b)
    choix = int(input("Souhaitez vous voir la liste des blocs disponibles pour ce plateau de jeu ? Tapez 1 si oui, 2 si non."))
    if choix == 1:
        print_bloc(path)
    continuer=int(input("Mettez 1 pour continuer et jouer : "))
    while continuer!= 1:
        continuer = int(input("Mettez 1 pour continuer et jouer : "))
    else:                                                           #si le joueur souhaite jouer directement, on passe l'étapes des règles et on arrive directement ici
        print_grid(grille)
        while compteur < 2:                                        #tant que le joueur ne fait pas trois tentatives invalides successives, le jeu continue
            print("===============")
            print("SCORE : ", score)
            print("===============")
            c = select_bloc(b)

            tourner = str(input("Voulez-vous tourner le bloc ? 1. Oui      2. Non  : "))        
            while tourner != str(1) and tourner != str(2):
                tourner = str(input("Voulez-vous tourner le bloc ? 1. Oui      2. Non  : "))
            if tourner == str(1):
                tourner2=str(input("1. Gauche        2. Droite  :  " ))
                while tourner2 != str(1) and tourner2 != str(2):
                    tourner2=str(input("1. Gauche        2. Droite  :  " ))
                if tourner2 == str(1):
                    dir=True                                       # pour tourner dans le sens horaire
                else:
                    dir=False                                      # pour tourner dans le sens anti-horaire
                c=rotate_bloc(c,dir)                               # rotate_bloc(c,dir) return une liste


            boole=False
            i = str(input("Donner la ligne à laquelle vous souhaitez placer le bloc : "))    
            while boole==False:
                if (len(i)!=1) or  (97 > ord(i) or 123 < ord(i)) or (ord(i)-97 > len(grille)-1 or ord(i)-97<0):     # pour éviter les problèmes avec plus de 1 de long, éviter de choisir une lettre au-delà de la grille 
                    i=str(input("Donner la ligne à laquelle vous souhaitez placer le bloc : "))
                else:
                    boole=True

            boole2=False
            j = str(input("Donner la colonne à laquelle vous souhaitez placer le bloc : "))
            while boole2==False:
                if (len(j)!=1) or (65 > ord(j) or ord(j) > 91) or (ord(j)-65 > len(grille[0])-1) :
                    j = str(input("Donner la colonne à laquelle vous souhaitez placer le bloc : "))
                else:
                    boole2=True

            while valid_position(grille,c,i,j)!=True and compteur<2:
                print("Nombre d'essais : ",compteur+1)                          #on ajoute un au compteur d'échecs si le joueur rate sa tentative.
                print("Sélectionnez un emplacement valide")
                compteur += 1

                boole=False
                i = str(input("Donner la ligne à laquelle vous souhaitez placer le bloc : "))
                while boole==False:
                    if (len(i)!=1) or  (97 > ord(i) or 123 < ord(i)) or (ord(i)-97 > len(grille)-1 or ord(i)-97<0):
                        i=str(input("Donner la ligne à laquelle vous souhaitez placer le bloc : "))
                    else:
                        boole=True

                boole2=False
                j = str(input("Donner la colonne à laquelle vous souhaitez placer le bloc : "))
                while boole2==False:
                    if (len(j)!=1) or (65 > ord(j) or ord(j) > 91) or (ord(j)-65 > len(grille[0])-1) :
                        j = str(input("Donner la colonne à laquelle vous souhaitez placer le bloc : "))
                    else:
                        boole2=True

            if valid_position(grille, c, i, j):
                emplace_bloc(grille, c, i, j)                                                   #si la position est valide, on place le bloc dans la grille
                os.system('cls')
                compteur = 0
            for verif_lig in range(len(grille)):                                                #enlever une ligne ou une colonne si elle est pleine
                if row_state(grille,verif_lig):                                              
                   row_clear(grille,verif_lig)
                   score += 10

            for verif_col in range(len(grille[0])):
                if col_state(grille,verif_col):
                    col_clear(grille,verif_col)
                    score+=10
            os.system('cls')
            save_grid(path + ".txt", grille)                                                    #mettre à jour la grille à la fin de chaque tour
            print_grid(read_grid(path+".txt"))
        else:
            color = fg('black')
            title = color + fig('                                           GAME OVER')
            print(title)
            print()
            print(" Votre score final est de : ",score)
            time.sleep(1)
            print()
            replay = str(input("Souhaitez vous rejouer ? Tapez 1 si oui, 2 si non : "))
            while replay != str(1) and replay != str(2)  :
                replay = str(input("Merci d'entrer soit 1 pour rejouer, soit 2 pour quitter : "))
            if replay == str(1) :
                test()
            elif replay == str(2) :
                os.system('cls')
                color = fg('black')
                title = color + fig('                                           A BIENTOT !')
                print(title)
                time.sleep(2)
                os.system('cls')
                exit()





############################### Bienvenue et menu du jeu ############################

color, color2 = fg('light_goldenrod_2a'), fg('blue')
title = color + fig('                                           TET') + color2 + fig('                                      WISH')
print(title)

'''print(color + "                              --------------------------------------------                            ", "\n")
print("                                       Bienvenue sur le Tetwish !                                      ", "\n")
print("                              --------------------------------------------                             ", "\n")'''

color = fg('white')
time.sleep(2)
print(color + "                                                Bonjour !", "\n")
time.sleep(2)
print("         Bienvenue sur le Tetwish. Souhaitez vous voir les règles ou commencer directement à jouer ?", "\n")
time.sleep(2)
choix = str(input("             1 :Lire les règles                   2 : Jouer                   3 : Quitter \n"))
time.sleep(2)

while choix != str(1) and choix != str(2) and choix != str(3) :
      choix = str(input("             1 :Lire les règles                   2 : Jouer                   3 : Quitter \n"))

if choix == str(1) :                                                         #choix 1 : règles, choix 2 :jouer et choix 3 : quitter
    print(regles)
    print()
    a=str(input("tapez 1 pour continuer : "))                           # nous le mettons en str pour éviter une erreur si nous mettons des lettres 
    while a!=str(1):
        a=str(input("tapez 1 pour continuer : "))
    os.system('cls')
    test()

elif choix == str(2) :
    os.system('cls')
    test()


else:
    os.system('cls')
    color = fg('black')
    title = color + fig('                                           A BIENTOT ! ')
    print(title)
    time.sleep(2)
    os.system('cls')
    exit()


