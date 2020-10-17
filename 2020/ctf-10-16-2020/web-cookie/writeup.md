# Web: Elon Musk's Fan Club
This problem serves a login page for Elon's fan club. The hint reveals 
that the website is controlling authentication via the `user` cookie. 
When logged in as `real-fan`, this cookie is set to `real-fan`, so if 
we can guess a privileged username, we can access the flag. The website 
also hints that only Elon can access the flag, so you have to set the 
`user` cookie to `elon` in order to access the flag.

## Prompt
Someone leaked the creds for an account on Elon Musk's fan club website, 
but I still can't get access to Elon's secrets. Can you help me find 
Elon's secret?

Username: `real-fan`

Password: `elon-musk-is-my-god`

`http://ctf.isss.io:4270/login`

_by mattyp_

## Hint
Inspect Element -> Storage
(only possible in Chrome/Firefox)

## Flag
`utflag{the_musk_will_inherit_the_earth}`
