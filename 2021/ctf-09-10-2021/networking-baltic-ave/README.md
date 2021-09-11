# Networking: Baltic Ave
In this challenge, a pcap file is given, which contains a login over HTTP 
to the site `ctf.isss.io:4376/login`. However, the credentials can only be used 
from the internal network, so you need to find a different way in. In the pcap 
file, the server's responds to the login by setting an `Authorization` cookie, 
which can be reused to access the `/flag` page.

## Prompt
Looks like my friend upgraded his security after I broke in last time. 
Can you bust through his defenses?

_by mattyp_

**pcap file attached**

## Hint
I wonder how the server remembers you once you login?

## Flag
`utflag{w3lc0m3_th1mbl3}`
