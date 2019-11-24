##*---------------------------------------------------------------*##
## --------- Metodo de tabla de diferencias divididas -------------##
## ------       UCV - Kembert Nieves CIV 21.283.323         -------##
##*---------------------------------------------------------------*##

import numpy as np


def table_diff():
    ##*--------------*##
    #*--- Entradas ---*#
    ##*--------------*##
    x = list(eval(input("Ingrese los valores de X separados por comas: ")))
    y = list(eval(input('Ingrese los valores de Y separados por comas: ')))

    if(len(x) != len(y)):
        return print("Error en los datos de entrada")

    n = len(x)

    Px_co = np.empty((n-1,n-1), float)



    ##*--------------*##
    #*--- Procesos ---*#
    ##*--------------*##

    for i in range(n):
        for j in range(n):
            if(j+1 > n - 1 ): continue
            if(i+j+1 > n - 1 ): continue
            if(i == 0):
                Px_co[i,j] = (y[j+1]-y[j]) / (x[i+j+1]-x[j])
            else:
                Px_co[i,j] = (Px_co[i-1][j+1]-Px_co[i-1][j]) / (x[i+j+1]-x[j])

    ##*-------------*##
    #*--- Salidas ---*#
    ##*-------------*##
    print("/*---------------   Res   ---------------------*/")
    print("Tabla de diferencias divididas")
    print("|  x  |:" + str(x))
    print("|  y  |:" + str(y))
    for i in range(n-1):
        print("|  "+str(i+1)+"  |:" + str(Px_co[i,0:]) )


##*-------------*##
#*---- main -----*#
##*-------------*##
table_diff()