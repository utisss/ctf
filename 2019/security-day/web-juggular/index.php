<!DOCTYPE HTML>
<html>
<head>
<title>Juggaloo</title>
</head>
<body>
<h1>Login</h1>
<?php
include("password.php");
$password_hash = "0e574837584728375847385748394857";
$guess = $_POST["pass"];

if(is_numeric($guess) && md5($guess) == $password_hash) {
	echo "<div>utflag{" . $password ."}</div>";
}else{
	echo "<div>Failed authentication</div>";
}
?>
<form method="post" path="/">
	<input type="text" name="pass" placeholder="password" />
	<input type="submit" />
</form>
</body>
</html>