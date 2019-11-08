# Phonebooks for Computers
* **Event:** Security Day CTF (10/09/2019)
* **Problem Type:** Networking
* **Point Value / Difficulty:** TBD
* **Tools Used:**
    * [Wireshark](https://www.wireshark.org/)

## Background
[DNS](https://en.wikipedia.org/wiki/Domain_Name_System) is the primary protocol for mapping IP Addresses to host names. For example, when you visit *supersecret.tk* in your browser, you computer actually sends a DNS Query for *supersecret.tk*, to which it receives an IP as a response.

## Steps
### Open up the PCAP in Wireshark
Open up the Packet Capture using Wireshark, or any other PCAP viewer.

### Filter out the noise
A lot of noise was included in the PCAP to make things more interesting. You can easily do this in Wireshark with *not tcp.port eq 443*. This removes all of the additional encrypted traffic and leaves us with some DNS and HTTP traffic.

### Analyze the traffic
We can see, by following the TCP stream of the HTTP traffic, that the flag isn't here, but it will be added at a later date. Sadly, the IP has changed, but fortunately for us, we have the DNS Request. Since DNS is in plaintext, we can see what URL was requested: *supersecret.tk*.

### Navigate to the hidden site
Using cURL or your favorite browser, navigate to the website and receive the flag.
