# To JWT or not to JWT
* **Event:** AmongUsCTF
* **Problem Type:** Web
* **Point Value / Difficulty:** Medium
* **Tools Required / Used:** Chrome or Firefox

## Solution

By looking at the source for the website and network requests made, a few API details can be worked out.

<br>

`/api/v1/` is the endpoint for the API.
<br>
The `get_flag` method returns the flag.
<br>
When signing up, the `register` method is called with a POST request containing the username and password.
<br>
When logging in, the `authenticate` method is called with a POST request containing the username and password.

<br>

Both `register` and `authenticate` set a cookie. This cookie is a JWT token.
The token can be decoded using the tool at [jwt.io](https://jwt.io).
The token consists of a header detailing the algorithm type,
a payload containing the username and if the user is an admin, 
and a signature.

There is an algorithm type in the JWT specification called "none". Tokens using this algorithm type have an empty signature.
A good JWT library will check the algorithm type and key id to make sure arbitrary tokens will not be accepted.
This library does not do that. Use an empty string for the signature, replace the algorithm type to "none" and change the admin flag to true.
This token will grant access to the flag.
