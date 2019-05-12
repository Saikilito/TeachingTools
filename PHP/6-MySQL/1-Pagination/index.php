<?php

error_reporting(E_ALL);
ini_set('display_errors', '1');

try{
    $db_data = 'mysql:host=localhost;dbname=pagination';
    $connection = new PDO($db_data , 'root' , 'root' );    
}
catch(PDOException $e){
    echo 'Error: ' . $e->getMessage();
    die('BD not connection');
}

//We ask if the page variable exists
$page = isset($_GET['page']) ? (int)$_GET['page'] : 1 ;
$limit_post = 5 ;

//To know from which article to bring by from the page
$init = ( $page > 1 ) ? ($page * $limit_post - $limit_post) : 0 ;

//SQL_CALC_FOUND_ROWS : count how many articles there are in my database
$articles = $connection->prepare("
    SELECT SQL_CALC_FOUND_ROWS * FROM articles 
    LIMIT $init , $limit_post
");
$articles->execute();
$articles = $articles->fetchAll();

if(!$articles){
    header('location: index.php');
}

//What pages we need ?
//FOUND_ROWS Exist thanks a the query SQL_CALC_FOUND_ROWS
$total_articles = $connection->query('SELECT FOUND_ROWS() as total');
$total_articles = $total_articles->fetch()['total'];

$num_page =  $total_articles / $limit_post ; 
$num_page = ceil($num_page);

?>

<?php require('index.view.php'); ?>