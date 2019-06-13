<h1 align="center">Python</h1>

Una variable es simplemente el contenedor de un valor. Es una forma de decirle a la computadora de que nos guarde un valor para luego usarlo.

* Hay variables públicas, privadas y súper privadas

* Python es un lenguaje dinámico, este concepto de privado y público se genera por convenciones del lenguaje.

* En programación el signo = significa asignación.

* El _ al inicio del nombre de una variable quiere decir que esa variable es privada. Ejemplo: _age = 20

* El doble guion bajo al inicio del nombre de una variable quiere decir que esa variable no se puede modificar por nada del mundo. Ejemplo: __variable importante = “no tocar”

* Las variables en general pueden reasignarse o cambiarse el valor que contienen posteriormente

* Si una variable está en mayúscula, usualmente se refiere a una constante, no debería reasignarse o modificarse. Es una convención.

* Reglas de Variables:

    * Pueden contener números y letras
    * No deben comenzar con número
    * Múltiples palabras se unen con _
    * No se pueden utilizar palabras reservadas por Python, las cuales  son:

Nombres restringidos python.png
* Una expresión es una combinación de valores, variables y operadores.
* El intérprete evalúa expresiones. Ejemplo: 2 + 2

* Expresiones son instrucciones para el intérprete para que evalué la expresión.

* Un enunciado (statements) es una unidad de código que tiene un efecto dentro del programa. Ejemplo: una asignación ```age = 20```

* Los enunciados tienen efectos dentro del programa, como print que genera un output.

  * Orden de operaciones (de arriba hacia abajo):
  * Paréntesis
  * Exponente
  * Multiplicación
  * División
  * Adición
  * Sustracción

PEMDAS = Paréntesis, Exponente, Multiplicación, Adicción, Sustracción

> Para escribir comentarios en Python podemos usar el símbolo #

## Operadores lógicos: 

Sirven para realizar comparaciones, devuelven un valor verdadero o falso.

| Operador   |      Descripción      |  Ejemplo |
|----------|:-------------:|------:|
| and |  ¿se cumple a y b? | r = True and False entonces r es False |
| or |    ¿se cumple a o b?   |   r = True o False entonces r es True |
| not    | Not a     |    r = not True entonces r es False |

## Operadores relacionales: 

Comparan dos expresiones y devuelven un valor verdadero o falso.

| Operador   |      Descripción      |  Ejemplo |
|----------|:-------------:|------:|
| == | ¿Son iguales a y b? | r = 5 == 3 entonces r es False |
| != |    ¿Son distintos a y b?   |   r = 5 != 3 entonces r es True |
| < | ¿Es a menor que b? |    r = 5 < 3 entonces r es False |
| > | ¿Es a mayor que b? | r = 5 > 3 entonces r es True |
| <= | ¿Es a menor o igual que b? | r = 5 <= 5 entonces r es True |
| >= | ¿Es a mayor o igual que b? | r = 5 >= 3 entonces r es True |

## Loops

### For

```python
    foods = ['a','b',...,'z']

    for food in foods:
        print(food) #'a','b',...,'z'
```

```python
    num = 10

    while num <= 10:
        print(num)  #1,2,3,...,10
```

## Funciones 

### Definir una función
```python
    def hello():
        print("Hellow Word")

    hello()  #Hellow Word
```
### Parámetros en una función
```python
    def hello(name):
        print("Hellow" + name)

    hello("Joe")  #Hellow Joe
```

### Parametros con valores por defecto
```python
    def hello(name="Joe"):
        print("Hellow" + name)

    hello()  #Hellow Joe
```

### Retorno de valores

```python
    def add(n1,n2):
        return n1 + n2

    add(1,3)  #4
```

### Funcines lambdas

Son funciones que se escriben en una sola linea de codigo

```python
    add = lambda n1,n2 : n1+n2

    add(1,10) #11
```

## Módulos

Para importar módulos de alguna librería de Python podemos usar el siguiente código

```python
    import name_module

    name_module.method_module()
```

Si queremos usar específicamente algún método de este módulo podemos usar

```python
    from name_module import method_module

    method_module()
```

Usando esta forma ya no necesitamos invocar el método desde el nombre del módulo debido a que ya especificamos que viene directamente desde este.

### Usar módulos descargados

Desde la versión 3.6 Python ya viene incluido con su manejador de paquetes ```pip``` con el podemos descargar módulos desde PyPi

