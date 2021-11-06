# Plaintextifier

This is a SSRF challenge.

If you navigate to the admin page, you get a 403 message indicating that you should be connected to the "VPN". This is really just a hint that the access to the admin page needs to come from the internal network.

So, you can tell the website to convert the admin page to plain text.

There's one other trick - you can't just give it the _public_ address of the admin page because that won't go through the internal network. Instead, you have to connect to localhost: `http://localhost:6418/admin`.
