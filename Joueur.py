class Joueur:
    def __init__(self):
        self.nom

nmax=5
 
def Minimax(n,nmax,J,Grille,x) :
    if n!=1:
        Victoire = victoire (x,J,Grille)
        print('Victoire = ', Victoire,n)
        if Victoire == 1 :
            Victoire = 0
            return(1000)
        if Victoire == -1 :
            Victoire = 0
            return (0)
        if Grille[35]!=0 and Grille[36]!=0 and Grille[37]!=0 and Grille[38]!=0 and Grille[39]!=0 and Grille[40]!=0 and Grille[41]!=0:
            return (500)
    Valeur=[0]*7
    Ordonnée = 0
    J = J*-1
    while Ordonnée<7 :
        y=0
        z=0
        while Grille[Ordonnée+7*y] !=0 and z==0:
            y+=1
            if y==6:
                z=1
                y=0
        if z==1:
            Valeur[Ordonnée]=-1
        else :
            x=Ordonnée + 7 * y
            Grille[x]=J
            if n==nmax:
                Valeur[Ordonnée]=Analyse(x,Grille)
            else:
                n+=1
                Valeur[Ordonnée]=Minimax(n,nmax,J,Grille,x)
                n-=1
            Grille[x]=0
        Ordonnée+=1
    if J==-1:
        x=0
        while Valeur[x]==-1:
            x+=1
        ValeurB=Valeur[x]
        while x<7:
            if Valeur[x]<ValeurB and Valeur[x]!=-1 :
                ValeurB=Valeur[x]
            x+=1
    else :
        x=0
        ValeurB=0
        Best=0
        while x<7:
            if Valeur[x]>ValeurB :
                ValeurB=Valeur[x]
                Best=x
                print('best = ' ,Best,' Valeurb = ',ValeurB)
            x+=1
    print(ValeurB)
    J*=-1
    if n==1:
        print("Best = ",Best)
        return(Best)
    else:
        return(ValeurB)
 
def Analyse(x,Grille) :
    Axe = 1
    Valeur = 0
    while Axe!=5 :
        Alignement = [0]*7
        vuex = x
        if Axe == 1 :
            while vuex%7!=0 :
                vuex-=1
        if Axe == 3 :
            while vuex%7!=0 and vuex>6 :
                vuex-=8
        if Axe == 4 :
            while vuex%7!=6 and vuex>6 :
                vuex-=6
        if Axe == 2 :
            while vuex>6 :
                vuex-=7
        Aide = 0
        Alignement = [0]*7
        while Aide != 7:
            if vuex!=-1 :
                Alignement[Aide]=Grille[vuex]
                if vuex==x:
                    Position = Aide
                if Axe == 1:
                    vuex+=1
                    if vuex%7==0 :
                        vuex=-1
                if Axe == 2:
                    vuex+=7
                    if vuex>41 :
                        vuex=-1
                if Axe == 3:
                    vuex+=8
                    if vuex%7==0 or vuex>41 :
                        vuex=-1
                if Axe == 4:
                    vuex+=6
                    if vuex%7==6 or vuex>41 :
                        vuex=-1
            else :
                Alignement[Aide]=2
            Aide+=1
        Distance1 = -1
        Distance2 = -1
        Lot1=0
        Lot2=0
        Regard=Position
        while Regard >-1 :
            if Alignement[Regard]==-1 or Alignement[Regard]==2:
                Action=7
            if Alignement[Regard]==1:
                    Lot1+=1
                    Action=1
            if Alignement[Regard]==0 and Lot1==0:
                Distance1+=1
                Action=1
            if Alignement[Regard]==0 and Lot1!=0:
                Action=7
            Regard=Regard-Action
        Regard=Position
        while Regard<7 :
            if Alignement[Regard]==-1  or Alignement[Regard]==2:
                Action=7
            if Alignement[Regard]==1:
                    Lot2+=1
                    Action=1
            if Alignement[Regard]==0 and Lot2==0:
                        Distance2+=1
                        Action=1
            if Alignement[Regard]==0 and Lot2!=0:
                Action=7
            Regard = Regard+Action
        if Lot1 == 0 :
            Distance1 = 10
        if Lot2 == 0 :
            Distance2 = 10
        if Distance1==0 and Distance2 ==0 :
            Lot=Lot1+Lot2+1
            Distance=0
        if Distance1==Distance2 and Distance1!=0 :
            if Lot1>Lot2 :
                Distance=Distance1
                Lot=Lot1+1
            else :
                Distance=Distance2
                Lot=Lot2+1
        if Distance1<Distance2 :
            Distance=Distance1
            Lot=Lot1+1
        if Distance1>Distance2 :
            Distance=Distance2
            Lot=Lot2+1
        if Distance ==0:
            Valeur+=20
        if Distance==1:
            Valeur+=10
        if Distance==2:
            Valeur+=30
        if Lot==2 :
            Valeur+=10
        if Lot==3 :
            Valeur+=100
        if Lot>=4 :
            Valeur+=1000
        Regard=Position
        Distance1 = -1
        Distance2 = -1
        Lot1=0
        Lot2=0
        while Regard >-1 :
            if Alignement[Regard]==1 or Alignement[Regard]==2:
                Action=7
            if Alignement[Regard]==-1:
                    Lot1+=1
                    Action=1
            if Alignement[Regard]==0 and Lot1==0:
                Distance1+=1
                Action=1
            if Alignement[Regard]==0 and Lot1!=0:
                Action=7
            Regard=Regard-Action
        Regard=Position
        while Regard<7 :
            if Alignement[Regard]==1 or Alignement[Regard]==2 :
                Action=7
            if Alignement[Regard]==-1:
                    Lot2+=1
                    Action=1
            if Alignement[Regard]==0 and Lot2==0:
                        Distance2+=1
                        Action=1
            if Alignement[Regard]==0 and Lot2!=0:
                            Action=7
            Regard = Regard+Action
        if Lot1 == 0 :
            Distance1 = 10
        if Lot2 == 0 :
            Distance2 = 10
        if Distance1==0 and Distance2 ==0 :
            Lot=Lot1+Lot2+1
            Distance=0
        if Distance1==Distance2 and Distance1!=0 :
            if Lot1>Lot2 :
                Distance=Distance1
                Lot=Lot1+1
            else :
                Distance=Distance2
                Lot=Lot2+1
        if Distance1<Distance2 :
            Distance=Distance1
            Lot=Lot1+1
        if Distance1>Distance2 :
            Distance=Distance2
            Lot=Lot2+1
        if Lot >= 3 :
            Valeur+=500
        if Lot ==2 :
            Valeur+=50
        if Lot == 1 :
            Valeur +=5
        Axe+=1
    if x%7 == 3 :
        Valeur+=3
    if x%7 == 2 or x%7 == 4 :
        Valeur+=2
    if x%7 == 1 or x%7 == 5 :
        Valeur+=1
    return(Valeur)
 
 
 
def Clic(x) :
    #Répétition des touches
        pygame.key.set_repeat(673, 576)
        for event in pygame.event.get(): #Attente des événements
            if event.type == QUIT:
                Victoire = 3
            if event.type == MOUSEBUTTONDOWN:
              if event.button == 1:   #Si clic gauche
                  #On donne à x la valeur
                  x = event.pos[0]
                  y = 0
                  if x >= 577 :
                    y = 1
                    x = 672
                  if x >= 481 :
                    if y == 0 :
                        x = 576
                        y = 1
                  if x >= 385 :
                    if y == 0 :
                        x = 480
                        y = 1
                  if x >= 289 :
                    if y == 0 :
                        x = 384
                        y = 1
                  if x >= 193 :
                    if y == 0 :
                        x = 288
                        y = 1
                  if x >= 97 :
                    if y == 0 :
                        x = 192
                        y = 1
                  if y == 0 :
                        x = 96
                        y = 1
                  x = int(x/96)
        return(x)
 
 
def victoire(x,Tour,Grille) :
    Victoire=0
    #Réussite verticale
    if x >= 21 :
         if Grille[x-7]==Tour and Grille[x-14]==Tour and Grille[x-21]==Tour:
                    Victoire = Tour
    #Réussite horizontale
    vuex = 0
    if x%7!=0 :
        if Grille[x-1] == Tour:
            vuex = vuex + 1
            if x%7!=1 :
                if Grille[x-2] == Tour:
                    vuex = vuex + 1
                    if x%7!=2 :
                        if Grille[x-3] == Tour:
                            vuex = vuex + 1
    if x%7!=6 :
        if Grille[x+1] == Tour:
            vuex = vuex + 1
            if x%7!=5 :
                if Grille[x+2] == Tour:
                    vuex = vuex + 1
                    if x%7!=4 :
                        if Grille[x+3] == Tour:
                            vuex = vuex + 1
    if vuex >= 3 :
        Victoire = Tour
    #Réussite Diagonale Gauche
    vuex = 0
    if x%7!=0 and x>6:
        if Grille[x-8] == Tour:
            vuex = vuex + 1
            if x%7!=1 and x>13:
                if Grille[x-16] == Tour:
                    vuex = vuex + 1
                    if x%7!=2 and x>20:
                        if Grille[x-24] == Tour:
                            vuex = vuex + 1
    if x%7!=6 and x<35:
        if Grille[x+8] == Tour:
            vuex = vuex + 1
            if x%7!=5 and x<28:
                if Grille[x+16] == Tour:
                    vuex = vuex + 1
                    if x%7!=4 and x<21:
                        if Grille[x+24] == Tour:
                            vuex = vuex + 1
    if vuex >= 3 :
        Victoire = Tour
    #Réussite Diagonale Droite
    vuex = 0
    if x%7!=6 and x>6:
        if Grille[x-6] == Tour:
            vuex = vuex + 1
            if x%7!=5 and x>13:
                if Grille[x-12] == Tour:
                    vuex = vuex + 1
                    if x%7!=4 and x>20:
                        if Grille[x-18] == Tour:
                            vuex = vuex + 1
    if x%7!=0 and x<35:
        if Grille[x+6]== Tour:
            vuex = vuex + 1
            if x%7!=1 and x<28:
                if Grille[x+12] == Tour:
                    vuex = vuex + 1
                    if x%7!=2 and x<21:
                        if Grille[x+18] == Tour:
                            vuex = vuex + 1
    if vuex >= 3 :
        Victoire = Tour
    return(Victoire)
 
import pygame
from pygame.locals import *
pygame.init()
fenetre = pygame.display.set_mode((673, 576))
fond = pygame.image.load("F:/Choix.png").convert()
fenetre.blit(fond, (0,0))
font=pygame.font.Font(None, 24)
text = font.render("Voulez-vous jouer en Rouge ?", 1, (255,0,0))
fenetre.blit(text,(50,270))
text = font.render("Voulez-vous jouer en Jaune ?", 1, (255,255,0))
fenetre.blit(text,(390,270))
pygame.display.flip()
x = 0
while x == 0 :
    pygame.key.set_repeat(673, 576)
    for event in pygame.event.get():
            if event.type == QUIT:
                Victoire = 3
            if event.type == MOUSEBUTTONDOWN:
              if event.button == 1:
                  x = event.pos[0]
couleurjoueur = 1
if x >=337 :
    couleurjoueur = 2
fond = pygame.image.load("F:/Choix.png").convert()
fenetre.blit(fond, (0,0))
font=pygame.font.Font(None, 24)
text = font.render("Voulez-vous jouer en premier ?", 1, (255,0,0))
fenetre.blit(text,(50,270))
text = font.render("Voulez-vous jouer en second ?", 1, (255,255,0))
fenetre.blit(text,(390,270))
pygame.display.flip()
x = 0
while x == 0 :
    pygame.key.set_repeat(673, 576)
    for event in pygame.event.get():
            if event.type == QUIT:
                Victoire = 3
            if event.type == MOUSEBUTTONDOWN:
              if event.button == 1:
                  x = event.pos[0]
Tour = -1
if x >=337 :
    Tour = 1
grille = pygame.image.load("F:/grille.png").convert_alpha()
grille.set_colorkey((255,255,255))
rouge = pygame.image.load("F:/pion rouge.png").convert()
rouge.set_colorkey((255,255,255))
jaune = pygame.image.load("F:/pion jaune.png").convert()
jaune.set_colorkey((255,255,255))
x = 0
fenetre.blit(grille, (x, 0))
pygame.display.flip()
Victoire = 0
Cases = 0
x = 0
n=1
Grille = [0]*42
n=0
while Victoire == 0 and Cases != 42:
    if Tour == -1 :
        x = 0
        while x == 0 :
            x = 0
            while x ==0 :
                x = Clic(x)
                if Grille[x+34] != 0 :
                    x = 0
        y = 0
        while Grille[7*y+x-1]!= 0 :
            y = y+1
        print(x,y)
        if couleurjoueur == 1 and Tour == -1 :
           fenetre.blit(rouge,(-87+96*x,488-96*y))
        if couleurjoueur == 1 and Tour == 1 :
            fenetre.blit(jaune,(-87+96*x,488-96*y))
        if couleurjoueur == 2 and Tour == -1 :
            fenetre.blit(jaune,(-87+96*x,488-96*y))
        if couleurjoueur == 2 and Tour == 1 :
            fenetre.blit(rouge,(-87+96*x,488-96*y))
        pygame.display.flip()
        x=7*y+x-1
        Grille[x] = -1
        Cases = Cases + 1
        Victoire = victoire(x,Tour,Grille)
        Tour = 1
    if Tour == 1 and Victoire != -1 and Cases != 42:
    #Choix de l'Ordi
        J = -1
        n=1
        x=0
        x = Minimax(n,nmax,J,Grille,x)
        y = 0
        print(x)
        while Grille[x+7*y]!=0 :
            y+=1
            print(x, y)
        Grille[7*y+x]=1
        Cases = Cases + 1
        x=x+1
        if couleurjoueur == 1 and Tour == -1 :
            fenetre.blit(rouge,(-87+96*x,488-96*y))
        if couleurjoueur == 1 and Tour == 1 :
            fenetre.blit(jaune,(-87+96*x,488-96*y))
        if couleurjoueur == 2 and Tour == -1 :
            fenetre.blit(jaune,(-87+96*x,488-96*y))
        if couleurjoueur == 2 and Tour == 1 :
            fenetre.blit(rouge,(-87+96*x,488-96*y))
        pygame.display.flip()
        x = 7*y+x-1
        Victoire = victoire (x,Tour,Grille)
        Tour = -1
 
if Victoire == 1 :
    print ("Victoire de l'Ordi")
if Victoire == 0 :
    print ("Match nul...")
if Victoire == -1 :
    print("Victoire du Joueur")
pygame.quit()
quit()