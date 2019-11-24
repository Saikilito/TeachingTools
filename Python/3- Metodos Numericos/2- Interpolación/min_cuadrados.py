##*-----------------------------------------------------------*##
## ----- Metodo de Interpolación por metodo de lagrange -------##
## ----       UCV - Kembert Nieves CIV 21.283.323         -----##
##*-----------------------------------------------------------*##


import numpy as np
from sympy import *

def min_cuadrados():
    ##*--------------*##
    #*--- Entradas ---*#
    ##*--------------*## 

    x = list(eval(input("Ingrese los valores de X separados por comas: ")))
    y = list(eval(input('Ingrese los valores de Y separados por comas: ')))
    print("Este programa genera modelos polinomiales")
    m = int(input("Ingrese el grado del polinomio que quiere modelar: "))
    
    if(len(x) != len(y)):
        return print("Error al ingresar datos!")    

    if(m >= len(x)):
        return print("Se requieren más datos para este grado")

    m += 1
    n = len(x)
    Sx = np.zeros((n,n),float)
    Sxy = np.zeros(n,float)
    auxSx = np.empty((m,m),float)
    auxSxy = np.empty((m),float)
    auxSol = np.empty((m),float)


    Px = 0
    X, Y = symbols('x y')
    
    ##*--------------*##
    #*--- Procesos ---*#
    ##*--------------*##

    # *--- Creando vectores ---*#
    for i in range(n):
        for j in range(n):
            for k in range(n):
                #*--- Matriz de sumatorias de x elevado ---*#
                Sx[i,j] += x[k]**(j+i)
            #*--- Vector de sumatorias de y * x elevado ---#
            Sxy[i] += y[j]*(x[j]**i) 
    
    #*--- Solucionando el sistema ---*#
    auxSx = Sx[0:m,0:m]
    auxSxy = Sxy[0:m]
    sol = np.linalg.solve(auxSx,auxSxy)
    auxSol = np.around(sol,3)
    #*--- Armando el polinomio solicitado ---*#
    for i in range(m):
        Px += X**i * np.around(sol[i],3)

    ##*-------------*##
    #*--- Salidas ---*#
    ##*-------------*##
    
    
    print('X array')
    print(x)

    print('Y array')
    print(y)

    print("El modelo solicitado fue un polinomio de grado: ",(m-1))
    
    while(1):
        print("/*------------------    Menu    ------------------*/")
        print("Presione 1 para ver solo los coeficientes")
        print("Presione 2 para ver el polinomio")
        print("Presione 3 para ver ambos")
        user = input("Presione 0 para salir del programa: ")

        if(user == "1"):
            print("/*---------------   Res   ---------------------*/")
            print("Los coeficientes a0,a1,...,an respectivamente son: ")
            print(np.around(sol,3))
            print(np.around(auxSol,3))
        elif(user == "2") :
            print("/*---------------   Res   ---------------------*/")
            print("La expresion del polinimio es")
            print(Y, " = " , Px)

        elif(user == "3"):
            print("/*---------------   Ambos   ---------------------*/")
            print(sol)
            print(str(Y) + " = " + str(Px))
        elif (user == "0"):
            print("\n")
            print("/*-----------------Gracias!!-----------------*/")
            print("Fin del programa")
            return 0


##*-------------*##
#*---- main -----*#
##*-------------*##
min_cuadrados()