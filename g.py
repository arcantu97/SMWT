import threading
from random import randint 
class Negativos(Exception):
    pass
class Menores(Exception):
    pass
class Menores2(Exception):
    pass
class Menores3(Exception):
    pass

cont = 0
print("\n")
d = int(input("\t\t\t¿Cuántas instancias deseas generar? "))
while True:
    try:       
        nom = str(input("\t\t\tIntroduce el nombre que recibiran los archivos: "))
        print("\n")
        n = int(input("\t\t\t¿Cuántas tareas deseas generar?  "))
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
            i = 0
            for archivo in range(d):
                k = str(archivo+1)
                fichero = open(str(nom) + "-" + str(archivo+1) + "-" + str(n) + ".txt",'a')
                for i in range(n):
                    i += 1
                    pi = randint(pmin,pmax)
                    vi = randint(vmin,vmax*pmax)
                    wi = randint(wmin,wmax)
                    fichero.write(str(i) + ",")
                    fichero.write(str(pi) + ",")    
                    fichero.write(str(vi) + ",")
                    fichero.write(str(wi) + "\n") 
                fichero = open(str(nom) + "-" + str(archivo+1) + "-" + str(n) + ".txt",'a')
                fichero.write(str(n)+ ","+ ","+"," + "\n")
            cont += 1
            fichero.close()
            del(fichero)
            print("\t\t **** Archivos creados satisfactoriamente **** ")
            break 
    except ValueError:
        print("\t\t\t Introduciste un caracter. Por favor introduce un numero entero.")
    except Negativos as na:
        print("\t\t\tNo se admiten valores menores a '1' ", na)
    except Menores as mens:
        print("\t\t\t El valor del peso maximo no puede ser menor al del peso minimo, ingrese un valor mayor a ",wmin, mens)
    except Menores2 as mens2:
        print("\t\t\t El valor del tiempo de vencimiento máximo no puede ser menor al del tiempo de vencimiento minimo, ingrese un valor mayor a ",vmin, mens2)
    except Menores3 as mens3:
        print("\t\t\t El valor del tiempo de procesamiento máximo no puede ser menor al del tiempo de procesamiento minimo, ingrese un valor mayor a ",pmin, mens3)
