# Baldi's Basics
This problem directs you to a website that asks you to solve math problems. If
you can solve 500 problems correctly in a row, the site gives you the flag.

The website uses secure flask session cookies, so even though you have access 
to the cookie (which contains the current challenge as well as the answer
streak), the user is unable to forge a new cookie.

So the next best thing we can do is automate the requests. We can use puppeteer
as a general-purpose tool for pretending to be a user, and its usage is quite 
simple. The full solution script is available in solution.js.