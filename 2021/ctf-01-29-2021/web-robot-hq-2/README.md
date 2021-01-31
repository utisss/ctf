# Web: Robot HQ 2
This problem is meant to be a successor to "Robot HQ 1". The websocket 
messages from the original problem now send a password to the server, 
which you have to guess. The correct password is just the inverse of the 
placeholder password ("beep-boop"). The more tricky part of the problem 
is figuring out how to send websocket messages. The simplest way is to 
run a modified version of the page's JavaScript source in your browser's 
JavaScript console. You could also intercept websocket messages using a 
proxy like Burp, and modify the payload before they're sent to the server.

## Prompt
Looks like the robots updated their HQ with a password, and they 
left a placeholder password in the source. Can you guess the correct 
password and break in?

`http://ctf.isss.io:4331/`

_by mattyp_

## Hint
Try to guess a password using the JavaScript console or a proxy like Burp!

The password is _very_ similar to the one in the page's source ...

## Flag
`utflag{l33t_w3b50ck3t5_hack}`
