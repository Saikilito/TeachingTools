<h1 align="center">
    <img src="./img/redux.jpg">
    <br/>
Redux
</h1> 

## ¿ Qué es Redux ?

Es un contenedor de Estados Predecibles para aplicaciones Javascript.

La razón de Redux es para facilitar el manejo del Frontend, debido a la cantidad de opciónes y exigencias actuales para la creación de aplicaciones web.

## ¿ Cuándo usar Redux ?

No es necesario usar siempre Redux, este debe ser usado cuando manejamos una cantidad de información considerable dentro de nuestra aplicación, pero si tenemos una app muy sencilla usar Redux podría tener un efecto contrario al esperado.

## El Store

El centro y la verdad de todo, con métodos para actualizar, obtener y escuchar datos.

El Store centraliza toda la información acerca de los estados y se encarga de distribuir la información a los componentes que lo necesitan.

1. Contiene el estado de la
aplicación.

2. Puedes acceder al estado
con el método getState().

3. Puedes actualizar el
estado con el método
dispatch(action).

4. Escucha cambios con el
método subscribe(listener).

5. Dejar de escuchar
cambios retornando la
función del método
subscribe(listener).

## Acciones

Las Acciones son un bloque de información que **envía datos** desde la aplicación hacia el **Store**.


## Reducers

Los Reducers son los encargados de cambiar el estado de la aplicación.

## El flujo en Redux

<h1 align="center">
    <img src="./img/flujoredux.jpg">
    <br/>
</h1> 

El flujo de Redux se mueve en una sola dirección.


## Tres principios fundamentales

1. **La única fuente de la verdad**

El Store debe contener toda la información, por lo que para cada aplicación deberías tener un **único Store**

2. **El estado es de sólo lectura**

El Store debe ser el único que actualize la información de los estados.

3. **Los cambios se realizan con funciones puras**

Los Reducers son funciones, deben ser lo más sencilla posible y que sea facil de entender.
