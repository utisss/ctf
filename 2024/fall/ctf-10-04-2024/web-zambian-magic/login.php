<?php

    // Check if password was set
    $password = $_POST["password"];
    if (!empty($password)) {
        // Hashing the password so it's secure
        $hash = hash("sha256", $password);
        // My friend told me to put this here to fix a PHP bug
        // I didn't really understand what she was saying though
        if (!is_numeric(substr($hash, 0, 1))) {
            die("Wrong password!");
        }
        // See if the hash is the same as my password's hash
        // Real SHA256 is unbreakable so this is impossible to collide!
        if ($hash == (real)"0e758515d6332438329391314305419418756482515623712615593624630160") {
            echo "Welcome, Edward! You're looking handsome today.<br />";
            echo file_get_contents('./secrets.txt', true);
        } else {
            die("Wrong password!");
        }
    } else {
        die("Must specify password");
    }

?>