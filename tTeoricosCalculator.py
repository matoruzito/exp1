from sympy import *
import math 

pi = 3.141592   #Valor de Pi aproximado


print("Bienvenido a la calculadora de tiempos teóricos para periodo de péndulo simple \n")

#----Recibimos un conjunto cerrado [min,max] para valores de G supuestos----#

minG = sympify(input("Minimo valor supuesto de G:\t "))
maxG = sympify(input("Maximo valor supuesto de G:\t "))
L = sympify(input("Largo de la cuerda: \t "))

if(minG > maxG):
    print("Minimo debe ser menor que el maximo! Adios!\n")
else:
    precision = sympify(input("Cantidad de decimales de precisión:\t "))
    resta = maxG - minG 
    iteraciones = resta*(10**precision) #Cantidad de iteraciones
    i = 0
    g = []
    t = []
    g.append(minG)
    print("ID\t\t G\t\t T\t\t")
    while(i < iteraciones):
        newG = g[i] + (1 / (iteraciones / 2))       #incrementar de a paso definido
        newT = 2*pi * math.sqrt(L / newG)     #Obtener T teórico para el supuesto G
        

        g.append(newG)
        t.append(newT)
        print(i, "\t\t", float(g[i]), "\t\t", float(t[i]), "\t\t")
        i = i+1
    








