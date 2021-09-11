# Networking: Free Parking
In this challenge, a pcap file is given, which contains an HTTP access that loads 
the flag from `ctf.isss.io:4376/flag`. The flag can be found by searching through 
the file manually (e.g. `strings dump.pcapng | grep utflag`), or by opening the 
packet dump in a tool like Wireshark.

## Prompt
Whoever runs the "Free Parking" spot is hiding something, so I started sniffing 
Internet traffic. Can you check to see if anything's up?

_by mattyp_

**pcap file attached**

## Hint
You can search through the packet dump using command-line tools, or use a packet 
analysis tool, like [Wireshark](https://www.wireshark.org/).

## Flag
`utflag{parking_shark}`
