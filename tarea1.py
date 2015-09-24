# coding: utf-8
import numpy
from pylab import *
import matplotlib
b=numpy.loadtxt('sun_AM0.dat')
LongitudOnda=[]
Flujo=[]
for par in b:
    a=np.array(par)
    LongitudOnda.append(a[0])
    Flujo.append(a[1])
plot(LongitudOnda,Flujo)
xlabel('Longitud de onda (nm)')
ylabel('Flujo (W/m^2/nm)')
xlim(100,2600)
ylim(0,2.5)
title('Espectro del Sol')
savefig("Espectro.png")
show()
