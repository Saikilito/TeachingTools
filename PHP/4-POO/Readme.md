# Programación Orientada a Objetos

La programación orientada a objetos es un paradigma de programación donde se busca ser análogo a las partes de una aplicación como parte de un conjunto de objetos.

## Clases

Pueden ser consideradas el molde desde donde vamos a crear los objetos

Se definen de la siguiente manera :

```php

    class Class_name(){
        //code...
    }

```

>Por convención los nombres de las clases se escriben empezando con una letra mayúscula

Para crear una clase con atributos podemos hacer de la siguiente manera :

```php

    class Class_name(){
        public $attribute1; 
        public $attribute2;
        public $attribute3;
    }

```

>Los atributos se comportan como variables dentro de las clases.

## Instanciar

Instanciar una clase es crear un tipo de objeto que nace desde esa clase, de una misma clase podemos crear infinidades de objetos unicos y todos con las mismas propiedades asignadas por su clase : 

```php

    class Class_name(){
        public $attribute1; 
        public $attribute2;
        public $attribute3 = true;
    }

    $Some_object = new Class_name();

```
>   Es posible darle valores por defecto a los atributos de las clases con tan solo asginarle el valor directamente en la definición del mismo


Para asignar valores al atributo de algún objeto podemos usar : 

```php

    $Some_object = new Class_name();

    $Some_object->attribute1 = 'random_val1';
    $Some_object->attribute2 = 'random_val2';

```

Los objetos tambien nos permiten usar **Modificadores de niveles de acceso** para sus atributos : 

```php

    class Class_name(){
        public $attribute1; 
        private $attribute2;
        protected $attribute3;
    }

```

**public** : otorga acceso a entidades fuera de la clase para que puedan usar sus atrivitos o metodos.

**private** : niega el acceso a entidades fuera de la clase para que puedan usar sus atributos o metodos.

**protected** : otorga el acceso solo a clases que hereden de el pero lo niega al resto de entidades.

### Metodos

Dentro de las clases tambien podemos definir funciones, una funcion declarada dentro de un objeto obtiene el nombre de "metodo del objeto"

```php

    class Class_name(){
        public $attribute1; 
        private $attribute2 = true;

        public function name_of_method($par){
            $this->$attribute1 = $par ;
            //code . . .
        }
    }

```

>Para poder hacer referencia a un atributo de la clase dentro de un metodo es necesario usar " $this " cual es el objeto interno que representa a la clase.

### Metodos mágicos

En PHP dentro de la clases existen os llamados metodos magicos, los cuales cumplen funciones especiales para trabajar con los objetos.

* Constructor

El constructor nos provee una forma de instaciar un objeto dandole valores directamente en una única linea, este nos facilita la tarea de tener que asignarle valores a cada atributo: 

```php

    class Class_name(){
        public $attribute1; 
        public $attribute2;

        public function __construct($attr1,$attr2{
            $this->attibute1 = $attr1;
            $this->attribute2 = $attr2;
        })
    }

    $Object_with_construct = new Class_name("val1","val2");

```

## Herencia

En PHP solo podemos usar Herencia sencilla, es decir, cada clase solo puede heredar de un unico padre.

```php
class Class_Father {
    //code...
}

class Class_Children extends Class_Father {
    //code...
}

```

## Polimorfismo

Existen varios tipos de polimorfismo :


* Si dentro de la clase hijo declaramos un metodo con el mismo nombre de un metodo declarado en la clase padre estaremos **sobrescribiendo el meotodo**, esto nos puede servir para definir comportamientos diferentes dentro de cada clase hijo.


* **Si creamos un constructor dentro de la clase hijo** estaremos sobrescribiendo el constructor de la clase padre y este dejara de funcionar a menos de que de lo llamemos de la siguiente manera : 

```php
public function __construct($title, $description) {
            parent::__construct($title, $description);

            
}
```

## Interfaces de objetos

Una interface es un modelo que intenta estandarizar ciertos aspectos de nuestras clases. Las interfaces garantizas que ciertas funciones o clases empleen obligatoriamente algunas caracteristicas.

```php

    interface Name_Interface {
        //... code characteris 
    }

```

Luego en una clase la usariamos de la siguiente manera: 

```php

    class Name_Class extends Father_Class implements Name_Interface {
        //... code characteris 
    }

```
> Usando la palábra reservada implements aseguramos que esta clase mantenga los requrimientos de las clases

> Si implementamos una interface en una clase padre los hijos heredaran diche interface


Por ejemplo, si quisieramos que todas las clases implementaran una funcion:

```php

    interface Name_Interface {
        public function name_function();
    }

```

Entonces las clases que implementen esta interface necesariamente deberan tener un metodo  "name_function" obligatoriamente.

Una interface tambien se puede usar para que las funciones esperen cierto tipo de datos por ejemplo.

```php

    function name_function(Name_Interface $var){
        //code...
    }
```

A partir de aqui todos los parametros que entren por la variable "$var" deberan cumplir las reglas de las interfaces.

## Namespace

El namespace se usa para solucionar problemas entre coliciones de nombres.

Imagina que estas declarando una clase llamada "Project" y luego intentar usar una libreria que tambien implementa una clase con el mismo nombre. Este tipo de problemas los solucionamos con namespace.

Por ejemplo, imaginemos la siguiente estructura de archivos:

    /index.php
    /---/project1/
        /---anythings.php
        /---Project.php
    /---/project2/
        /---Project.php

Ahora en cada archivos tendriamos lo siguiente:

* Para index.php

    ```php
    <?php

        require('project1/Project.php');
        require('project1/anythings.php');
        require('project1/Project.php');

        use project1\{Project,anything};

        $P1 = new Project();
        $P2 = new project2\Project();
    
    <?
    ```
        
* Para project1/Project.php

    ```php
    <?php
        
        namespace project1;

        class Project {
            //...code
        }

    <?
    ```

* Para project2/Project.php

    ```php
    <?php
        namespace project2;

        class Project {
            //...code
        }
    ?>
    ```

* Para project1/anythings.php

```php
    
    namespace project1;

    //code...

```

Notece los siguientes aspectos.

1. namespace es la primera linea declarada en el archivo
2. En index.php se llama a dos archivos que tienen el mismo name space con la palabra reservada 'use' encerrando ambas en llaves y separandolas cada una con comas
3. Los namespace se nombran dependiendo del nivel de la carpeta y separando los niveles con '\'
4. La declaracion del objeto llamado "$P1" usa la forma implicita del namespace debido a la palabra reservada "use".
5. La declaracion del objeto llamado $P2" usa la forma explicita del namespace debido a que ya existe una declaración de "Project" de forma implicita.

>Los **namespace** viven dentro solo dentro de cada bloque de script, al detertar un " ?> " Se acaba el ambito del namespace así dentro de cada archivo pueden existir mas de un namespace

Ejemplo para nombrar a un namespace debajo de varias carpetas:

Supongamos la siguiente estructura de archivos

    /index.php
    /---/file1/
        /---file1.php
        /---file2/
            /---file2.php
            /---file3/
                /---file3.php

La convencion para nombrar los namespace sería la siguinte:


Para file1/file1.php

```php
    namespace file1;
```

Para file1/file2/file2.php

```php
    namespace file1\file2;
```

Para file1/file2/file3/file3.php

```php
    namespace file1\file2\file3;;
```

## Instaciamiento a partir de cadenas

Php es capas de instaciar objetos desde un String que contenga el **namespace**. Por ejemplo.

```php

<?php

    require('app/Class_Name.php');

    $namespace_str = 'App/Class_Name';

    $new_object = new $namespace_srt ;
?>

```

Tambien funciona si queremos ejecutar un metodo desde una cadena

```php
<?php

    require('app/Class_Name.php');

    $namespace_str = 'App/Class_Name';
    $method_str = 'method_of_class';

    $new_object = new $namespace_srt ;
    $new_object->$method_str();
    
?>
```