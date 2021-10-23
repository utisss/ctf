# JWT 1

This challenge involves hacking JWT tokens with an algorithm of "none".

Essentially, in this mode a JWT token is simply a fancy unauthenticated wrapper
for a base64-encoded payload that looks like `eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpc19hZG1pbiI6ZmFsc2V9.`, 
which we can input into jwt.io to find that the
contents are simply `{"is_admin":false}`. We can modify the contents to instead
read `{"is_admin":true}`. For example, we can use the following python script
to generate a new JWT token:

```
import jwt
print(jwt.encode({ "is_admin": True }, None, algorithm="none"))
```

Now, we can simply change our cookie to be this value, refresh the page, and 
we're done!