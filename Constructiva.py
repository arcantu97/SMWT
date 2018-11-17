import numpy as np
import itertools
from itertools import permutations
import collections
import sys

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
l2 = l
ttp2 = 0
m = list(permutations(l2))
for i in m:
	for x in i:
		w = x[3]#elemento 3 de la permutacion x
		t = x[5]#elemento 5 de la permutacion x
		op = w*t
		ttp2 += op
		if ttp2 < ttp:
			if ttp2 == 0:
				break
			if ttp2 > 0:
				print("\t\t\tTardanza Total Ponderada es: ", ttp2)
				break

