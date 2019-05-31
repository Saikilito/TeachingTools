# Composer

**Composer** es un manejador de dependencias, el, entre otras cosas, nos ayuda a traer librerías de terceros a nuestros proyecto. Muchas de la librerías escritas para PHP se pueden encontrar dentro de la web [ Packagist ](www.packagist.org) que es la página oficial en donde podemos referirnos de manera confiable.

Para trabajar con “composer” es importante tener en cuenta que debemos descargarlo en nuestra computadora e instalarlo en cada proyecto que queramos utilizarlo, el procedimiento varía teniendo en cuenta el sistema operativo. 

## Para instalar

1. Para el caso de “Windows” podemos descargarlo desde aquí: [Composer Windows](https://getcomposer.org/Composer-Setup.exe) 
2. Al instalar nos pedirá la ruta de la carpeta en donde tengamos instalado nuestro PHP (generalmente está dentro del servidor local que estemos usando al momento).
3. Luego de instalarlo debemos reiniciar la terminal (o CMD).
4. En nuestra terminal debemos ubicarnos en la carpeta del proyecto donde lo queremos instalar.
5. Usamos el siguiente comando 
``` $composer install ```

Antes de tener en cuenta las funciones de “composer” es importante hacer mención de lo que se conoce como la **PHPFIG**, estos son un grupo de desarrolladores dedicados a la creación de estándares en PHP, esto lo hacen con fin de optimizar el manejo y uso del software y librerías que se puedan dar en este lenguaje, dentro de los estándares conocidos podremos ver algunos como:

* PSR-4 
* PSR-7 

## **Autoloader PSR-4** 

Dentro del estándar PSR-4 existe lo que se conoce como **autoloader** el cual nos permite tener un auto-cargado de archivos a partir de los “namespace”.

Si usamos la convención para los **namespace** de ponerles el nombre dependiendo del nivel de ruta donde se encuentren, automáticamente podemos cárgalos al implementar el **use** evitando así tener que usar **require** para cada archivos.

La forma de configurar esto dentro de nuestro archivo "composer.json" es la siguiente:

Debemos tener el siguiente código :

```js
{
    "autoload":{
        "psr-4":{
            "namespace_name\\":"main_directory_path/"
        }
    },
}
```

Dentro del objeto "psr-4" debemos especificar el “namespace” y asignarle una ruta, ambos referentes al primer directorio desde donde “composer” debe empezar a buscar.

Luego de esto debemos ejecutar la siguiente línea dentro de nuestro CMD:

```
$ composer install
```

Adicional a esto debemos saber que en nuestra carpeta **vendor** se creara un archivo con el nombre de "**autoload.php**" este archivo es el que contendrá todas las rutas asociadas a los **namespace** y debe ser cargado con un **require** dentro de las líneas principales de nuestra aplicación para poder hacer uso del auto-cargado.

## Laravel Eloquent (ORM)
Eloquen es un **ORM** que permite trabajar con diferentes tipos de bases de datos como MySQL, Postgress, SQLite, entre otros...

Eloquen se instala mediante “composer” bajo los siguientes comandos:

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

* Para guardar toda la información de una tabla como un objeto podemos invocar el siguiente método de ```eloquent```

```php
    $var = Model_Name :: all();
```

## Zend-Diactoros (PSR-7)

PSR-7 posee un estandar que nos permite normalizar el funcionamiento de **resquests** y **responses** dentro de una aplicación. En este caso **zend-diactoros* es una interfase para el **manejo de estructuras HTTP**

Para instalar podemos usar el siguiente comando:

``` 
    $ composer require zendframework/zend-diactoros 
```

Una de las cosas que nos permite esta librería es manejar las variables súper globales desde una sola variable para ello podemos usar el siguiente condigo.

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

Si queremos obtener el método que se está usando una petición, podemos usar:

```php  
    $request->getMethod() ;
```

Si queremos obtener los “headers” enviados 

```php
    $request->getHeaders()
```

Si queremos obtener el código de respuesta del servidor

```php
    $request->getStatusCode()
```

Si queremos obtener el cuerpo de los **datos enviados** en una petición, podemos usar:

```php  
    $request->getParsedBody() ; //return an asosiative array
```

Si queremos obtener el cuerpo de los **archivos subidos** en una petición, podemos usar: 

```php  
    $request->getUploadedFiles() ; //return an asosiative array
```

Si queremos saber si un (o los) **archivo** se subió **sin problemas**, podemos usar:

```php  
    $files = $request->getUploadedFiles() ; 

    $element_file = $files['file_name'];

    $element_file->getError()//If it's ok return a const UPLOAD_ERR_OK

    // if($element_file->getError() == UPLOAD_ERR_OK) ...
```

Si queremos obtener el **nombre** de un **archivo** que se cargó sin error, podemos usar:

```php
    if($element_file->getError() == UPLOAD_ERR_OK){
        $fileName = $element_file->getClientFilename();
    }
```

Si queremos **mover** de directorio un **archivo** que se cargó sin error, podemos usar:

```php
    if($element_file->getError() == UPLOAD_ERR_OK){
        element_file->moveTo('path');
    }
```

Mover un archivo es importante debido que al cargarlos estos se alojan en un espacio de memoria hasta que se decide dónde debe ser alojado.

Debemos tener en cuenta que la carpeta donde vamos a alojar nuestros archivos subido debe existir y además debe tener permisos de escrituras, en un servidor con Linux podemos configurar estos permisos desde la terminar usando el comando:

```
    $   chmod 777 name_directory/
```
Ten en cuenta que debes estar ubicado en donde se encuentra la carpeta

>Este comando es válido en Linux y en Mac

## Aura/Router (PSR-7)

Como bien lo infiere el nombre es una librería para la gestión de rutas.

>Requiere tener instalado **zend-diactoros**

Para instalar podemos usar el siguiente comando:

``` 
    $ composer require aura/router 
```

Para implementar un “router” podemos escribir el siguiente código

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

2. La variable "**$handler**" que se pasa como tercer parámetro generalmente la usamos para indicarle al manejador la ruta donde se encuentra el archivo con el cual debemos responder a la petición http.

3. La variable "**$handler**" puede ser accedida dentro del objeto "**$router**" usando "**$router->handler**"

4. La variable "**$handler** puede responder bien si le asignamos un “string” que apunte a la ruta donde se encuentra el archivo con el que queremos responder, pero realmente **podemos pasar cualquier cosa que nosotros queramos** como por ejemplo una array o un objeto.

## Respect/Validation (Validación de formularios)

Para instalarlo :
```
    $ composer require respect/validation
```

Para usar en un archivo se llama por convención a :

```php
    use Respect\Validation\Validator as v ;
```

* Valiandando arrays

1. Cadena no vacia
```php
    $arrayData = [/*...,data,...*/];
    
    $array_val = v::key('assosiative_name', v::stringType()->notEmpty());
    $array_val->validate($arrayData);//If it's ok then return true 
```

2. Validar varios elementos del mismo array
```php
    $arrayData = [/*...,data,...*/];
    
    $array_val = v::key('assosiative_name1', v::stringType()->notEmpty())
        ->key('assosiative_name2', v::stringType()->notEmpty());
    $array_val->validate($arrayData);//If it's ok then return true
```

Podemos concatenar validadores, en este caso, llamandolos continuando los "**key**" despues de una "**->**".

* Manejando Excepciones

Cuando validamos es común querer hacerlo dentro de **try/catch** para manejar las excepciones.

Si en lugar de “validate” usamos **assert**, validaremos también pero de igual forma tendremos acceso a información sobre el por qué el usuario no está pasando la validación.

```php

    try{
        $arrayData = [/*...,data,...*/];
        
        $array_val = //code validation ;
        $array_val->assert($arrayData);
    }
    catch(\Exception $e){
        $responseMessage = $e->getMessage();
    }
```

Al usar ```\Exception``` lo que estamos indicando es que en una jerarquía de herencia usaremos la jerarquía más alta posible para lograr capturar los errores producidos en el try/catch.

## vlucas/phpdotenv (Variables de entorno)

Al instalar esta librería podremos disponer de variables de entorno para poder cuidar de información sensible antes de hacer un “deploy” o para poder compartir en el código de manera segura.

Se debe crear un archivo de extensión "**.env**" en la raíz del proyecto, dentro de él podemos escribir la variables que queremos manejar de la forma ```VAR="value"```, no es necesario utilizar "**;**". Luego debemos usar el siguiente código dentro de nuestro proyecto para indicar donde tenemos alojado nuestro archivo "**.env**"

```php
    $dotenv = Dotenv\Dotenv::create(__DIR__ . '/..' );
    $dotenv->load();
```
Luego podremos disponer de cualquier variable con solo ejecutar la siguiente función.

```php
    getenv('VAR`);
```

> Por convención los nombres de las variables de entorno se escriben en mayúsculas.

