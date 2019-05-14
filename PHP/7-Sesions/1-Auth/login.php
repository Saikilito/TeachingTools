<?php 
require('displayErrors.php');
session_start();


if(isset($_SESSION['user'])){
    header('location: index.php');
}

if($_SERVER['REQUEST_METHOD'] == 'POST') {
    $user = filter_var(strtolower($_POST['user']), FILTER_SANITIZE_STRING);
    $password = hash('sha512',$_POST['password']);

    try{
        $db_data = 'mysql:host=localhost;dbname=auth_practice';
        $connection = new PDO($db_data , 'root' , 'root' );

        $my_query_sql = 'SELECT * FROM user WHERE user = :user AND password = :password';

        $statement = $connection->prepare($my_query_sql);
        $statement->execute([
            ":user" => $user,
            ":password"=>$password
        ]);

        $result = $statement->fetch();
        
        $errors = '' ; 

        if($result == false){
            $errors .= '<li>User or password is wrong</li>';
        }
        else{
            $_SESSION['user'] = $user ;
            header('location: index.php');
        }
    }
    catch (PDOException $e){
        echo "Error: " . $e->gerMessage();
    }
}


?>
<?php require('views/login.view.php'); ?>