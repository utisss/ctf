# HTTP 1
* **Event:** Security Day CTF
* **Problem Type:** Networking

## Background
Wireshark is a tool that can capture and view logs of traffic going through a network. 

## Steps
Open th pcap file in Wireshark, and you can see a few TCP packets. Follow the TCP stream by right clicking on one of the packets, then follow -> TCP Stream. This shows the individual bytes which are being sent during the connection. On the bottom there are some unreadable bytes; this is because the HTTP connection is gzip-encoded. You can export the file which was transmitted through HTTP by clicking File -> Export Objects -> HTTP.