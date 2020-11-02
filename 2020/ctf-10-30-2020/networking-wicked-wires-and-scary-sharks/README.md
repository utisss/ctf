# Wicked Wires and Scary Sharks
* **Event:** Spooky CTF
* **Problem Type:** Networking
* **Difficulty:** Medium
* **Tools Used:** Wireshark

## Solution
There's a capture file and a log of TLS session keys. Set Wireshark to use those session keys to decrypt the TLS traffic. There will be a HTTP2 request going to a website requesting a file named `flag.webp`. There are several data streams responding to this request. Copy those bytes into a file (if copying hex, make sure to convert hex to bytes), and open up the image in a browser to see the flag.
