# Mappy
* **Event:** Galactic Battle CTF
* **Problem Type:** Networking
* **Difficulty:** Easy
* **Tools Used:** nmap, curl

## Solution

Nmap can be used for this problem.
<br><br>
`nmap mappy.ctf.isss.io`
<br><br>
There is one TCP port open.
Connecting to it via telnet or netcat and sending data causes the host to return a response.
The response makes it clear that it's an HTTP server.
<br><br>
`curl http://mappy.ctf.isss.io`
