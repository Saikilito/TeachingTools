## ÍNDICE
1. [HTML](#HTML)
2. [CSS](#CSS)
3. [Javascript](#Javascript)

<h1 align="center"> HTML</h1>

HTML es un lenguaje de marcado de etiquetas

Los lenguajes de marcado de etiquetas son sistemas de reglas para poder escribir.

## Estructura básica

Una estructura básica de HTML podría ser la siguiente:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta description="my awesome website"">
    <title>Título de mi primera página</title>
</head>
<body>
</body>
</html>
```
Para entenderlo debemos ir conociendo algunos conceptos

**Etiquetas comunes:**

```html
<h1></h1>
<h2></h2>
<h2></h2>

<div></div>
<!-- Contenedor de elementos con algunos pocos formatos -->

<span></span>
<!-- Contenedor de elemntos que no cumple con ningun formato -->

<p></p>
```

## Etiquetas y atributos

Las etiquetas son fragmentos de texto rodeados por corchetes angulares ```< >``` que tiene funciones y usos específicos

Los tributos afectan al elemento cuando están presentes o enriquecen la definición de la misma.

```html
<html lang="es">Hola n_n</html>
```

## Las etiquetas meta 

Estas etiquetas se incorporan en el encabezado de una página web y que resultan invisibles para el visitante normal, pero son de gran utilidad para los navegadores, motores de buscadores u otros programas que puedan valerse de esta información.

```html
<head>
    <meta name="description" content="My awesome website">
</head>
```

## Otras etiquetas comunes
```html
<img src="url_img" alt="description_img"/>
<!-- Sube para poner imagenes dentro de nuestra pagina -->
<!-- Quizas encuentres algunos gif interesantes en https://giphy.com/ -->
<a href="www.pagina_linkeada">
```

<h1 align="center"> CSS</h1>

Podemos referirnos a CSS (Cascading Style Sheets) como hojas de estilo en cascada en español.

Éstas definirán la apariencia de nuestra página, pues si bien con HTML ya podemos crear estructuras también nos veremos en la necesidad de darle una buena presencia a nuestra web.

Dentro de nuestro HTML para poder llamar a una hoja de estilos (archivos con terminación '.css') podemos usar la etiqueta link de la siguiente manera:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta description="my awesome website"">
    
    <!-- Usando la etiqueta link -->
    <link rel="stylesheet" href="path_file.css">

    <title>Título de mi primera página</title>
</head>
<body>
</body>
</html>
```

Se llama hojas de estilo en cascada porque las ```"clases"``` que son las reglas con las que definiremos nuestros estilos se van anidando hacia adentro, un ejemplo de una clase podría verse de la siguiente manera

```css
.box{
    height: 100px;
    width: 100px;
    background:red;
}
```
## Selectores

Los selectores nos permiten conectar un elemento de HTML con un estilo de CSS, esta conexión nos permite definir que elemento específico tendrá cual estilo o forma que nosotros decidamos

### **Selectores de tipo clase** 

Buscan un elemento basado en el contenido del atributo ```class``` de las etiquetas, es decir, dentro de alguna(s) etiqueta(s) HTML tendremos el atributo ```class``` igualado al valor de un nombre que a su vez dentro de nuestro archivo CSS tendra el mismo nombre precedido por un '.', de esta manera lograremos hacer que los dos conecten y los estilos sean recibidos por elemento que queremos. 

Tomando el ejemplo anterior:

```css
/* Here your CSS */
.box{
    height: 100px;
    width: 100px;
    background:red;
}
```

Podemos usar esta clase, por ejemplo en un elemento div

```html
<!-- Dentro del body de nuestro archivo HTML escribimos -->
<div class="box"><div>
```

Y obtendríamos un cuadrado de '100px X 100px' con un color de fondo rojo, pero estas propiedades las iremos aprendiendo poco a poco.

### **Selectores de tipo ID** 

Hacen lo mismo que los los Selectores de clases, con la diferencia de que estos referencian los elementos de HTML por el atributo id y dentro de nuestro archivo CSS su nombre ira precedido por un '#'

Modificando un poco el ejemplo anterior:
```css 
#box{
    height: 100px;
    width: 100px;
    background:red;
}
```

```html
<!-- Dentro del body de nuestro archivo HTML escribimos -->
<div id="box"><div>
```

Pero el atributo ```id``` tiene una particularidad, y es que dentro de HTML **no es correcto tener dos elementos con el mismo 'id'**, mientras con por ejemplo con el atributo ```class``` podemos tener cuantos elementos con el mismo valor en el atributo 'class' como nosotros queramos.

### Atributos dentro de las clases

Cada clase contiene atributos, estos atributos definen los estilos que emplea cada clase. 

Por ejemplo:

```css
#box{
    height: 100px;
    width: 100px;
    background:red;
    color:white;
    padding:10px;
    font-size:20px
}
```
Estos atributos:
* ```height``` define una altura para el elemento de de 100px
*  ```width``` es el atributo que define el ancho del elemento en este 100px también.
*  ```background``` es el atributo que definirá el color de fondo para el elemento
*  ```color``` es el atributo que define el color de las letras dentro del elemento.
*  ```padding``` es el atributo que define el espacio interior que tendra cada elemento.
*  ```font-size``` es el atributo que define el tamaño de la tipografía.

El elemento HTML que contenga el ```id="box"```  heredará estas propiedades.

Otra manera para ingresar estilos dentro de nuestro HTML sin usar la etiqueta ```link``` podría ser usar la etiqueta ```style``` dentro del ```head``` de nuestro HTML y escribir directamente nuestros estilos sin la necesidad de “linkear” ningún archivo.

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta description="my awesome website"">
    <title>Título de mi primera página</title>
    <style>      
       /* Here your rules that CSS */
       #box{
        height: 100px;
        width: 100px;
        background:red;
        color:white;
        padding:10px;
        font-size:20px
        }
    </style>
</head>
```

Esto no es recomendado para proyectos reales pero puede ser útil en ciertas ocasiones y vale la pena conocer que existe esta opción. 

<h1 align="center"> Javascript</h1>

Es un lenguaje de programación que te permite realizar actividades complejas en una página web.

A él le vamos a delegar la mayor parte de interactividad, dinamismo y consulta de información, así como también nos permite almacenar valores útiles dentro de variables, en el mundo web el manejo de información es una de las cosas más importante que existe y esto lo vamos a administrar con este lenguaje.

Para entender Javascript debemos conocer la existencia del objeto DOM (Document Object Model) que vive dentro del navegador.

Cuando nuestro navegador “renderiza” nuestra web, este reconoce las estructuras esenciales con la que está construida, y sabe también como todos los elementos estan representados y jerarquizados como si fueran las partes de un árbol.

Esta estructura jerárquica tiene más o menos la siguiente forma:

```
--DOM
---HTML
----BODY
-----ELEMENT1
------ELEMENT1.2
------ELEMENT1.2
-----ELEMENT2
------ELEMENT2.1
```
Éste árbol es el DOM, es decir, como se jerarquiza todo lo que tiene que ver con tu sitio web y tiene muchas más características de las que podemos ver y **Javascript** tiene conexión directa con el DOM y esto permite un manejo poderoso del mismo y es gracias ello que podemos crear tanta interactividad en nuestro sitio.

Dentro de nuestro HTML para poder llamar a un “Script” de **Javascript** (archivos con terminación '.js') podemos usar la etiqueta script de la siguiente manera:

```html
<body>
    <script src="path_file.js"></script>
</body>
```

Dentro del atributo ```src``` pondremos la dirección en la que se encuentra nuestro archivo **Javascript**.

Para probar nuestra primera línea de código en Javascript (js) crearemos un archivo (con terminacion de nombre .js) y dentro escribiremos el siguiente código:

```javascript
// Here your code in javascript
var a = 'Hola';
var b = 'Mundo';

alert(a + ' ' + b);
```
> La palabra reservada ```var``` se usa para indicar la definición de una variable
> La palabra reservada ```alert``` se usa para llamar a una función

Si hemos “linkeado” correctamente nuestro archivo podremos representar en pantalla un mensaje de alerta que dirá ```"Hola Mundo"```