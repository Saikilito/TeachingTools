<h1 align="center">Numpy</h1>

Numpy es una librería de Python que significa **Numerical Python**, esta es la librería principal de este lenguaje para la informática científica proporcionando potentes estructuras de datos implementado matrices y matrices multidimensionales, estas estructuras de datos garantizan el cálculo de eficientes con matrices.

**Numpy Array:** Es un potente objeto de Matriz N-dimensional que tiene formas de filas y columnas.

## ¿Por qué usar Numpy en lugar de listas?

* Numpy ocupa menos memoria en comparación a las listas de Python
* Numpy es mucho más rápido en términos de ejecución

## Cómo implementar Numpy

Para importar numpy por convención se hace de la siguiente manera

```python
import numpy as np
```

Para **definir un vector**:

```python
a =  np.array([1,2,3])  

print('1D array')
print(a)
```

Para **definir una matriz**:

```python
b = np.array([
    (1,2,3),
    (4,5,6)
])

print('2D array')
print(b)
```

## Operaciones básicas de Numpy

_Especificar_ el **tipo de dato** que contiene el Array:

```python
    a = np.array([
        (1,2,3),
        (4,5,6)
    ],
    dtype=np.int64)
```

_Obtener_ el **tipo de datos** de una matris

```python
    a = np.array([1,2,3],[4,5,6])
    a.dtype # int64
```

_Obtener_ las **dimensiones**

```python
    a = np.array([1,2,3],[4,5,6])
    a.shape # (2,3)
```

_Obtener_ elementos de una columna

```python
    a = np.array([
        (1,2,3),
        (4,5,6)
    ])

    a[0:,2] # [3,6]
```

_Obtener_ el valor **maximo y minimo** de una matriz

```python
    a = np.array([
        (1,2,3),
        (4,5,6)
    ])

    a.max() #6
    a.min() #1
```

_Obtener_ la **inversa** de una matriz
```python
A = ([
    [2,0,1],
    [3,0,0],
    [5,1,1]
]);

np.linalg.inv(A)

#array([[ 0.        ,  0.33333333,  0.        ],
#       [-1.        , -1.        ,  1.        ],
#       [ 1.        , -0.66666667,  0.        ]])
```

**Sumar** _todos los elementos_ de una matriz

```python
    a = np.array([
        (1,2,3),
        (4,5,6)
    ])

    a.sum() #21
```

## Inicializar Matrices

Para crear matrices rellenas con elementos "**1**"

```python
    fill = 2
    column = 2
    ones = np.ones(fill,columns)
    # [(1,1),
    #  (1,1)]
```

Para crear matrices rellenas con elementos "**0**"

```python
    fill = 2
    column = 2
    ones = np.zeros(fill,columns)
    # [(0,0),
    #  (0,0)]
```

Para crear matrices rellenas con **elementos vacíos**

```python
    fill = 2
    column = 2
    ones = np.empty(fill,columns)
    # [(0.,0.),
    #  (0.,0.)]
```

Para crear matrices rellenas con **elementos aleatorios**

```python
    fill = 2
    column = 2
    ones = np.random.random(fill,columns)
    # [(0.465,0.6879),
    #  (0.889,0.144)]
```

Para _crear_ matrices rellenas con elementos de **un solo valor**

```python
    fill = 2
    column = 2
    num = 8
    ones = np.full((fill,columns),num)
    # [(8,8),
    #  (8,8)]
```

Para _crear_ una **Matriz identidad**

```python
    np.eye(3,3) 
    #[(1,0,0),
    # (0,1,0),
    # (0,0,1)]
```

```python
    np.identity(3)
    #[(1,0,0),
    # (0,1,0),
    # (0,0,1)]
```

## Función Arange

Para _crear_ matrices rellenas con elementos **espaciados uniformemente**

Si necesitamos especificar un rango sin ubicar una cantidad de valores pero sí el **paso entre números** para nuestro array, podemos usar el método **arange**

```python
    spaces = np.arange(start = 1, stop = 10, step = 1)
    # [1,2,3,4,5,6,7,8,9]
```
Esta función excluye el número limite stop

Si queremos usar esta misma función para un array de dos dimensiones podríamos usar
```python
    np.arange(1, 10, 1).reshape((3,3))
    # [(1,2,3),
    # (4,5,6),
    # (7,8,9)]
```

## Funcion Linespace

Si necesitamos _especificar_ el **número de elementos** pero no el paso que deben contener los valores nuestro array podemos usar el método **linspace**

```python
    np.linspace(start = 0, stop = 100, num = 5)
    #[0,25,50,75,100]
```

 Si queremos excluir el valor stop dentro de nuestra secuencia podemos agregar un parámetro final en false

```python
    np.linspace(start = 0, stop = 100, num = 5, endpoint = False)
    #[0,25,50,75]
```


## Cambiar la forma de una matriz

```python
    a = np.array([
        (1,2,3),
        (4,5,6)
    ])
    # [1,2,3,
    #  4,5,6 ]

    a.reshape(3,2)
    # [1,2,
    #  3,4,
    #  5,6 ]

```

Este quiere decir que debe agrupar todos los elementos de la columna 2 a partir de la fila 0 en adelante

