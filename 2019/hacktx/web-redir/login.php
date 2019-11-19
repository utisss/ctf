<!DOCTYPE HTML>
<html>
<head>
<title>Log in!</title>
</head>
<body>
<h1>Super secure login form</h1>
<form action="enter.php" method="post">
<input type="hidden" name="authenticated" value="false" />
<input type="submit" value="Continue" />
</form>
<script>
var form = document.querySelector("form");
form.submit();
</script>
</body>
</html>