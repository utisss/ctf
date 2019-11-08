# In The Clear
* **Event:** Security Day CTF (10/09/2019)
* **Problem Type:** Networking
* **Point Value / Difficulty:** TBD
* **Tools Used:**
    * [Wireshark](https://www.wireshark.org/)

## Background
Oftentimes, web developers utilize cookies for authentication and sessions. When sending cookies, HTTP includes them as a HTTP Header. If we aren't using HTTPS, this information is available as plaintext to any eavesdropper. 

## Steps
### Open up the PCAP in Wireshark
Open up the Packet Capture using Wireshark, or any other PCAP viewer.

### Filter out the noise
A lot of noise was included in the PCAP to make things more interesting. You can easily do this in Wireshark with *not tcp.port eq 443*. This removes all of the additional encrypted traffic and leaves us with some HTTP traffic.

### Analyze the traffic
We can see, by following the TCP stream of the HTTP traffic, that the flag isn't here, but it will be added at a later date. This time, we get the URL, but navigating there yields no results. Luckily, though, a authentication cookie is included within the request.

### Extract and utilize the cookie from the HTTP traffic
Look at the HTTP request to see the cookie in plaintext as an HTTP header. Using any method, set this cookie in your browser. Navigate to the website to reveal the flag.
