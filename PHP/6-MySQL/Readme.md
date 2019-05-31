<h1 align="center">Php con MySQL</h1>

PHP se integra de una manera muy óptima con MySQL, cuando descargas un servidor local, como por ejemplo MAMP, ya trae integrado MySQL listo para usar y además tiene un administrador para la base de datos llamado PhpMyAdmin con el que se puede manejar la base de datos de manera visual, sencilla y con todas las opciones que puedas necesitar

## ÍNDICE 

1. [Formato Actual ( Recomendado) ](#formato-actual-pdo)
2. [Formato Antiguo ( No Recomendado )](#formato-antiguo)
3. [Algunos Querys SQL a tener en cuenta
](#algunos-querys-sql-a-tener-en-cuenta)

**Conectar PHP con MySQL**

Conectar MySQL a PHP es muy sencillo, para esta tarea veremos tres maneras de hacerlo

### Formato actual PDO
**_( recomendado )_** <br/><br/>
&nbsp;**PDO significa Objetos de Datos de PHP por sus siglas en ingles**

1. **Para crear una conexión a MySQL utilizando PDO solo debemos usar el siguiente código :**

```php
    try{

       $db_data = 'mysql:host=localhost;dbname=db_name';
        $connection = new PDO($db_data , 'user_db' , 'password_db' );

        //code...
    }
    catch(PDOException $e){
        echo "Error: " . $e->getMessage();
    };
```

**La variable '$db_data' contiene la siguiente información:**

>_host_ : Aquí debemos asignar el puerto al que está conectado nuestra BD

>_dbname_: Aquí debemos asignar el nombre de la base de datos que queremos usar

**Luego en los datos que recibe PDO**

>_user_db_ : Aquí debemos asignar el nombre de usuario para la base de datos

>_password_db_ : Aquí debemos asignar la contraseña de la base de datos

2. **Para hacer consultas debemos :**

>El siguiente código debe ir dentro de la función try/catch sustituyendo el comentario por el mismo

**Si deseamos hacer consultas sin usar variables**
```php
    $res = $connection->query('QUERY MYSQL');
```
Esta función devuelve un arreglo por lo que si queremos ver en pantalla la información capturada podemos usar el siguiente código, por ejemplo:

```php
    foreach ($res as $fill){
        echo $fill['associative_name'];
    };
```

>Pero este método es recomendable solo para Querys que no se mezclan con variables, debido a que presenta inseguridades, por ejemplo si capturamos información mediante la URL se podrá inyectar código

**Si desemos hacer consultas utilizando variables**

```php
    $var_val = 'random_val';
    $query_var = 'MYSQL_QUERY WHERE field = :var_val';

    $statement = $connection->prepare($query_var);

    $statement->execute(
        array(
            ':var_val' => $var_val
        );
    );

    $res_statement = statement->fetchALl();

    print_r($res_statement);
```
>Cambia MYSQL_QUERY por la consulta real

Lo que acabamos de ver es una consulta con una query que requiere del uso de variables

>' :var_val ' será reconocido como una variable dentro de la query

Se usa el método 'prepare' y se le pasa la query que deseamos enviar, luego el método 'execute' recibirá un array como argumento y dentro de este array debemos definir todas las variables que deseamos usar dentro de la query.

Por ultimo usaremos el método 'fetchAll' para obtener los valores de la tabla y guardarlos en una variable que finalmente podremos usar.

<br/><br/>

### **_Formato antiguo_**
**_( no recomendado )_**<br/><br/>

> Esta forma no es recomendada de usar actualmente ya que tiene algunos problemas de seguridad, pero es necesario tenerla en cuenta ya que en la web existen muchos proyectos que están escritos usando esta forma debido a que era la manera en que se hacía en el pasado

1. **Debemos crear la configuración de conexión para MySQL**

&nbsp;Esto podemos lograrlo llamando la siguiente función y guardando su resultado en una variable

```php

$connection = mysql_connect('localhost' , 'user_db' , 'password_db') or die('message about file connection');

```

&nbsp; El primer parámetro hace referencia al puerto donde nos vamos a conectar

&nbsp; El segundo nos solicita el nombre de usuario para MySQL

&nbsp; El tercero nos solicita la contraseña del usuario

&nbsp; Por último si existe algún error al conectarnos corremos la función 'die' y dentro enviamos un mensaje indicando el error en la conexión

2. **Debemos enviar la configuración de MySQL y seleccionar una base de datos**

&nbsp;Esto podemos lograrlo llamando la siguiente función

```php

mysql_select_db( ' db_name ' , $connection );

```

&nbsp;En este caso no es necesario guardarlo en una variable, con solo ejecutar la función estaremos conectados a la BD

3. **Ahora podemos ejecutar una query para hacer consultas a la BD**

&nbsp;Para ejecutar Querys tenemos la siguiente función :

```php
    $query_res = mysql_query('MYSQL_QUERY');
```
&nbsp;Luego para poder usar esta información debemos guardarla en una variable y para esto tenemos las siguientes funciones las cuales retornan la información en diferentes formatos: 

```php
    $fill_res = mysql_fetch_object($query_res);
```
&nbsp;O la siguiente función :
```php
    $fill_res = mysql_fetch_array($query_res);
```

&nbsp;Estas funciones retornan un Objeto Php y un Array Asociativo respectivamente.

&nbsp;Cada vez que alguna de estas funciones es llamada retorna una fila de la tabla que se guarda en la variable correspondiente, luego esta función se posicionara en la siguiente fila, colocándose así en una fila diferente cada vez que es llamada.

&nbsp;Por lo tanto, si queremos mostrar información recorriendo una tabla podemos usar un ciclo como por ejemplo:

```php
   while($fill_res = mysql_fetch_object(query))
   {
       echo $fill_res->attribute_object;
   }
```

O si queremos usar la otra función

```php
   while($fill_res = mysql_fetch_object(query))
   {
       echo $fill_res['associative_name'];
   }
```

## ORM (Object Relational Maping)

Existen varias librerías que funcionan como ORM, una de las más conocidas es Laravel Eloquent, hacemos referencia a ella en la sección de “composer” ya que estas no son nativas de PHP.

Adicionalmente en esta sección dejaremos un archivo que hace referencia a una práctica con el ORM de Eloquent.

## Algunos Querys SQL a tener en cuenta

Para poder hacer consultas a la base de datos es importante tener en cuenta algunas Querys básicas que podrían ser de ayuda

### Insertar valores en una tabla
```php
    'INSERT INTO <name_table> (field1,field2,...,fieldN) VALUES (val1, val2, ... ,valN)';
```

### Actualizar un valor 
```php
    'UPDATE <name_table> SET <update_field> = <val> WHERE <field> = <val>';
```

### Ver algunos valores de una tabla
```php
    'SELECT field1,field2,...,fieldN FROM <name_table>';
```

### Ver algunas filas de una tabla
```php
    'SELECT * FROM <name_table> WHERE <field> = <val>';
```

### Ver filas por coincidencia
```php
    'SELECT * FROM <name_table> WHERE <field> LIKE <'val'%> ';
```

El símbolo '%' en SQL significa donde se coloca que puede ir cualquier cosa, en este caso traerá todas las coincidencias que encuentre con 'val' sin importar las 'cosas' que consiga luego de él, este se puede colocar en cualquier parte del valor.

### Ver algunos valores ordenardamente
De forma ascendente:
```php
    'SELECT * FROM <name_table> ORDER BY <field> ASC';
```
De forma descendente:
```php
    'SELECT * FROM <name_table> ORDER BY <field> DESC';
```

### Ver algunos valores limitando la cantidad de filas
```php
    'SELECT * FROM <name_table> LIMIT <val_num>';
```
Si deseamos traer filas desde un número especifico hasta otro:
```php
    'SELECT * FROM <name_table> LIMIT <since_val_num>,<more_val_num>';
```

### Borrar algunas filas
```php
    'DELETE FROM <name_table> WHERE <field> = <val>';
```
