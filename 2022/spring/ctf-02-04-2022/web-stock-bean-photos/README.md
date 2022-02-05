# Web: Stock Bean Photos
In this challenge, you're pointed at a website that simply serves you image files. 
If you inspect the site's source, you can see that the dropdown includes filenames, 
which are submitted to the server. The server then responds with the file, if it 
exists in some directory. 

The first step to this problem is requesting a file that isn't listed in the dropdown. 
You can do this by modifying the HTML code for the dropdown, creating your own request using the
"Network" tab in your browser's developer tools, or by intercepting and modifying a request using 
a proxy tool like Burp. If you request a random filename, you'll notice the server returns an error.
You'll notice that the server does the same thing if you include ".." in the filename, suggesting
you might be able to try a path traversal attack.

The next step is getting to the flag (which a hint says is at "flag.txt"). If you just try a
filename like `/flag.txt`, it won't work, suggesting that you need to use a relative path. To do
this, you need to figure out how many `../` you need to do request something like
`../../../flag.txt`. A standard way to do this is to look a special file which is always at the same 
location, like `/etc/passwd`. Then, you can successively try filenames like `../etc/passwd`,
`../../etc/passwd`, `../../../etc/passwd` until you find the root directory. Once you know this, you
can request `../../../../flag.txt`, and you're done.

