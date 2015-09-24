# coding: utf-8
import numpy
from pylab import *
import matplotlib
b=numpy.loadtxt('sun_AM0.dat')
LongitudOnda=[]
Flujo=[]
integral=0
for par in b:
    a=np.array(par)
    LongitudOnda.append(a[0])
    Flujo.append(a[1])
#for a in range(1695):
#    LongDif=LongitudOnda[a+1]-LongitudOnda[a]
#    PromFlujo=(Flujo[a]+Flujo[a+1])/2
#    Add=PromFlujo*LongDif
#    integral=integral+Add
#print (integral)
J=np.trapz(Flujo,LongitudOnda)
print (J)
plot(LongitudOnda,Flujo)
xlabel('Longitud de onda (nm)')
ylabel('Flujo (W/m^2/nm)')
xlim(100,2600)
ylim(0,2.5)
title('Espectro del Sol')
savefig("Espectro.png")
show()
