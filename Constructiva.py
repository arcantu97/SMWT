import numpy as np
import itertools
from itertools import combinations_with_replacement
import collections
import sys
import pprint

print("\n")
archivo = str(input("\t\t\tIntroduce el nombre del archivo: "))
fa = np.genfromtxt(archivo +".txt", delimiter=',', usecols=(0,1,2,3), dtype="int")[0:-1]
N = np.genfromtxt(archivo+".txt", delimiter=',')[-1,0:1]
N = int(N)
print("\t\t\tCantidad de procesos: ", N)

# Convirtiendo array a lista y ordenando por pesos
l = fa.tolist()
l.sort(key=lambda x: x[3], reverse=True)
# Empezando heuristica constructiva
TN = []
C = []
D = []
T = []
c = 0
ttp = 0
for d in l:
	ind = d[0]
	TN.append(ind)
	p = d[1]
	c += p
	d.append(c)
	tot = p - d[2]
	if tot < 0:
		d.append(0)
	else:
		d.append(tot)
	w = d[3]
	t = d[5]
	op = w*t 
	ttp += op
print("\n\n")
print("\t\t\tConstructiva")
print("\t\t\tTardanza Total Ponderada es: ", ttp)
# ***********************************

print("\n\n")
print("\t\t\t Busqueda local")
ttp2 = 0
for i in itertools.permutations(l):
	for x in i:
		for t in x:
			w = x[3]
			t = x[5]
			op = w*t
			ttp2 += op
			if ttp2 < ttp and ttp2 > 0:
				c = ttp2
				
	print("\t\t\tTardanza Total Ponderada es: ",c)
	break
			
				


