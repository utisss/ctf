```
 # Broken shell
 * **Event:** Among Us CTF
 * **Problem Type:** Reversing
 * **Point Value / Difficulty:** Med (200)
 ## Steps
 #### Step 1
You connect to the binary and notice it is some sort of custom shell that only lets you ping and has a function responsible for pinging the target you enter.
#### Step 2
When you try some special bash characters, the program quits and says don't hack me. This tells you that the program is running on linux and might be farming out requests to the 'ping' command.
#### Step 3
After trying a bunch of command injection payloads, you should come across sequential commands with semicolons.(cat test.txt;foo;bar) The binary doesn't check these, and the flag is located at flag.txt.
Since the flag is located at flag.txt, a simple payload of "ping localhost;cat flag.txt" will net you the flag.
utflag{f3016bf4966893c42ae60c379df561bc84f91e47}
```