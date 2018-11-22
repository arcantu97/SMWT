import numpy as np
import itertools
from itertools import combinations_with_replacement
import collections
import sys
import pprint

print("\n")
archivo = str(input("\t\t\tIntroduce el nombre del archivo: "))
fa = np.genfromtxt(archivo +".txt", delimiter=',', usecols=(0,1,2,3), dtype="int")[0:-1]
fa2 = np.genfromtxt(archivo +".txt", delimiter=',', usecols=(0,1,2,3), dtype="int")[0:-1]
fa3 = np.genfromtxt(archivo +".txt", delimiter=',', usecols=(0,1,2,3), dtype="int")[0:-1]
N = np.genfromtxt(archivo+".txt", delimiter=',')[-1,0:1]
N = int(N)
print("\t\t\tCantidad de procesos: ", N)


# *****************       Experimento #1 por peso(Prioridad) *********************************
l = fa.tolist()
l.sort(key=lambda x: (x[3]), reverse=True)
x =l
# Empezando heuristica constructiva
print("\n\n")
print("\t\t\t ****** Experimento #1 por peso(Prioridad) ******")
TN = []
C = []
D = []
T = []
c = 0
ttp = 0
for d in x:
	p = d[1]
	c += p
	d.append(c)
for m in x:
	tot = m[4] - m[3]
	if tot < 0:
		m.append(0)
	else:
		m.append(tot)
	w = m[3]
	t = m[5]
	op = w*t
	ttp+= op
print("\n\n")
print("\t\t\t Heuristica Constructiva")
print("\t\t\tTardanza Total Ponderada es: ", ttp)

print("\n\n")
print("\t\t\t Busqueda local")
ttpf = 0
for i in itertools.permutations(x):
	for x in i:
		for t in x:
			w = x[3]
			t = x[5]
			op = w*t
			ttpf += op
			if ttpf < ttp and ttpf > 0:
				c = ttpf
				
	print("\t\t\tTardanza Total Ponderada es: ",c)
	break

# *******************************************************

# *****************       Experimento #2 por tiempo de procesamiento *********************************
l2 = fa2.tolist()
l2.sort(key=lambda x: (x[1]), reverse=True)
x2 =l2
# Empezando heuristica constructiva
print("\n\n")
print("\t\t\t ****** Experimento #2 por tiempo de procesamiento ******")
TN2 = []
C2 = []
D2 = []
T2 = []
c2 = 0
ttp2 = 0
for d2 in x2:
	p2 = d2[1]
	c2 += p2
	d2.append(c2)
for m2 in x2:
	tot2 = m2[4] - m2[3]
	if tot2 < 0:
		m2.append(0)
	else:
		m2.append(tot)
	w2 = m2[3]
	t2 = m2[5]
	op2 = w2*t2
	ttp2+= op2
print("\n\n")
print("\t\t\t Heuristica Constructiva")
print("\t\t\tTardanza Total Ponderada es: ", ttp2)

print("\n\n")
print("\t\t\t Busqueda local")
ttpf2 = 0
for i2 in itertools.permutations(x2):
	for x2 in i2:
		for t in x2:
			w2 = x2[3]
			t2 = x2[5]
			op2 = w*t
			ttpf2 += op2
			if ttpf2 < ttp2 and ttpf2 > 0:
				c2 = ttpf2
				
	print("\t\t\tTardanza Total Ponderada es: ",c2)
	break

# *******************************************************


# *****************       Experimento #3 por relación peso/tiempo de vencimiento *********************************
l3 = fa3.tolist()
l3.sort(key=lambda x: (x[3]/x[2]), reverse=True)
x3 =l3
# Empezando heuristica constructiva
print("\n\n")
print("\t\t\t ****** Experimento #3 por relación peso/tiempo de vencimiento ******")
TN3 = []
C3 = []
D3 = []
T3 = []
c3 = 0
ttp3 = 0
for d3 in x3:
	p3 = d3[1]
	c3 += p3
	d3.append(c3)
for m3 in x3:
	tot3 = m3[4] - m3[3]
	if tot3 < 0:
		m3.append(0)
	else:
		m3.append(tot3)
	w3 = m3[3]
	t3 = m3[5]
	op3 = w3*t3
	ttp3+= op3
print("\n\n")
print("\t\t\t Heuristica Constructiva")
print("\t\t\tTardanza Total Ponderada es: ", ttp3)

print("\n\n")
print("\t\t\t Busqueda local")
ttpf3 = 0
for i3 in itertools.permutations(x3):
	for x3 in i3:
		for t3 in x3:
			w3 = x3[3]
			t3 = x3[5]
			op3 = w3*t3
			ttpf3 += op3
			if ttpf3 < ttp3 and ttpf3 > 0:
				c3 = ttpf3
				
	print("\t\t\tTardanza Total Ponderada es: ",c3)
	break

# *******************************************************



m1 = "************** Experimento #1 Por peso (Prioridad) **************"
m2 = "************** Experimento #2 Por tiempo de procesamiento **************"
m3 = "************** Experimento #3 Por relación peso/tiempo de vencimiento **************"
rc = "Resultados de constructiva"
rbl = "Resultados de busqueda local"
mn = "***********Fin de experimento**********"
fichero = open("resultados" + "-" + str(archivo) + ".txt",'a')
# experimento 1
fichero.write(str(m1)+ "\n")
fichero.write(str(rc) + ": " + str(ttp) + "\n")
fichero.write(str(rbl) + ": " + str(c)+ "\n")
fichero.write(str(mn) + "\n"+ "\n")
# experimento 2
fichero.write(str(m2)+ "\n")
fichero.write(str(rc) + ": " + str(ttp2) + "\n")
fichero.write(str(rbl) + ": " + str(c2)+ "\n")
fichero.write(str(mn) + "\n"+ "\n")
# experimento 3
fichero.write(str(m3)+ "\n")
fichero.write(str(rc) + ": " + str(ttp3) + "\n")
fichero.write(str(rbl) + ": " + str(c3)+ "\n")
fichero.write(str(mn) + "\n"+ "\n")
fichero.close()
del(fichero)