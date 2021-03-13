import Grille as grl
import random

class puissance4:

    def __init__(self):
        self.grille = None
        self.vainqueur = 0
        self.mode = 1

    def debut(self):
        mode = int(input("Entrez votre mode de jeu, Tapez 1 pour Humain Vs Humain, 2 pour Humain VS Ordi et 3 pour Ordi Vs Ordi : "))
        if mode<=2 :
            self.mode = mode
            hauteur = int(input("Entrez hauteur : "))

            while hauteur < 4 or type(hauteur) != int :
                hauteur = int(input("Mauvaise valeure, choisir une hauteur supérieure à 4 : "))
            
            largeur = int(input("Entrez largeur : "))
            while largeur < 4 or type(largeur) != int :
                largeur = int(input("Mauvaise valeure, choisir une largeur supérieure à 4 : "))
        
        else :
            self.mode=mode
            largeur=hauteur=6

        self.grille = grl.Grille(hauteur, largeur)
        self.partie()

    def partie(self):
        if self.mode == 1 : #Humain Vs Humain
            joueur = 1
            continuer = True
            while( continuer ):
                self.grille.affichage()

                colonne = int(input("Joueur "+str(joueur)+" entrez votre prochain coup"))
                valide = self.grille.coup(joueur, colonne)
                while(valide != 0):
                    if valide == 1:
                        print("Mauvaise valeure")
                    if valide == 2:
                        print("Colonne pleine")
                    colonne = int(input("Joueur "+str(joueur)+" rejouez votre coup"))
                    valide = self.grille.coup(joueur, colonne)

                if self.grille.test_rempli() :
                    continuer = False
                elif self.grille.test_fin() :
                    self.vainqueur = joueur
                    continuer = False

                joueur = joueur % 2 + 1

            self.fin()

        elif self.mode == 2 : #Humain Vs Ordi
            joueur = 1
            continuer = True
            while( continuer ):
                self.grille.affichage()
                
                if joueur==1 : #Humain
                    colonne = int(input("Joueur "+str(joueur)+" entrez votre prochain coup"))
                    valide = self.grille.coup(joueur, colonne)
                    while(valide != 0):
                        if valide == 1:
                            print("Mauvaise valeure")
                        if valide == 2:
                            print("Colonne pleine")
                        colonne = int(input("Joueur "+str(joueur)+" rejouez votre coup"))
                        valide = self.grille.coup(joueur, colonne)

                    if self.grille.test_rempli() :
                        continuer = False
                    elif self.grille.test_fin() :
                        self.vainqueur = joueur
                        continuer = False
                else : # Ordi
                    colonne = random.randint(0,self.grille.longueur - 1)
                    print("ordinateur a joué la colonne {0}:".format(colonne))
                    valide = self.grille.coup(joueur, colonne)
                    while(valide != 0):
                        if valide == 1:
                            print("Mauvaise valeure")
                        if valide == 2:
                            print("Colonne pleine")
                        colonne = random.randint(0,self.grille.longueur - 1)
                        print("ordinateur a rejoué la colonne {0}:".format(colonne))
                        valide = self.grille.coup(joueur, colonne)

                    if self.grille.test_rempli() :
                        continuer = False
                    elif self.grille.test_fin() :
                        self.vainqueur = joueur
                        continuer = False

                joueur = joueur % 2 + 1

            self.fin()

        else : #Ordi Vs Ordi
            joueur = 1
            continuer = True
            while( continuer ):
                self.grille.affichage()

                colonne = random.randint(0,self.grille.longueur - 1)
                print("ordinateur {0} a joué la colonne {1}:".format(joueur,colonne))
                valide = self.grille.coup(joueur, colonne)
                while(valide != 0):
                    if valide == 1:
                        print("Mauvaise valeure")
                    if valide == 2:
                        print("Colonne pleine")
                    colonne = random.randint(0,self.grille.longueur - 1)
                    print("ordinateur {0} a rejoué la colonne {1}:".format(joueur,colonne))
                    valide = self.grille.coup(joueur, colonne)

                if self.grille.test_rempli() :
                    continuer = False
                elif self.grille.test_fin() :
                    self.vainqueur = joueur
                    continuer = False

                joueur = joueur % 2 + 1

            self.fin()

    def fin(self):
        if self.vainqueur == 0:
            print("Match nul")
        else:
            if self.mode == 1:
                print("Joueur " + str(self.vainqueur) +" a gagné !")
            elif self.mode == 2:
                if self.vainqueur ==1:
                    print("Joueur " + str(self.vainqueur) +" a gagné !")
                else :
                    print("ordinateur a gagné !")
            else :
                print("ordinateur " + str(self.vainqueur) +" a gagné !")
            
jeu = puissance4()
jeu.debut()