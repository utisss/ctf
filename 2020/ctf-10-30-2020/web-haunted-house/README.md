# Web: Haunted House
This problem displays a login page with just a username. 
If you try to login, it tells you that you are not spooky enough 
to enter. The hint suggests inspecting the page to see how this 
is determined. If you use your browser's "Inspect Element" function, 
you can find that there is a hidden field in the login form, `spooky`, 
which is set to `false`. Since the actual request is sent from your 
browser and not controlled by the server, you can simply change the 
field to `true` and login, or intercept the request and change the 
field to `true` that way.

## Prompt
All my friends got into this cool haunted house, 
but they won't let me in the door! Can you help me 
get into the haunted house?

`http://ctf.isss.io:4280/login`

_by mattyp_

## Hint
Try _inspecting_ to see how they know you're not spooky enough.

## Flag
`utflag{jeff_is_the_spookiest_of_them_all}`
