import csv
from random import randint
class Negativos(Exception):
    pass
class Menores(Exception):
    pass
class Menores2(Exception):
    pass
class Menores3(Exception):
    pass 

contador=1
print("\n")
d = int(input("\t\t\tCantidad de instancias a generar: "))
print("\n")
nom = str(input("\t\t\tIntroduce el nombre del archivo a generar: "))
while contador <= d:
    try:
        print("\n")
        n = int(input("\t\t\tIntroduce la cantidad de procesos a generar: "))
        if d < 1 and n < 1:
            raise Negativos
        print("\n")
        wmin = int(input("\t\t\tIntroduce el peso minimo: "))        
        if wmin < 1:   
            raise Negativos
        print("\n")
        wmax = int(input("\t\t\tIntroduce el peso minimo: "))
        if wmax < wmin:   
            raise Menores
        print("\n")
        vmin = int(input("\t\t\tIntroduce el tiempo de vencimiento minimo: "))
        if vmin < 1:
            raise Negativos
        print("\n")
        vmax = int(input("\t\t\tIntroduce el tiempo de vencimiento maximo: "))
        if vmax < vmin:   
            raise Menores2
        print("\n")
        pmin = int(input("\t\t\tIntroduce el tiempo de procesamiento minimo: "))
        if vmin < 1:
            raise Negativos
        print("\n")
        pmax = int(input("\t\t\tIntroduce el tiempo de procesamiento maximo: "))
        if pmax < pmin:   
            raise Menores3
        if d > 0 and n > 0:
            N = str(n)
            incluir = 0
            while contador <= d:
                archivo = 0
                i = 0
                k = str(archivo+1)
                with open(str(nom) + "-" + str(archivo+1) + "-" + str(n) + ".txt",'a') as f:
                    writer = csv.writer(f, lineterminator='\n')
                    for i in range(n):
                        i+=1 
                        vi = randint(vmin,vmax)
                        wi = randint(wmin,wmax)
                        pi = randint(pmin,pmax)
                        writer.writerow([i,pi,vi,wi])
                    writer.writerow([N,'','',''])
                    contador+=1
                break
            print("\t\t **** Archivos creados satisfactoriamente **** ")
    except ValueError:
        print("\t\t\t Introduciste un caracter. Por favor introduce un numero entero.")
    except Negativos as na:
        print("\t\t\tNo se admiten valores menores a '1' ", na)
    except Menores as mens:
        print("\t\t\t El valor del peso maximo no puede ser menor al del peso minimo, ingrese un valor mayor a ",wmin, mens)
    except Menores2 as mens2:
        print("\t\t\t El valor del peso maximo no puede ser menor al del peso minimo, ingrese un valor mayor a ",vmin, mens2)