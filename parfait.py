from math import *
#construction des combinaisons possibles
def combinaison(liste):
    p = []
    i, imax = 1, 2**len(liste)-1
    while i <= imax:
        s = []
        j, jmax = 0, len(liste)-1
        while j <= jmax:
            if (i>>j)&1 == 1:
                s.append(liste[j])
            j += 1
        p.append(s)
        i += 1 
    return p       
#insertion des valeurs de l'intervalle
print('donnez la valeur de a')
a=int(input())
print('donnez la valeur de b')
b=int(input())
#construction de la liste des entiers compris entre a et b
liste=[]
while a <= b:
    liste.append(a)
    a=a+1

p=combinaison(liste)
c=0
for i in range (len(p)):
    m=1
    for j in range (len(p[i])):
        m=m*p[i][j]
    if sqrt(m)== int(sqrt(m)):#verifier si le produit des elements est un nbr parfait
       
        c=c+1
print("C(a,b)=",c)

