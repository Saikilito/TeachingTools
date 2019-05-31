# Formularios con PHP

Para poder enviar información desde el cliente, la interface más popular es el uso de formularios.

En HTML este se basa generalmente en una etiqueta **form** llena de inputs y de algún botón tipo **submit** o de algún método que nos permita ejecutar la acción de enviar los datos.

Un formulario tiene el siguiente aspecto

```html
    <form action="file.php" method="method"> 
        <input type="text" name="name" placeholder="name"/>
        <input type="email" name="email" placeholder="email"/>
        <input type="password" name="password" placeholder="password"/>
        <button type="submit">Send Info</button>
    </form>
```

En la etiqueta **form** podremos diferenciar dos atributos:

1.  **action** en el debemos especificar cuál es la dirección del archivo que recibirá la información que enviemos en este formulario.

2. **method** en el debemos identificar cual será el método que usaremos para enviar los datos, generalmente se usan los métodos '**GET**' y '**POST**' pero existen algunos más.

En las etiquetas **input** nos interesa el ponerle un atributo **name** ya que cuando el servidor reciba los datos los asociará con el valor de este atributo y de esta manera podremos diferenciar que valor pertenece a cual input.

En la etiqueta **button** nos interesa agregar el atributo '**type="submit"**' ya que este es el que permitirá que al presionar el botón el formulario se "entere" y envíe los datos.

## Variables super globales

* $_GET : Esta variable procura almacenar información que ha sido enviada desde un formulario por el método ```get``` como un array asociativo.

Por ejemplo si enviamos un nombre por este método podemos preguntar por el usando la key: ```$_GET['name'] ```

* $_POST: Esta variable procura almacenar información que ha sido enviada desde un formulario por el método post.

Por ejemplo si enviamos un email por este método podemos preguntar por el usando la key ```$_POST['email']```

Esta variables capturaran información de las etiquetas que ocupan el envío por lo que es una técnica para identificar a que hace referencia cada información es ponerle un atributo "name" a cada input.

* $_SERVER

Esta variable “super global” nos ayuda a saber qué es lo que está pasando con el servidor

Por ejemplo.

Con la key ```$_SERVER['RESQUEST_METHOD']``` podemos preguntar si se ha enviado alguna información por algún método (GET o POST generalmente), esta devolverá un “string” con el nombre del método utilizado

## Recibir los datos enviados en el mismo archivo

Para lograr recibir los datos enviados por un formulario y recibirlos en el mismo archivo que lo ha ejecutado existen diversos métodos, uno de los métodos recomendados para este fin es :

```html
    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST"> 
        <!-- code ... -->
    </form>
```

* Con la función "**htmlspecialchars"" indicamos que no se aceptaran caracteres especiales, esto lo ocupamos como método de seguridad.

* Con la variable “super global” "**$_SERVER['PHP_SELF']**" indicamos la dirección, es decir el mismo archivo, donde recibiremos los datos enviados por el formulario


## Validaciones 

La validación de los input en un formulario son extremadamente importantes, porque nos aseguramos de que el usuario introduzca la información de la forma más certera posible y también tratamos de evitar lo más posible problemas con vulnerabilidades en nuestro sistema. 

## Sanitizadores

Los Sanitizadores usan un función llamada **filter_var** la cual recibe dos parámetros, el primero sería la variable a tratar y el segundo será el nombre del filtro.

```php

    filter_var($string_var, SANITIZER);

```

### **SANITIZE_STRING**

```php
    $string_var='<b>String without sanitizer</b>';
    filter_var($string_var , FILTER_SANITIZE_STRING); //String without sanitizer
```

Esta variable nos permite curar los “string” de modo que evitemos caracteres especiales dentro de nuestro código.
