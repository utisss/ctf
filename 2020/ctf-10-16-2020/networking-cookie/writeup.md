# Networking: Cool Kids Club
In this challenge, a pcap file is given, which contains a login over HTTP 
to the site `ctf.isss.io:4271/login`. However, the credentials can only be used 
from the internal network, so you need to find a different way in. In the pcap 
file, the server's responds to the login by setting an `Authorization` cookie, 
which can be reused to access the `/flag` page.

## Prompt
I was sniffing my friend's internet traffic to try to get in on his secret club, 
but I can't break in. Can you break into his secret club?

_by mattyp_

**pcap file attached**

## Hint
I wonder how the server remembers you once you login?

## Flag
`utflag{wow_you_must_be_really_cool}`
