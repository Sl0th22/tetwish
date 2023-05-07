########################################################
################## Nom : TetWish #######################
######### Auteurs: Henri SU, Vidjay VELAYOUDAM #########
################## Fonction : Jeu ######################
########################################################


regles = "Le SP Game est un jeu qui se rapproche du célèbre Tetris mais qui n’en est pas réellement un. \n" \
         "Pour jouer,il suffit de sélectionner un plateau de jeu parmi les trois disponibles : Triangle, Losange ou Cercle.\n" \
         "Ensuite, choisissez la taille de votre plateau de jeu (minimum 21x21, maximum 26x26). \n" \
         "Vous pourrez alors commencer à jouer :\n" \
         "Vous avez le choix entre trois blocs à placer, sélectionnés au hasard :\n" \
         "choisissez-en un parmi ces trois, et entrez les coordonnées auxquelles vous souhaitez placer ce dernier :\n" \
         "Attention, le bloc ne peut être placé que s’il rentre entièrement dans la grille aux coordonnées saisies.\n" \
         "Si vous choisissez un bloc trop grand ou que les coordonnées saisies ne permettent pas de placer le bloc, \n" \
         "la partie s’arrête au bout de trois tentatives, et c’est un Game Over. \n" \
         "Lorsque vous arrivez à remplir entièrement une ligne ou une colonne, cette dernière est éliminée \n" \
         "et les blocs présents au-dessus descendent d’un cran, ou dans le cas d’une colonne, cette colonne \n" \
         "disparait complètement. Le but du jeu est de placer des blocs et d’éliminer des lignes et des colonnes \n"\
         " afin de continuer à placer ces blocs et d’augmenter ainsi votre score, le tout sans dépasser la dernière ligne.\n" \
         "Si vous ne pouvez placer aucun des blocs proposés aléatoirement, Game Over ! Bonne chance !"