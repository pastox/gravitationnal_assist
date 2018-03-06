## Récupération des données

ed=e2
e_assist=e4

LL=Deplace(Simulation3,ed,e_assist,900,Objectif3,R,100)
LL=DeplaceSansObjectif(LL,ed,1500)
Xc,V,Ep,Ec,Em=courbes(LL,ed,e_assist)

LL2=DeplaceSansObjectif([Simulation2],ed,1500)
Xc2,V2,Ep2,Ec2,Em2=courbes(LL2,ed)

LL3=Deplace(Simulation3,ed,792,Objectif2,R,5)
LL3=DeplaceSansObjectif(LL3,ed,1500)
Xc3,V3,Ep3,Ec3,Em3=courbes(LL3,ed)

a,b=abs(Em[782*e0//ed]-Em[10*e0//ed]),Em[-1]-Em[785*e0//ed]
c = Em2[10*e0//ed]-((Simulation3[0][1][2]**2+Simulation3[0][1][3]**2)/2+Epot(Simulation3))

## Trajet espace
# Avec assistance
trace(LL)
plt.plot([Objectif2[0]],[Objectif2[1]],'ok')

# Le plus rapide
trace(LL2)

# Dynamique
plt.plot([Objectif2[0]],[Objectif2[1]],'ok')
dynamique(LL,100)

dynamique(LL2,50)

## Graphiques
# Vitesse
plt.xlabel("Temps (jours)")
plt.ylabel("Vitesse de la sonde relativement au solei (m/s)")
plt.plot(Xc,V)

# Énergies (avec assistance)
plt.xlabel("Temps (jours)")
plt.ylabel("Énergies (Joules/kg)")
plt.plot(Xc,Ep,'g',label="Ep")
plt.plot(Xc,Ec,'b',label="Ec")
plt.plot(Xc,Em,'r',label="Em")
plt.legend()
plt.show()


plt.xlabel("Temps (jours)")
plt.ylabel("Énergies (Joules)")
plt.plot(Xc3,Ep3,'g',label="Ep")
plt.plot(Xc3,Ec3,'b',label="Ec")
plt.plot(Xc3,Em3,'r',label="Em")
plt.legend()
plt.show()

# Énergies (sans assistance) 
plt.xlabel("Temps (jours)")
plt.ylabel("Énergies (Joules)")
plt.plot(Xc2,Ep2,'g',label="Ep")
plt.plot(Xc2,Ec2,'b',label="Ec")
plt.plot(Xc2,Em2,'r',label="Em")
plt.legend()
plt.show()

## Analyse des résultats
es(a,2)
print('Joules/kg à fournir pour AG')
print()
es(b,2)
print('Joules/kg gagnés par AG')
print()
es(c,2)
print('Joules/kg à fournir trajet direct')
print()
print(int((c-a)/c*100),'% Pourcentage énergie gagnée par AG par rapport au trajet direct')
print ()
print('Temps du trajet :',JourArrive(LL)//365,'ans et',(JourArrive(LL)%365)//31,'mois')
print(int((JourArrive(LL)-JourArrive(LL2))/JourArrive(LL2)*100),'% de temps de trajet supplémentaire au trajet direct')
