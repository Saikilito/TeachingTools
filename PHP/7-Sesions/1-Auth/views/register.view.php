<?php require('views/Layout/header.php'); ?>
    <title>Register</title>
</head>
<body>
    <div class="container">
    

    <h1 class="title">Register</h1>
    <hr class="border">

    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST" class="form" name="login">
        <div class="form-group">
            <i class="icon left fa fa-user"></i><input type="text" name="user" class="user" placeholder="User">
        </div>
        <div class="form-group">
            <i class="icon left fa fa-lock"></i><input type="password" name="password" class="password" placeholder="Password">
        </div>
        <div class="form-group">
            <i class="icon left fa fa-lock"></i><input type="password" name="password2" class="password_btn" placeholder="Password Confirmation">
            <i class="submit-btn fa fa-arrow-right" onclick="login.submit()"></i>
        </div>
        
        <?php if(!empty($errors)): ?>
            <div class="error">
                <ul><?php echo $errors ?></ul>
            </div>
        <?php endif; ?>
    </form>

    <p class="text-register">
        ¿ Do you have alredy account ?
        <a href="login.php">Login</a>
    </p>

<?php require('views/Layout/footer.php'); ?>