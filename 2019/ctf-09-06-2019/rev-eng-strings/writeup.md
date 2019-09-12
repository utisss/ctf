# Strings
* **Event:** BepisCTF (ISSS CTF 09-06-2016)
* **Problem Type:** Reverse Engineering

## Background
[Strings](https://linux.die.net/man/1/strings) linux tool that looks for strings inside files.

## Steps
### Run strings
```
$ strings password | grep "flag"
utflag{h4rdc0d3d_str1ngs}
```
