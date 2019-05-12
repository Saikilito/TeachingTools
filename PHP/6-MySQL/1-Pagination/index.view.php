<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://fonts.googleapis.com/css?family=Oswald:300,400,700" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <title>Paginator</title>
</head>
<body>
    <div class="container">
        <h1>Articles</h1>
        <section class="articles">
            <ul>

                <?php foreach ($articles as $article): ?>
                    <li> 
                        <?php echo $article['ID'] . ' - ' . $article['article'] ;?>
                    </li>
                <?php endforeach ?>

            </ul>
        </section>
        <section class="paginator">
            <ul>
                <?php if($page == 1): ?>
                    <li class="disabled">&laquo;</li>
                <?php else: ?>
                    <li class="""><a href="?page=<?php echo $page - 1 ?>">&laquo;</a></li>
                <?php endif ?>

                <?php 
                    for ($i=1; $i <= $num_page ; $i++) { 
                        if ($page == $i)
                            echo "<li class='active'><a href='?page=$i'>$i</a></li>";
                        else
                            echo "<li><a href='?page=$i'> $i </a></li>";
                    }      
                ?>

                <?php if($page == $num_page): ?>
                    <li class="disabled">&raquo;</li>
                <?php else: ?>
                    <li class="""><a href="?page=<?php echo $page + 1 ?>">&raquo;</a></li>
                <?php endif ?>
              
            </ul>
        </section>
    </div>
</body>
</html>