# Thanks TLS
* **Event:** ThankfulCTF (11/15/2019)
* **Problem Type:** Networking
* **Point Value / Difficulty:** 300
* **Tools Used:**
    * [Wireshark](https://www.wireshark.org/)

## Overview
TLS/SSL allows for secure web traffic. It provides both authenticity and confidentiality. Unfortunately, not everything can be encrypted. As part of the handshake, the domain-name of the server is sent in the clear. This is called the SNI.

## Steps
### Open up the PCAP in Wireshark
Open up the Packet Capture using Wireshark, or any other PCAP viewer.

### Find the SNI in the Client Hello
Locate the SNI within the Client Hello packet. You should find utflag.tk

### Navigate to the server
Navigate to https://utflag.tk to get the flag.
