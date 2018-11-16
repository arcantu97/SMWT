import numpy as np
from itertools import combinations

print("\n")
archivo = str(input("\t\t\tIntroduce el nombre del archivo: "))
fa = np.genfromtxt(archivo +".txt", delimiter=',', usecols=(0,1,2,3), dtype="int")[0:-1]
N = np.genfromtxt(archivo+".txt", delimiter=',')[-1,0:1]
N = int(N)
print("\n")
print("\t\t\tCantidad de procesos: ", N)

# Convirtiendo array a lista y ordenando por pesos
l = fa.tolist()
l.sort(key=lambda x: x[3], reverse=True)
t = l
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
print("Orden de trabajos: ",TN)
print("Tardanza Total Ponderada es: ", ttp)

for i in range(1, len(l) + 1):
    print (combinations(l, i))