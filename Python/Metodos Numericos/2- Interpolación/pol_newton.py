##*---------------------------------------------------------------*##
## -- Metodo de Interpolación por diferencias divididas y Newton --##
## ------       UCV - Kembert Nieves CIV 21.283.323         -------##
##*---------------------------------------------------------------*##

import numpy as np
from sympy import *

def pol_newton():
    ##*--------------*##
    #*--- Entradas ---*#
    ##*--------------*## 
    x = list(eval(input("Ingrese los valores de X separados por comas: ")))
    y = list(eval(input('Ingrese los valores de Y separados por comas: ')))

    if(len(x) != len(y)):
        return print("Error en los datos de entrada")
    
    n = len(x)
    Px_co = np.empty((n-1,n-1), float)
    
    Px = ""
    PxAux = y[0]
    monomios = 1   
    pol = 1
    polinomio = 0
    
    X = symbols('x')

    ##*--------------*##
    #*--- Procesos ---*#
    ##*--------------*##

    #*--- Obtener los coeficientes de la tabla ---*#
    for i in range(n):
        for j in range(n):
            if(j+1 > n - 1 ): continue
            if(i+j+1 > n - 1 ): continue
            if(i == 0):
                Px_co[i,j] = (y[j+1]-y[j]) / (x[i+j+1]-x[j])
            else:
                Px_co[i,j] = (Px_co[i-1][j+1]-Px_co[i-1][j]) / (x[i+j+1]-x[j])

    #*--- Armar el polinomio ---*#
    for i in range(n-1):
        for j in range(i+1):
            monomios *= X-x[j]
        
        PxAux += factor(Px_co[i,0] * (monomios))
        monomios = 1

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
        print("Presione 3 para ver el polinomio de Newton ")
        print("Presione 4 para ver todos ")
        user = input("0 para salir del programa: ")

        if(user == "1"):
            print("/*---------------   Res   ---------------------*/")
            print("Los coeficientes a0,a1,...,an respectivamente")
            print("Proveniente de la tabla de diferencias divididas son: ")
            print("a_0: "+str(y[0]))
            for i in range(n-1):
                print("a_"+str(i+1)+":"+str(Px_co[i,0]))
            
        elif (user == "2"):
            print("\n")
            print("/*---------------   Res   ---------------------*/")
            print("La expresion extendida del polinimio es")
            print(expand(PxAux))
        elif (user == "3"):
            print("\n")
            print("/*-------------------------------------------*/")
            print("Polinomio en la forma de Newton")
            print(PxAux)
        elif(user == "4"):
            print("\n")
            print("/*-------------  Ver todos  --------------------*/")
            print("a_0: "+str(y[0]))
            for i in range(n-1):
                print("a_"+str(i+1)+":"+str(Px_co[i,0]))
            print(expand(PxAux))
            print(PxAux)
        elif (user == "0"):
            print("\n")
            print("/*-----------------Gracias!!-----------------*/")
            print("Fin del programa")
            return 0
    
##*-------------*##
#*---- main -----*#
##*-------------*##
pol_newton()