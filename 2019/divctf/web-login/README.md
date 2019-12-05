# Login
* **Event:** DivCTF
* **Problem Type:** Web
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:** Chrome debugger

## Steps​
We can try registering a new account, but since the new account's username is not "admin", we don't get access to the flag. We can also try registering the username "admin", but the login process doesn't allow that. Once we get to members.php, however, we can check the cookies in the Chrome web inspector tools, then we find a cookie called "logged_in_user", containing the username of the currently logged in user. Changing that to "admin" and refreshing the page gets us the flag. 