# HTML $& CSS

HTML es un lenguaje de marcado de etiquetas

Los lenguaje de marcado de etiquetas son sistemas de reglas para poder escribir.

## Estructura básica

Una estructura básica de html podría ser la siguiente:

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

Etiquetas comunes:

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

Las etiuquetas son fracmentos de texto readoados por corchetes angulares ```< >``` que tiene funciones y usos específicos

Los tributos afectan al elemto cuando estan presentes o enriquecen la definición de la misma.

```html
<html lang="es">Hola n_n</html>
```

## Las etiquetas meta 

Estas etiquetas se incoporan en el encabezado de una página web y que seultan invisbles para el visitante normal, pero son de gan utilidad para los navegadores, motores de buscades u otros programas que puedan valerse de esta información.

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