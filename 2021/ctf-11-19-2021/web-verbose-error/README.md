# Web: Senpai's Favorite Vegetable
This challenge points you to a webapp that allows you to select Senpai's favorite vegetable. The
drop-down option has a suspicious option called `__utflag__`, which when submitted, will display an
error about an `isAdmin` field. The error is supposed to point you to try adding a field `isAdmin`
to the POST request that submits the form. You can do this by using a tool like BurpSuite to
intercept and modify browser requests, or with a command-line tool like `curl`. One easy way to do
this is to open the "Network" tab in your browser's developer tools, find the request you're
interested in, right-click it, and select "Copy-\>Copy as cURL". This option will copy the request
as a command-line `curl` command that you can modify.

