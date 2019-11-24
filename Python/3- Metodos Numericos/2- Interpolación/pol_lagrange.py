##*-----------------------------------------------------------*##
## ----- Metodo de Interpolación por metodo de lagrange -------##
## ----       UCV - Kembert Nieves CIV 21.283.323         -----##
##*-----------------------------------------------------------*##

import sys
from sympy import *
import numpy as np

def lagrange():
    ##*--------------*##
    #*--- Entradas ---*#
    ##*--------------*## 
    
    x = list(eval(input("Ingrese los valores de X separados por comas: ")))
    y = list(eval(input('Ingrese los valores de Y separados por comas: ')))
    
    if(len(x) != len(y)):
        return print("Error al ingresar datos!")
    
    polI = 1
    divAux = []
    l_x = []
    X = symbols('x')

    ##*--------------*##
    #*--- Procesos ---*#
    ##*--------------*##

    suma = 0 
    for i in range(len(x)):        
        for j in range(len(x)-1):
            if j!=i:
                alpha = j+1           
                
                if (alpha == i): alpha += 1 
                if (alpha == len(x)): continue

                polI = (X-x[j])*(X-x[alpha])
                divI = (x[i]-x[j])*(x[i]-x[alpha])

        suma += y[i]*polI/divI
        l_x.append(y[i]*polI/divI)
        divAux.append(y[i]/divI)

    ##*-------------*##
    #*--- Salidas ---*#
    ##*-------------*##

    print('X array')
    print(x)

    print('Y array')
    print(y)

    while(1):    
        print("/*------------------    Menu    ------------------*/")
        print("Presione 1 para ver solo los coeficientes")
        print("Presione 2 para ver el polinomio extendido ")
        print("Presione 3 para ver el polinomio de Lagrange ")
        print("Presione 4 para ver todos ")
        user = input("0 para salir del programa: ")

        if(user == "1"):
            print("/*---------------   Res   ---------------------*/")
            print("Los coeficientes de lagrange a0,a1,...,an respectivamente")
            print(divAux)
            
        elif(user == "2"):
            print("\n")
            print("/*---------------   Res   ---------------------*/")
            print("La expresion extendida del polinimio es")
            print(expand(suma))        
        elif(user == "3"):
            print("\n")
            print("/*---------------   Res   ---------------------*/")
            print("Polinomio en la forma de Lagrange")
            print(suma)
            print("Donde: ")
            for i in range(len(x)):
                print("L_"+str(i)+" = "+str(l_x[i]))
        elif(user == "4"):
            print("\n")
            print("/*-------------  Ver todos  --------------------*/")
            print(divAux)
            print(expand(suma))        
            print(suma)
        elif(user == "0"):
            print("\n")
            print("/*-----------------Gracias!!-----------------*/")
            print("Fin del programa")
            return 0

##*-------------*##
#*---- main -----*#
##*-------------*##
lagrange()