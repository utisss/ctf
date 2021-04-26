# Web: Flag Suggestions
This problem allows users to upload pictures of flags. Client-side protections 
prevent uploading anything besides images, but these can be bypassed. However, 
uploading webshells won't succeed because the server doesn't have a PHP server 
or anything similar, and doesn't allow POST requests to the `/suggestions` 
directory. The hint suggests a different direction: path traversal. While you 
can't directly do something like `/suggestions/../flag.txt` in your browser, 
you can use the developer tools or a proxy tool like Burp to browse to 
`/suggestions/../flag.txt` to steal the flag.

## Prompt
Some country is allowing people to submit flag suggestions! 
What are the odds that their government has the smartest web devs...

`http://ctf.isss.io:5381/`

_by mattyp_

## Hint
It's gonna take forever to *traverse* all these suggestions...

Flag is stored in a file named `flag.txt`.

## Flag
`utflag{this_server_needs_some_hand_sanitizer}`
