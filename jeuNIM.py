import random as r
import math as m
def newgame():
    global nomJ1
    global nomJ2
    global Score1
    global Score2
    global meilleurScore1
    global meilleurScore2
    
    
    nomJ1,nomJ2=("inserer","inserer")
    Score1,Score2,meilleurScore1,meilleurScore2=0,0,0,0
    joueur1=input("saisissez le nom du 1er joueur: ")
    joueur2=input("saisissez le nom du 2eme joueur: ")
    with open("load.txt",'r') as save:
        for ligne in save:
            if ligne.split(':')[0]==joueur1:
                nomJ1,Score1,meilleurScore1=ligne.strip('\n').split(':')
                
            if ligne.split(':')[0]==joueur2:
                nomJ2,Score2,meilleurScore2=ligne.strip('\n').split(':')
                
    if nomJ1=="inserer":
        nomJ1=joueur1
    if nomJ2=="inserer":
        nomJ2=joueur2
def TAS():
    return [r.randrange(5,24) for i in range(r.randrange(3,8))]
def calculeScore(tour):
    s=0
    for i in range(m.ceil(tour/2)): 
        s+=i*(10**i)
    return s
    
def Top10():
    print("Top 10:")
    List=[]
    index=0
    listrange=0
  
    with open("load.txt",'r') as save:
        for best in save:
            List.append([best.strip('\n').split(':')[0],best.strip('\n').split(':')[2]])
    if len(List) <10:
        listrange=len(List)
    else:
        listrange=10
    for l in range(listrange):
        index=0
        smax=int(List[0][1])
        for i in range(len(List)):
            if int(List[i][1])>smax:
                smax=int(List[i][1])
                index=i 
        print(l+1,".",List[index][0],":",smax)
        List.remove(List[index])
    
def affichage(tas):
    chaine=""
    for i in range(len(tas)):
        chaine+=str(i+1)+"|"
        for piece in range(tas[i]):
            chaine+="*"
        for espace in range(23-tas[i]):
            chaine+=" "
        print(chaine,"| ",tas[i])
        chaine=""
def nbrPieceTotal(tas):
    total=0
    for i in tas:
        total+=i
    return total
def NIM():
    tas=TAS()
    newgame()
    print("Joueur1:",nomJ1,"| ancien score:",Score1,"| Meilleur Score:",meilleurScore1)
    print("Joueur2:",nomJ2,"| ancien score:",Score2,"| Meilleur Score:",meilleurScore2)
    tour=1
    while True:
        if tour%2==0:
            print("Au tour de",nomJ2)
        else:
            print("Au tour de",nomJ1)
        
        affichage(tas)
        print("Choisissez un tas: ")
        numTas=int(input())
        print("Choisissez un nombre de pieces: ")
        nbrPiece=int(input())
        try:
            if tas[numTas-1] or tas[numTas-1]<=0:
                if nbrPiece<=23 and nbrPiece>0:
                    if nbrPieceTotal(tas)-nbrPiece <1:
                        score=calculeScore(tour)
                        f = open("load.txt","r")
                        lignes = f.readlines()
                        f.close()
                        if tour%2==0:
                            print(nomJ1," EST LE GAGNANT !!! SCORE:",score)
                            
                            with open("load.txt",'w') as save:
                                    for ligne in lignes:
                                        if ligne.split(':')[0]==nomJ1:
                                            pass
                                        else:
                                            save.write(ligne)
                            with open("load.txt",'a') as save:
                                
                                if score>int(meilleurScore1):
                                    save.write("{}:{}:{}\n".format(nomJ1,score,score))
                                else:
                                    save.write("{}:{}:{}\n".format(nomJ1,score,meilleurScore1))

                        else:
                            print(nomJ2," EST LE GAGNANT !!! SCORE:",score)
                            with open("load.txt",'w') as save:
                                    for ligne in lignes:
                                        if ligne.split(':')[0]==nomJ2:
                                            pass
                                        else:
                                            save.write(ligne)
                            with open("load.txt",'a') as save:
                                if score>int(meilleurScore1):
                                    save.write("{}:{}:{}\n".format(nomJ2,score,score))
                                else:
                                    save.write("{}:{}:{}\n".format(nomJ2,score,meilleurScore2))
                        print("Game Over!")
                        Top10()
                        break  
                
                    if tas[numTas-1]-nbrPiece >=0:
                        tas[numTas-1]-=nbrPiece
                        tour+=1
                else:
                    print("Choix invalide")
            else:
                print("Choix du tas invalide")
        except:
            print("Erreur!! veuillez réessayer!")
    nouvPartie=input("Commencer une nouvelle partie? oui/non  ")
    if nouvPartie=="oui":
        NIM()
    else:
        print("FIN DU JEU")
       
NIM()
