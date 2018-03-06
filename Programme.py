from math import *
import numpy as np
from random import randint
import matplotlib.pyplot as plt 
from copy import deepcopy

## Modification listes

def ajoutAstre(L,r,m,w,alpha,rayon):
    L.append([cos(alpha)*r,sin(alpha)*r,r,m,w,alpha,rayon])
    return(L)

def espace(m,x,y,vx0,vy0):
    return([[m,[x,y,vx0,vy0]]])

## Modélisation

# Gravitation

def attraction(x,y,xa,ya,e,m):
    d=sqrt((x-xa)**2+(y-ya)**2)
    G=6.67*10**(-11) #6.67*10**(-11)
    cos_alpha=(xa-x)/d
    sin_alpha=(ya-y)/d
    xn=e**2*m*cos_alpha/(d**2)*G
    yn=e**2*m*sin_alpha/(d**2)*G
    return(xn,yn)

cste=99000000000000000000
rsoleil=700E6

# Crash

def testcrash(L):
    a=False
    if sqrt((L[0][1][0])**2+(L[0][1][1])**2)<rsoleil:
        L[0][1][0],L[0][1][1]=0,0
        a=True
    else:
        for i in L[1:]:
            if sqrt((L[0][1][0]-i[0])**2+(L[0][1][1]-i[1])**2)<i[6]:
                L[0][1][0],L[0][1][1]=i[0],i[1]
                a=True
                break
    return(a)


# Déplacement

def avance(L,e):
    x,y=L[0][1][0],L[0][1][1]
    if testcrash(L):
        L[0][1][2],L[0][1][3]=0,0
        for i in L[1:]:
            alpha=i[5]
            alpha+=e*i[4]
            i[5]=alpha
            i[0],i[1]=i[2]*cos(alpha),i[2]*sin(alpha)
    else:
        x1,y1=attraction(x,y,0,0,e,L[0][0])
        for i in L[1:]:
            xn,yn=attraction(x,y,i[0],i[1],e,i[3])
            x1,y1=x1+xn,y1+yn
            alpha=i[5]
            alpha+=e*i[4]
            i[5]=alpha
            i[0],i[1]=i[2]*cos(alpha),i[2]*sin(alpha)
        L[0][1]=[x+L[0][1][2]*e+x1,y+L[0][1][3]*e+y1,L[0][1][2]+x1/e,L[0][1][3]+y1/e]

## Affichage
#Instantané

size=1000000 #1000000
axe=1000000000000

def cercle (r):
    A=np.linspace(0,2*pi,1000)
    X,Y=[],[]
    for i in A:
        X.append(r*cos(i))
        Y.append(r*sin(i))
    plt.plot(X,Y,color='grey')
    
def afficheSimple(L):
    plt.xlim(-axe,axe)
    plt.ylim(-axe,axe)
    a=L[0][0]
    plt.plot(0,0,'oy',markersize=20000000/size,zorder=1) #700000000
    plt.plot(L[0][1][0],L[0][1][1],'or',zorder=10)
    for i in L[1:]:
        plt.plot(i[0],i[1],'og',markersize=i[6]/size,zorder=5)
    for i in L[1:]:
        cercle(i[2])
    plt.show()

def affiche2(L):
    plt.xlim(-axe,axe)
    plt.ylim(-axe,axe)
    plt.plot(L[0][1][0],L[0][1][1],'or',zorder=10)
    for i in L[1:]:
        plt.plot(i[0],i[1],'og',markersize=i[6]/size,zorder=5)
    plt.show()

def afficheRef(L,n):
    plt.xlim(-axe/600,axe/600)
    plt.ylim(-axe/600,axe/600)
    plt.plot(L[0][1][0]-L[n][0],L[0][1][1]-L[n][1],'or',zorder=10)
    plt.show()

def deplacementAffichageFinal(L1,e,n):
    L=deepcopy(L1)
    X,Y=[],[]
    for i in range (n):
        avance(L,e)
        X.append(L[0][1][0])
        Y.append(L[0][1][1])
    afficheSimple(L)
    plt.plot(X,Y,color="r")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    for i in L[1:]:
        cercle(i[2])

def Epot (L):
    cte=-6.67*10**(-11)
    S=cte*L[0][0]/(sqrt(L[0][1][0]**2+L[0][1][1]**2))
    for i in L[1:]:
        S+=cte*i[3]/(sqrt((L[0][1][0]-i[0])**2+(L[0][1][1]-i[1])**2))
    return(S)

def MultiplieListe(Liste2,coeff):
    Liste=deepcopy(Liste2)
    for i in range (len(Liste)):
        Liste[i]*=coeff
    return(Liste)

## Réajuste
    
def ecart_obj (x,y,x1,y1,marge_erreur):
    return ( sqrt((x1-x)**2+(y1-y)**2)<marge_erreur )

def trajfinale (L,v_col,v_orth,n,e,vcol,vorth):
    M=deepcopy(L)
    v_col=v_col/n+vcol
    v_orth=v_orth/n+vorth
    for i in range (n):
        vn=sqrt(M[0][1][2]**2+M[0][1][3]**2)
        ajoutvitesse(M,v_col,v_orth,vn)
        avance (M,e)
    return((M[0][1][0],M[0][1][1]))


def reajuste (L,x1,y1,n,m,e,vcol,vorth):
    M=deepcopy(L)
    v=sqrt(M[0][1][2]**2+M[0][1][3]**2)
    vmax=n**3*v/(10*(492*e0//e)**3)
    v_moins,v_plus= -vmax,vmax
    pas1=(v_plus-v_moins)/m
    pas2=(v_plus-v_moins)/(4*m)
    emin,k,l=np.inf,0,0
    for i in range (m):
        for j in range (m):
            x,y=trajfinale(L,v_moins+pas1*i,v_moins/4+pas2*j,n,e,vcol,vorth)
            ecart=sqrt((x1-x)**2+(y1-y)**2)
            if ecart<emin:
                emin=ecart
                k,l=i,j
    return(v_moins+pas1*k,v_moins/4+pas2*l)
  
def Deplace(L1,e,e_assist,n,Obj,Rprime,nb_points):
    L= deepcopy(L1)
    LL,R,n=[],MultiplieListe(Rprime,e0//e),n*e0//e
    Objectif=deepcopy(Obj)
    Objectif[-1]*=e0//e
    vcol,vorth=0,0
    for i in range (int((Obj[2] - 0.25)*e0//e)):
        if i in R:
            v1,v2=reajuste(L,Objectif[0],Objectif[1],Objectif[2]-i,nb_points,e,vcol,vorth)
            v1,v2=v1/(Objectif[2]-i-0.25*e0//e),v2/(Objectif[2]-i-0.25*e0//e)
            vcol+=v1
            vorth+=v2
            print(i*e//e0)
        vn=sqrt(L[0][1][2]**2+L[0][1][3]**2)
        ajoutvitesse(L,vcol,vorth,vn)
        avance(L,e)
        LL.append(deepcopy(L))
    v1,v2=reajuste(L,Objectif[0],Objectif[1],(Objectif[2]-i)*e//e_assist,nb_points,e_assist,vcol,vorth)
    vn=sqrt(L[0][1][2]**2+L[0][1][3]**2)
    ajoutvitesse(L,v1,v2,vn)
    avance(L,e_assist)
    LL.append(deepcopy(L))
    for i in range(int((Obj[2] - 0.25)*e0//e_assist +1),int((Obj[2]+0.25)*e0//e_assist):
        avance(L,e_assist)
        LL.append(deepcopy(L))
    for i in range(int((Obj[2] + 0.25)*e0//e),n):
        avance(L,e)
        LL.append(deepcopy(L))
    return LL

def ajoutvitesse(L,vcol,vorth,vn):
    if vn!= 0 :
        L[0][1][2]+=vcol*L[0][1][2]/vn-vorth*L[0][1][3]/vn
        L[0][1][3]+=vcol*L[0][1][3]/vn+vorth*L[0][1][2]/vn

def vtot(L,vcol,vorth,vn):
    return(sqrt((vcol*L[0][1][2]/vn-vorth*L[0][1][3]/vn)**2+(vcol*L[0][1][3]/vn+vorth*L[0][1][2]/vn)**2))

def DeplaceSansObjectif(LL,e,n):
    L,n=deepcopy(LL[-1]),n*e0//e
    for i in range (n):
        avance(L,e)
        LL.append(deepcopy(L))
    return LL

## Analyse résultats

def courbes(LL,e,e_assist):
    Xc,V,Ep,Ec,Em,t=[],[],[],[],[],0
    for i in LL[:int((792-0.25)*e0//e)+1]: #jusqu'au changement du pas, soit 6 heures avant AG
        t = t + e/e0
        Xc.append(t)
        v=sqrt(i[0][1][2]**2+i[0][1][3]**2)
        V.append(v)
        Ep.append(Epot(i))
        Ec.append(v**2/2)
        Em.append(Epot(i)+v**2/2)
    for i in LL[int((792-0.25)*e0//e)+1:int((792-0.25)*e0//e)+1+int(0.5*e0//e_assist)+1]:
        t = t + e_assist/e0
        Xc.append(t)
        v=sqrt(i[0][1][2]**2+i[0][1][3]**2)
        V.append(v)
        Ep.append(Epot(i))
        Ec.append(v**2/2)
        Em.append(Epot(i)+v**2/2)
    for i in LL[int((792-0.25)*e0//e)+1+int(0.5*e0//e_assist)+1:]:
        t = t + e/e0
        Xc.append(t)
        v=sqrt(i[0][1][2]**2+i[0][1][3]**2)
        V.append(v)
        Ep.append(Epot(i))
        Ec.append(v**2/2)
        Em.append(Epot(i)+v**2/2)
    return (Xc,V,Ep,Ec,Em)

def trace(LL):
    Xt,Y=[],[]
    for i in LL:
        Xt.append(i[0][1][0])
        Y.append(i[0][1][1])
    afficheSimple(LL[-1])
    plt.plot(Xt,Y,'r')

def es(x,cs):
    n=0
    while x>=10:
        n+=1
        x=x/10
    print(int(x*10**cs)/10**cs,'x10^',n)

def JourArrive(LL):
    c,max=0,0
    t=0
    for i in LL:
        c+=1
        if i[0][1][0]**2+i[0][1][1]**2 > max:
            max=i[0][1][0]**2+i[0][1][1]**2
            t=c
    return(int(t/24))

def dynamique(LL,vitesseExecution):
    n,v=len(LL),vitesseExecution
    plt.ion()
    afficheSimple(LL[0])
    plt.pause(1)
    i,j=v,0
    while i < n:
        plt.plot([LL[j][0][1][0],LL[i][0][1][0]],[LL[j][0][1][1],LL[i][0][1][1]],'r')
        i+=v
        j+=v
        plt.pause(0.001)