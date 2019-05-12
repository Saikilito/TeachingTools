# Formularios con PHP

## Validaciones 

La validación de los input en un formulario son extremadamente importantes, porque nos aseguramos de que el usuario introdusca la información de la forma más certera posible y también tratamos de evitar lo más posible que generar alguna vulnerabilidad en nuestro sistema. 

## Variables super globales

* $_GET : Esta variable procura almacenar información que ha sido enviada desde un formulario por el metodo get como un array asociativo

* $_POST: Esta variable procura almacenar información que ha sido enviada desde un formulario por el metodo post

Esta variables capturaran información de las etiquetas que ocupan el envío por lo que es una técnica para identificar a que hace referencia cada información es ponerle un atributo "name" a cada input.