# Is It Up?
This problem points you to a webapp that lets you enter a hostname, and will tell you if it's up.
For hosts that are up (e.g. google.com), the webapp will say it's up, and for hosts that are down
(e.g. random IP addresses), the webapp will say it's down. The first hint suggests trying to cause
an error, which you can do by using invalid hostnames, like `google$com`. If the hostname you enter
causes an error, the error will be reflected on the webpage. The error reveals that the `ping`
command-line utility is being used internally. As a result, you can try injecting commands using
shell metacharacters like `\`` or `$()`. If you try using spaces, you should notice that they're
stripped from the hostname, meaning you can't do something simple like `google.com\`cat
/flag.txt\``. There might be other ways to do this, but a standard way to bypass the spacing
constraint is to use the special shell value `${IFS}, which contains spaces. So, a hostname like
`google.com`cat${IFS}/flag.txt` will cause an error and also reveal the flag.

