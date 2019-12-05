<!DOCTYPE HTML>
<html>
<head>
	<title>Members Area</title>
</head>
<body>
	<h1>Members-Only Area</h1>
<?php
	if(!isset($_COOKIE["logged_in_user"])) {
		echo "<div>You are not logged in!</div>";
	}else if($_COOKIE["logged_in_user"] != "admin") {
		echo "<div>You are logged in, but your username is not 'admin', so you cannot access the admins-only flag.</div>";
	}else{
		echo "utflag{cookies_are_weird_au3875}";
	}
?>
</body>
</html>