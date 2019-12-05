<?php
if($_POST["username"] == "admin") {
	die("The user already exists!");
}
setcookie("logged_in_user", $_POST["username"], time() + (86400 * 30), "/login");
header("Location: /login/members.php");
?>