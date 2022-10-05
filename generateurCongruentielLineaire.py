from random import *
from matplotlib.pylab import *
from numpy import *
import time

#test
a=137
c=187
m=2**8
z=10
for i in range(50) :
    z=(a*z+c)%m
    print("z(",i+1,")", "=",z)

#première implémentation 
def GCL1(a,c,m,z,nbIter) :
    tab = []
    for i in range(nbIter) :
        z=(a*z+c)%m
        tab.append(z)
    return tab

print(plt.hist(GCL1(137,187,2**8,10,200), bins=8, edgecolor = 'red'))

#deuxième implémentation : U(n) = Z(n)/m
def GCL(z,nbIter=1000,a=16807,c=0,m=2**31-1):
    tab = []
    for i in range(nbIter) :
        z=((a*z+c)%m)
        tab.append(z/m)
    return tab
    
nbIter=1000
a=16807
c=0
m=2**31-1
z=10
print(GCL(z,nbIter,a,c,m)[0:10],'\n') # affiche les 10 premières valeurs
print(GCL(z,nbIter,a,c,m)[-10:]) # affiche les 10 dernières valeurs

#Test de la fonction rand() et d'une fonction alea imitant le comportement de rand.
U=rand(1000)
hist(U,bins=10, range=(0,1))

def alea(n=1):
    return(GCL(int(time.time()))[0:n])
alea()

#TEST DES FONCTIONS
z=20704370
print(GCL(z,nbIter,a,c,m)[-10:])
print(GCL(z,nbIter,a,c,m)[-10:])
z=20704371
print(GCL(z,nbIter,a,c,m)[-10:])
print(GCL(a=25,c=16,m=256,z=50,nbIter=1000))
print(rand())
print("\n")
print(rand(10))
print("\n")
print(rand(10,10))