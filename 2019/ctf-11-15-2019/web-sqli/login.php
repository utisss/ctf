<?php
if(isset($_POST["username"]) && isset($_POST["password"])) {
	$conn = new mysqli("localhost", "USER", "PASSWORD", "users");
	if($conn->connect_error) {
		die("connection failed: " . $conn->connect_error);
	}

	$query = "SELECT name FROM user WHERE name='".$_POST["username"]."' and password='".$_POST["password"]."'";
	$result = $conn->query($query);

	if($result && $result->num_rows > 0) {
		echo "Login successful!";
	}else{
		echo "Login failed";
	}
}else{
	echo "invalid request";
}
?>