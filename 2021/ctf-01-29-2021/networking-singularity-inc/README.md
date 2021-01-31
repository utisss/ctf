# Web: Singularity Inc.
This problem gives you a packet dump and points you to a webpage 
which requires HTTP Basic Auth credentials. However, since HTTP 
Basic Auth is not performed over encrypted channels, credentials 
and authorization cookies can be stolen and used by network attackers. 
For instance, in this problem, you can access the page by setting the 
`Authorization` header in your browser or a command-line tool. 
Alternatively (and more simply), you can load the packet dump in 
a packet analysis tool like Wireshark, which will decode the username 
and password used in the login.

## Prompt
I was spying on the Singularity company and I managed to capture 
traffic on their internal login page. Can you use the traffic to 
break the login and figure out what today's flag is?

**put packet dump here**

`http://ctf.isss.io:4332/flag`

_by mattyp_

## Hint
Try opening the file in a packet analyzer like Wireshark!

## Flag
`utflag{http-basic-auth-equals-doodoo}`
