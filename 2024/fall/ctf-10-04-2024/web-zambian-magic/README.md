# Zambian Magic
* **Event:** SpaceCTF (ISSS CTF 10-04-2024)
* **Problem Type:** Web

## Background

[PHP Type Juggling](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md)

[Magic Hashes](https://github.com/spaze/hashes)

## Exploit

After inspect element and finding the source code for the login page, we can observe a particularly
odd line: the comparison of the password hash to a hardcoded hash. The hash is (mistakenly) cast to
a real number, and appears as 0e(numbers). In scientific notation, this comes out to 0 x 10^(x) = 0.
This is a hint that we need to find something else that hashes under sha256 to something that PHP
would interpret as 0. Luckily for us PHP 7 is a very loose language when it comes to type inference,
and so with a bit of googling we can find a list of "magic hashes" which accomplish this.