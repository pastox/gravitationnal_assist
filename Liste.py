    
## Listes

e0=3600*24 #1 jour
e1=3600*6 #6 heures
e2=3600 #1 heure
e3=3600//2 #30 minutes
e4=3600//60 #1 minute

# Planètes

MasseSoleil=2000000000000000000000000000000
ROterre = 150000000000

Terre =[150000000000.0, 0.0, 150000000000, 6e+24, 1.9923849908611068e-07, 0, 6400000]
Mars = [227000000000.0,0.0,227000000000.0,6.41e+23,1.0585451552609955e-07,0,3396000.0]
Jupiter = [778E9,0, 778E9,1.89E27,2*pi/(4335*24*3600),0,70E6]
Mercure = [58E9, 0, 58E9, 330E21, 2*pi/(24*3600*88), 0,2439E3]
Venus = [108E9,0,108E9, 4.8E24, 2*pi/(24*3600*224), 0,6E6]
Jupiter2 = [cos(pi/5-pi/110)*778E9,sin(pi/5-pi/110)*778E9, 778E9,1.89E27,2*pi/(4335*24*3600),pi/5-pi/110,70E6]

# Sondes

Lune=[ROterre+400E6, 0, 0, (29850+1000)]

# Lanceurs

P=[[MasseSoleil, [ROterre, 0, 0, 0]], Terre]

Accel=[[MasseSoleil, [ROterre+400E6, 0, 0, (29800)]], Terre]

Lune0=[[MasseSoleil, Lune], Terre]

Frein=[[MasseSoleil, [ROterre+400E6, 400E6, -1500, (29850)]], Terre]

Lune_mars=[[MasseSoleil, Lune], Terre, Mars]

SystemeSolaire = [[MasseSoleil, Lune], Mercure, Venus, Terre, Mars, Jupiter] 

Simulation = [[MasseSoleil,[ROterre+400E6,0,0,35268.65]], Terre, Jupiter2] 
Simulation2 = [[MasseSoleil,[ROterre+400E6,0,0,38670]], Terre, Jupiter] # sans assistance
Simulation3 = [[MasseSoleil,[ROterre+400E6,0,0,35230]], Terre, Jupiter2]
Simulation4 = [[MasseSoleil,[ROterre+400E6,0,0,29850]], Jupiter2]

r,a=150000000000+500E3+6400000, 62/365*2*pi
x,y=72376161263.93092,131383755771.77516
rayon=sqrt(x**2+y**2)
angle=atan(y/x)

Objectif=[x,y,792]
Objectif2=[x+(500E3+6400000)*cos(angle),y+(500E3+6400000)*sin(angle),792]
Objectif3=[x+(6400000+250E3)*cos(angle),y+(6400000+250E3)*sin(angle),792]

R=[300,500,640,730,770]
C=['r','g','c','y','r']

R1=[650,700,750]
C1=['c','r','g']