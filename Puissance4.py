import Grille as grl

class puissance4:

    def __init__(self):
        self.grille = None
        self.vainqueur = 0

    def debut(self):
        hauteur = int(input("Entrez hauteur"))

        while(hauteur < 4) and (type(hauteur) != int) :
            hauteur = int(input("Mauvaise valeure, choisir une hauteur supérieure à 4"))
        
        largeur = int(input("Entrez largeur"))
        while(largeur < 4) and (type(largeur) != int) :
            largeur = int(input("Mauvaise valeure, choisir une largeur supérieure à 4"))
            
        self.grille = grl.Grille(hauteur, largeur)
        self.partie()

    def partie(self):
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

    def fin(self):
        if self.vainqueur == 0:
            print("Match nul")
        else:
            print("Joueur " + str(self.vainqueur) +" a gagné !")
            
jeu = puissance4()
jeu.debut()