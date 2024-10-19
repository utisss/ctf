# Environmentally Friendly File Server
* **Event:** NightmareCTF (ISSS CTF 10-18-2024)
* **Problem Type:** Web

## Background

(Path Traversal)[https://owasp.org/www-community/attacks/Path_Traversal]

(/proc)[https://www.linux.com/news/discover-possibilities-proc-directory/]

## Exploit

There are a few parts to this challenge.

1) Path traversal attack. The fileserver will open any filepath it's given, unfortunately it does
add a relative path to the start so you can't do absolute paths. ../. seem to get removed by
browsers, but you can use `curl` or %2e or a combination of both to get around it.

2) The problem hints towards finding the shell in an environment variable, so read the
/proc/self/environ file.