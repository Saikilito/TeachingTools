<?php session_start();

if(isset($_SESSION['user'])){
    header('location: content.php');
}
else{
    header('location: register.php');
}

?>