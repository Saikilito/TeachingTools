# Composer

**Composer** es un manejador de dependencias, el, entre otras cosas, nos ayuda a traer librerias de terceros a nuestros proyecto. Muchas de la librerias escritas para PHP se pueden encontrar dentro de la web [ Packagist ](www.packagist.org) que es la página oficial en donde podemos referirnos de manera confiable.

Para trabajar con composer es importante tener en cuenta que debemos descargarlo en nuestra computadora e instalarlo en cada proyecto que queramos utilizarlo, el procedimiento varía teniendo en cuenta el sistema operativo. 

## Para instalar

1. Para el caso de windows podemos descargarlo desde aquí: [Composer Windows](https://getcomposer.org/Composer-Setup.exe) 
2. Al instalar nos pedira la ruta de la carpeta en donde tengamos instalado nuestro php (generalmente esta dentro del servidor local que estemos usando al momento).
3. Luego de instalarlo debemos reiniciar la terminal (o CMD).
4. En nuestra terminal debemos ubicarnos en la carpeta del proyecto donde lo queremos instalar.
5. Usamos el siguiente comando 
``` $composer install ```

Antes de tener en cuenta las funciones de composer es importante hacer mención de lo que se conoce como la **PHPFIG**, estos son un grupo de desarrolladores dedicados a la creación de estandares en PHP, esto lo hacen con fín de optimizar el manejo y uso del software y librerías que se puedan dar en este lenguaje, dentro de los estandares conocidos podremos ver algunos como:

* PSR-4 
* PSR-7 

## **Autoloader PSR-4** 

Dentro del estandar PSR-4 existe lo que se conoce como **autoloader** el cual nos permite tener un autocargado automatico de archivos a partir de los namespace.

Si usamos la convención para los **namespace** de ponerles el nombre dependiendo del nivel de ruta donde se encuentren, automaticamente podemos cargalos al implementar el **use** evitando así tener que usar **require** para cada archivos.

La forma de configurar esto dentro de nuestro archivo "composer.json" es la siguiente:

debemos tener el siguiente codigo

```js
{
    "autoload":{
        "psr-4":{
            "namespace_name\\":"main_directory_path/"
        }
    },
}
```

Dentro del objeto "psr-4" debemos especificar el namespace y asignarle una ruta, ambos referentes al primer directorio desde donde composer debe empezar a buscar.

Luego de esto debemos ejecutar la siguiente linea dentro de nuestro CMD:

```
$ composer install
```

Adicional a esto debemos saber que en nuestra carpeta **vendor** se creara un archivo con el nombre de "**autoload.php**" este archivo es el que contendra todas las rutas asociadas a los **namespace** y debe ser cargado con un **require** dentro de las líneas principales de nuestra aplicación para poder hacer uso del autocargado.

## Laravel Eloquent (ORM)
Eloquen es un **ORM** que permite trabajar con diferentes tipos de bases de datos como MySQL, Postgress, SQLite, entre otros...

Eloquen se instala mediante composer bajo los siguientes comandos:

    $ composer require illuminate/database

Luego de instalar configuramos un objeto parecido a este.

```php

use Illuminate\Database\Capsule\Manager as Capsule;
use Illuminate\Database\Eloquent\Model ;

class Class_Name extends Model {

    protected $table ='name_table';
    //code...
}

$capsule = new Capsule;

$capsule->addConnection([
    'driver'    => 'mysql',
    'host'      => 'localhost',
    'database'  => 'database_test',
    'username'  => 'root',
    'password'  => 'root',
    'charset'   => 'utf8',
    'collation' => 'utf8_unicode_ci',
    'prefix'    => '',
]);


// Configura la vairbale capsule como global
$capsule->setAsGlobal();
// Inicializa la variable
$capsule->bootEloquent();

if(!empty($_POST))
{
    $new_object = new Class_name();
    $new_object->character = $_POST['title'];
    $new_object->save();
}

```

Con esta simple configuración ya estariamos guardando información dentro de la base de datos.

* Para guardar toda la información de una tabla como un objeto podemos invocar el siguiente metodo de eloquent

```php
    $var = Model_Name :: all();
```

## Zend-Diactoros (PSR-7)

PSR-7 posee un estandar que nos permite normalizar el funcionamiento de **resquests** y **responses** dentro de una aplicación. En este caso **zend-diactoros* es una interfase para el **manejo de estructuras HTTP**

Para instalar podemos usar el siguiente comando:

``` 
    $ composer require zendframework/zend-diactoros 
```

Una de las cosas que nos permite esta librería es manejar las variables super-globales desde una sola variable para ello podemos usar el siguiente condigo.

```php
$request = Zend\Diactoros\ServerRequestFactory::fromGlobals(
    $_SERVER,
    $_GET,
    $_POST,
    $_COOKIE,
    $_FILES
);
```

Esta variable "**$request**" también nos permite conocer la ruta **URL** en la cual nos encontramos al ejecutar el script con la siguiente línea:

```php  
    $request->getUri()->getPath() ;
```

Si queremos obtener el methodo que se esta usando una peticion

```php  
    $request->getMethod() ;
```

Si queremos obetener el cuerpo de los datos enviados en una petición podemos usar:

```php  
    $requets->getParsedBody() ; //return an asosiative array
```


## Aura/Router (PSR-7)

Como bien lo infiere el nombre es una libreria para la gestion de rutas.

>Requiere tener instalado **zend-diactoros**

Para instalar podemos usar el siguiente comando:

``` 
    $ composer require aura/router 
```

Para implementar un router podemos escribir el siguiente código

```php

use Aura\Router\RouterContainer;

$routerContainer = new RouterContainer();

//Get map form routerContainer
$map = $routerContainer->getMap();

$map->get('name_get','path_url',$handler);
$map->post('name_pots','path_url',$handler);
$map->delete('name_delete','path_url',$handler);

//Compare the object requets with our map
$matcher = $routerContainer->getMatcher();

$route = $matcher->match($request);

```

* Tener en cuenta:

1. El objeto "**$request**" que se usa en la última línea proviene del manejador creado en la librería de **zend-diactoros**

2. La variable "**$handler**" que se pasa como tercer parametro generamente la usamos para indicarle al manjeador la ruta donde se encuentra el archivo con el cual debemos reponder a la petición http.

3. La variable "**$handler**" puede ser accedida dentro del objeto "**$router**" usando "**$router->handler**"

4. La variable "**$handler** puede responder bien si le asignamos un string que apunte a la ruta donde se encuentra el archivo con el que queremos responder, pero realmente **podemos pasar cualquier cosa que nosotros queramos** como por ejemplo una array o un objeto.


## Respect/Validation (Validación de formularios)

Para instalarlo :
```
    $ composer require respect/validation
```



