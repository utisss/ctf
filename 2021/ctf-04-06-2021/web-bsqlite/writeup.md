# BSqlite
# Difficulty: Hard

This challenge is a blind SQL injection. Take a look at 
2020/fall/ctf-10-02-2020/web-bsqli to get an idea of how bsqli works.

The twist is that you don't know the table names or the column names this time.

However, since we are given that the database is a Sqlite database, we know
that the sqlite_master table contains information on the table and column
names, so we can perform a blind SQL injection on that table.

For example, to exfiltrate the table name, we can use the following injection:
```
' UNION SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name LIKE 'a%'; -- 
```

We eventually find that the table name is 'secret_tbl'.

Then we can exfiltrate the column name using the following injection:
```
' UNION SELECT name FROM sqlite_master WHERE type='table AND name = 'secret_tbl' AND sql LIKE 'a%'; -- 
```

The sql column gets really long so you should definitely write a script to do this for you.

Finally, once we get the column name, we do a regular blind sql injection and we're done!
