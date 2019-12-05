<!DOCTYPE HTML>
<html>
<head>
<title>Very Secure User Information System</title>
</head>
<body>
<h1>Very Secure User Information System</h1>
<form method="GET">
<label for="username">Query by name: </label><br>
<input name="username"></input><br>
<input type="submit">
</form>
<?php
ini_set('display_errors', 1); ini_set('display_startup_errors', 1); error_reporting(E_ALL);
if(isset($_GET["username"])) {
	$conn = new mysqli("HOST", "USER", "PASS", "users");
	if($conn->connect_error) {
		die("connection failed: " . $conn->connect_error);
	}

	$query = "SELECT name, email FROM user WHERE name='".$_GET["username"]."'";
	echo "<div>SQL query: <i>$query</i></div>";
	$result = $conn->query($query);

	if($result && $result->num_rows > 0) {
		echo "<table><tr><th>Name</th><th>Email</th></tr>";
		while($row = $result->fetch_assoc()) {
			echo "<tr>";

			echo "<th>".$row["name"]."</th>";
			echo "<th>".$row["email"]."</th>";
			echo "</tr>";
		}
		echo "</table>";
	}else{
		echo "No users found";
	}
}
?>

</body>
</html>