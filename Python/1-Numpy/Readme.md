##INDICE
- [Usar Numpy en lugar de listas](#Usar-Numpy-en-lugar-de-listas)
- [Instalar Numpy](#Instalar-Numpy)
- [Cómo implementar Numpy](#C%C3%B3mo-implementar-Numpy)
  - [Definir un vector:](#Definir-un-vector)
  - [Definir una matriz:](#Definir-una-matriz)
- [Operaciones básicas de Numpy](#Operaciones-b%C3%A1sicas-de-Numpy)
  - [Multiplicar una matriz](#Multiplicar-una-matriz)
  - [Especificar el tipo de dato que contiene el Array:](#Especificar-el-tipo-de-dato-que-contiene-el-Array)
  - [Obtener el tipo de datos de una matriz](#Obtener-el-tipo-de-datos-de-una-matriz)
  - [Obtener las dimensiones](#Obtener-las-dimensiones)
  - [Obtener elementos de una columna](#Obtener-elementos-de-una-columna)
  - [Obtener el valor máximo y mínimo de una matriz](#Obtener-el-valor-m%C3%A1ximo-y-m%C3%ADnimo-de-una-matriz)
  - [Obtener la inversa de una matriz](#Obtener-la-inversa-de-una-matriz)
  - [Sumar todos los elementos de una matriz](#Sumar-todos-los-elementos-de-una-matriz)
  - [Cambiar la forma de una matriz](#Cambiar-la-forma-de-una-matriz)
- [Inicializar Matrices](#Inicializar-Matrices)
  - [Crear una Matriz identidad](#Crear-una-Matriz-identidad)
  - [Crear matrices rellenas con elementos "0"](#Crear-matrices-rellenas-con-elementos-%220%22)
  - [Crear matrices rellenas con elementos "1"](#Crear-matrices-rellenas-con-elementos-%221%22)
  - [Crear matrices rellenas con elementos aleatorios](#Crear-matrices-rellenas-con-elementos-aleatorios)
  - [Crear matrices rellenas con elementos vacíos](#Crear-matrices-rellenas-con-elementos-vac%C3%ADos)
  - [Crear matrices rellenas con elementos de un solo valor](#Crear-matrices-rellenas-con-elementos-de-un-solo-valor)
- [Función Arange](#Funci%C3%B3n-Arange)
- [Función Linespace](#Funci%C3%B3n-Linespace)

<h1 align="center">Numpy</h1>

Numpy es una librería de Python que significa “Numerical Python”, esta es la librería principal de este lenguaje para la informática científica proporcionando potentes estructuras de datos implementado matrices y matrices multidimensionales, estas estructuras de datos garantizan el cálculo de eficientes con matrices.

Numpy Array: Es un potente objeto de Matriz N-dimensional que tiene formas de filas y columnas.

## Usar Numpy en lugar de listas

* Numpy ocupa menos memoria en comparación a las listas de Python
* Numpy es mucho más rápido en términos de ejecución

## Instalar Numpy

??

## Cómo implementar Numpy

Para importar numpy por convención se hace de la siguiente manera

```python
import numpy as np
```

### Definir un vector:

```python
a =  np.array([1,2,3])  

print('1D array')
print(a)
```

### Definir una matriz:

```python
b = np.array([
    (1,2,3),
    (4,5,6)
])

print('2D array')
print(b)
```

## Operaciones básicas de Numpy

### Multiplicar una matriz
```python
    a = np.array([[1, 0], [2, -1]])
    np.dot(a, a)

    # array([[1, 0],
    #    [0, 1]])
```

### Especificar el tipo de dato que contiene el Array:

```python
    a = np.array([
        (1,2,3),
        (4,5,6)
    ],
    dtype=np.int64)
```

### Obtener el tipo de datos de una matriz

```python
    a = np.array([1,2,3],[4,5,6])
    a.dtype # int64
```

### Obtener las dimensiones

```python
    a = np.array([1,2,3],[4,5,6])
    a.shape # (2,3)
```

### Obtener elementos de una columna

```python
    a = np.array([
        (1,2,3),
        (4,5,6)
    ])

    a[0:,2] # [3,6]
```

Este caso se podría leer como *"obtener desde la fila 0 todos los elementos de la columna 2"*

### Obtener el valor máximo y mínimo de una matriz

```python
    a = np.array([
        (1,2,3),
        (4,5,6)
    ])

    a.max() #6
    a.min() #1
```

### Obtener la inversa de una matriz

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

### Sumar todos los elementos de una matriz

```python
    a = np.array([
        (1,2,3),
        (4,5,6)
    ])

    a.sum() #21
```

### Cambiar la forma de una matriz

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

## Inicializar Matrices

### Crear una Matriz identidad

```python
    np.eye(3) 
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

### Crear matrices rellenas con elementos "0"

```python
    fill = 2
    column = 2
    ones = np.zeros(fill,columns)
    # [(0,0),
    #  (0,0)]
```

### Crear matrices rellenas con elementos "1"

```python
    fill = 2
    column = 2
    ones = np.ones(fill,columns)
    # [(1,1),
    #  (1,1)]
```

### Crear matrices rellenas con elementos aleatorios

```python
    fill = 2
    column = 2
    ones = np.random.random(fill,columns)
    # [(0.465,0.6879),
    #  (0.889,0.144)]
```

### Crear matrices rellenas con elementos vacíos

```python
    fill = 2
    column = 2
    ones = np.empty(fill,columns)
    # [(0.,0.),
    #  (0.,0.)]
```

### Crear matrices rellenas con elementos de un solo valor

```python
    fill = 2
    column = 2
    num = 8
    ones = np.full((fill,columns),num)
    # [(8,8),
    #  (8,8)]
```

## Función Arange

Para crear matrices rellenas con elementos espaciados uniformemente

Si necesitamos especificar un rango sin ubicar una cantidad de valores pero sí el paso entre números para nuestro array, podemos usar el método arange

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

## Función Linespace

Si necesitamos especificar el número de elementos pero no el paso que deben contener los valores nuestro array podemos usar el método linspace

```python
    np.linspace(start = 0, stop = 100, num = 5)
    #[0,25,50,75,100]
```

 Si queremos excluir el valor stop dentro de nuestra secuencia podemos agregar un parámetro final en false

```python
    np.linspace(start = 0, stop = 100, num = 5, endpoint = False)
    #[0,25,50,75]
```