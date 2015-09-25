import numpy
from pylab import *
import matplotlib
#Importar Datos
b=numpy.loadtxt('sun_AM0.dat')
#Definiendo bases
LongitudOnda=[]
Flujo=[]
integral=0
integral2=0
#Ajustar las variables con los datos
for par in b:
    a=np.array(par)
    LongitudOnda.append(a[0]*100) #Multiplico por 100 para convertir de (W/m^2/nm) a (erg/s/A/cm^2)
    Flujo.append(a[1]*10) #Multiplico por 10 para pasar de nm a Angstrom (A)
#Integral Flujo v/s Longitud de onda
for a in range(1695):
    LongDif=LongitudOnda[a+1]-LongitudOnda[a]
    PromFlujo=(Flujo[a]+Flujo[a+1])/2
    Add=PromFlujo*LongDif
    integral=integral+Add
print ('La luminosidad del sol calculada es ' + str(integral)+ ' erg/s/cm^2')
#Constantes  
h=6.62606*10**(-27)
c=29979245800000
kb=1.38064*10**(-16)
Tsol=5778
GranK=((2*pi*h)/(c**2))*(((kb*Tsol)/h)**4)
#Preparando la segunda integral
P=[]
x=np.arange(0.002, pi/2.-0.002, 0.002)
for a in range(784):
    ad=(((np.tan(x[a]))**3)/(np.exp(np.tan(x[a]))-1))*((1/(np.cos(x[a]))**2))
    P.append(ad)
#Integrando
for a in range(783):
    LongDif=x[a+1]-x[a]
    PromFlujo=(P[a+1]+P[a])/2
    Add=PromFlujo*LongDif
    integral2=integral2+Add
print ('La integral de la funcion se Planck (sin constantes) es '+ str(integral2))
#Integrando utilizando np.trapz
J=np.trapz(Flujo,LongitudOnda)
print ('La primera integral usando np.trapz resulta '+str(J)+', muy parecido al obtenido con el algoritmo')
K=np.trapz(P,x)
print ('La integral de la funcion de Planck con np.trapz da '+str(K)+' igual que lo resultado con el algoritmo e igual (pi^4)/15')
#Preparando el plot
plot(LongitudOnda,Flujo)
xlabel('Longitud de onda (A)')
ylabel('Flujo (erg/s/A/cm^2)')
xlim(10000,260000)
ylim(0,25)
title('Espectro del Sol')
savefig("Espectro.png")
show()


