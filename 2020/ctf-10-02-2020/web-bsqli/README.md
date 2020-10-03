# Navigation Log In
# Difficulty: Medium

This challenge is a blind SQL injection. We can first check for SQL injection using the username
`' OR 1=1; -- `. (Note the space at the end). 

This changes the query to `SELECT * FROM Users WHERE username = '' OR 1=1; -- ' AND password = ''`. 
Since the ` -- ` comments out the rest of the line, this returns every user in the database, 
allowing us to log in.

However, we are interested in the password. Since we are not given any information other than a 
vague "success" or "failure", this is a blind SQL injection. The process is fairly long, but this 
guide is very useful: https://portswigger.net/web-security/sql-injection/blind

SQLMap also has a blind sql feature. 