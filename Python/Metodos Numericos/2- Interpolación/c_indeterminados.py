##*-----------------------------------------------------------*##
## ---- Metodo de Interpolación por coeficientes intedeminados -----##
## ----       UCV - Kembert Nieves CIV 21.283.323         -----##
##*-----------------------------------------------------------*##

from sympy import *
import numpy as np

def interpolacion_pol():    
    ##*--------------*##
    #*--- Entradas ---*#
    ##*--------------*## 
    
    x = list(eval(input("Ingrese los valores de X separados por comas: ")))
    y = list(eval(input('Ingrese los valores de Y separados por comas: ')))
    
    if(len(x) != len(y)):
        return print("Error en los datos de entrada")

    n = len(x)
    polExp = ""
    polInt = 0

    A =  np.empty((n,n), float)

    X,Y = symbols('x y')  

    ##*--------------*##
    #*--- Procesos ---*#
    ##*--------------*##

    #*--- Obtener Matriz A --*#
    for k in range(n):
        for i in range(n):
            A[k,i] = x[k]**(i)
          
    #*--- Solucionar sistema ---*#
    sol = np.linalg.solve(A,y)

    for i in range(n):
            polInt +=  sol[i] * X**(i)


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
        print("Presione 2 para ver el polinomio")
        print("Presione 3 para ver ambos")
        user = input("Presione 0 para salir del programa: ")

        if(user == "1"):
            print("/*---------------   Res   ---------------------*/")
            print("Los coeficientes a0,a1,...,an respectivamente son: ")
            print(sol)
        elif(user == "2") :
            print("/*---------------   Res   ---------------------*/")
            print("La expresion del polinimio es")
            print(str(Y) + " = " + str(polInt))

        elif(user == "3"):
            print("/*---------------   Ambos   ---------------------*/")
            print(sol)
            print(str(Y) + " = " + str(polInt))
        elif (user == "0"):
            print("\n")
            print("/*-----------------Gracias!!-----------------*/")
            print("Fin del programa")
            return 0



##*-------------*##
#*---- main ----*#
##*-------------*##
interpolacion_pol()