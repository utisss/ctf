# Frightening Flag
* **Event:** NightmareCTF (ISSS CTF 10-18-2024)
* **Problem Type:** Reverse Engineering

## Background

[ASCII](https://www.asciitable.com/)

## Exploit

\x08 is the ASCII for backspace, and the goal here is to realize that whatever program captured this
didn't actually do the backspaces. So we go in, find all the backspaces, then remove those and
whatever was right before them, and get the flag.

A sample solution is provided in sol.py.