# Web: SQLi
Difficulty: Easy

In this challenge, you're given a simple user lookup system, where you can input an email and get back a list of usernames. 
You are told that the database is using Postgres and that the user information is stored in a table called "users" with columns "username", "id", "email", and "password".

We can perform a simple SQL injection to grab the passwords of every user on the system. Note the trailing space is important. We assume there is only one column, since the website only shows one column's worth of data.
' UNION SELECT password FROM users; -- 

This gets us the flag. 

If the website showed more columns (say 3), we could not use the same query since it would be expecting three columns worth of data. We would have to pad out the result, perhaps as below:
' UNION SELECT password, password, password FROM users; -- 