# Follow the Stream
* **Event:** ThankfulCTF (11/15/2019)
* **Problem Type:** Networking
* **Point Value / Difficulty:** 100
* **Tools Used:**
    * [Wireshark](https://www.wireshark.org/)

## Overview
In this challenge, the flag is sent as ASCII-Art 1 character at a time. To reconstruct the ASCII Art, you can use Wireshark's Follow Stream option.

## Steps
### Open up the PCAP in Wireshark
Open up the Packet Capture using Wireshark, or any other PCAP viewer.

### Follow the TCP Stream
Right-click any of the TCP packets present in the PCAP, Select Follow->TCP Stream. This will present the flag as ASCII art.
