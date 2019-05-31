<h1 align="center">Template Engine</h1>

Un “Template Engine” es un motor para renderizar HTML.

El desarrollo propiamente dicho de PHP se ha enfocado sobre todo en el área de la programación, dejando un poco de lado su propia estructura para el manejo de HTML, es por eso que es una buena opción utilizar algún témplate que nos permita manejar mejores características para trabajar.

Una ventaja de usar un “template engina” (TE) es que al usar una sintaxis diferente, evita las tentaciones de mezclar el código de PHP con el HTML, consiguiendo así más modularidad y creando mayor independencia en cuanto a las vistas en nuestro modelo.

Entre otras ventajas:

* Ayuda con temas de seguridad
* Permite incluir “templates” externos dentro de nuestros “templates”
* Permite la herencia entre “templates”

## Twig

Para instalar Twig

```
$ composer require twig/twig
```

Para configurar twig

```php

    require_once '/path/to/vendor/autoload.php';

    $loader = new \Twig\Loader\FilesystemLoader('/path/to/  templates');
    $twig = new \Twig\Environment($loader, [
        'cache' => '/path/to/compilation_cache',
    ]);

    
```

Luego para renderizar una vista podemos usar :

```php

    $template = $twig->load('index.html');
    echo $template->render(['the' => 'variables', 'go' => 'here']);

```
O podemos rendezar y cargar el archivo a mostrar en una misma linea

```php

echo $twig->render('index.html', ['the' => 'variables', 'go' => 'here']);

```

## Trabajando con las plantillas de Twig

### Uso de variables

Para poder utilizar las **variables** en Twig no está permitido usar sintaxis PHP lo que podemos hacer es llamar las variables usando la siguiente sintaxis

```twig
    <h1>{{ variable }}</h1>
```
>La variable se llamara dentro de la plantilla sin necesidad de usar el "**$**"

### Uso de ciclo for

Ejemplo:

```twig
<h1>Members</h1>
<ul>
    {% for user in users %}
        <li>{{ user.username|e }}</li>
    {% endfor %}
</ul>
```

### Twig y PSR-7

Dentro de la librería “Zend-Diactoros” podemos encontrar una respuesta correcta que sea compatible con HTML esto es :

```php
    use Zend\Diactoros\Response\HTMLResponse;
```

Con ella podmos envolver a Twig de la siguiente manera:

```php
    return HTMLResponse($twig->render('index.html', ['the' => 'variables', 'go' => 'here']));
```

Supongamos que quien retorna la línea anterior es una función "renderHTML" que creamos nosotros, ahora podemos recibirla y pintarla en pantalla de la siguiente manera:

```php
    $response = renderHTML();
    echo $response->getBody();

```

De esta forma nuestro código maneja un estándar PSR-7

## Crear un Layout en Twig

Para el archivo contenedor
```twig

<!-- htmlCode -->
        {% block name_block %}
        {% endblock %}

<!-- htmlCode -->

```

Para el archivo contenido
```twig
{% extends "layour_path" %}

{% block name_block %}

    <!-- htmlCode -->

{% endblock %}

```