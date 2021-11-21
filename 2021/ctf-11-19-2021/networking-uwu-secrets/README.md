# Networking: Uwu Secrets
This problem starts you off with a command to lookup a very particular 
domain using a specific DNS server. There are two main things that you 
need to figure out to solve this problem. First, the 0 in 
`0.flag.uwu.com` can be replaced with other numbers, e.g. 1 and 
2 to get more information. Second, you need to realize that the IPs 
returned by the DNS server correspond to ASCII character values. For 
instance, each number in the reuslt for `0.flag.uwu.com` 
corresponds to the first four characters of "utflag".

If you work through all the available domain names, you can uncover the 
whole flag.

