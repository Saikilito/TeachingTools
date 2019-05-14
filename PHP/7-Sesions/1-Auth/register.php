<?php

ini_set('display_errors', '1');
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

?>

<?php session_start();

if(isset($_SESSION['user'])){
    header('location: index.php');
}
 
if($_SERVER['REQUEST_METHOD'] == 'POST') {
    $user = filter_var(strtolower($_POST['user']), FILTER_SANITIZE_STRING);
    $password = $_POST['password'];
    $password2 = $_POST['password2'];

    echo "$user . $password . $password2";

    $errors = '';

    if(empty($user) or empty($password) or empty($password2)){
        $errors .= '<li> Exist a field VACIO  </li>'; 
    }
    else{
        try{
            $db_data = 'mysql:host=localhost;dbname=auth_practice';
            $connection = new PDO($db_data , 'root' , 'root' );

            $my_query_sql = 'SELECT * FROM user WHERE user = :user LIMIT 1';

            $statement = $connection->prepare($my_query_sql);
            $statement->execute([
                ":user" => $user
            ]);

            $result = $statement->fetch();
                      
            if($result !== false){
                $errors .= '<li>El nombre de usuario ya existe</li>';
            }
          
            if($password != $password2){
                $errors .= '<li>Las contraseñas no son iguales</li>';
            }
            else{
                $password = hash('sha512', $password);
            }
            
        }
        catch (PDOException $e){
            echo "Error: " . $e->gerMessage();
        }
    }

    if (empty($errors)){
        $my_query_sql = 'INSERT INTO user (ID,user,password) VALUES (null,:user,:password)';
        
        $statement = $connection->prepare($my_query_sql);
        $statement->execute([
            ':user'=>$user,
            ':password'=>$password
        ]);

        header('location: login.php');

    }
}
 
?>

<?php require('views/register.view.php'); ?>