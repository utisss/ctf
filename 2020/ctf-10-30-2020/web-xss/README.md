# NGPEW Feedback Form 2
# Difficulty: Medium

This is a slightly hardened version of a challenge from 10/16. Here, the client
uses a filter so that the value sent to the server is XSS-proof. Specifically, 
all instances of < and > are removed. 

However, since this filtering is done client-side, we can bypass it. For example,
you can replace the "querydb" function in the JavaScript code with this version
that does not perform any filtering. This is done by simply defining the function
within the browser debug console.
```JavaScript
function querydb(method, path, data) {

    const feedback = data.get('feedback')//.replaceAll("<").replaceAll(">");

    const retry = (tries) => tries == 0
        ? null
        : fetch(
            path + btoa(feedback),
            {
                method,
                headers: { 'Content-Type': 'application/x-www-form-urlencoded'},
            }
          )
            .then(res => res.status == 200
                ? res.text().then(t => t)
                : "Some error occured"
            )
            .then(res => document.getElementById("databaseResult").innerHTML = res)
            .catch(e => retry(tries - 1));

    retry(1);
}
```

You can also use Burp Suite to modify the request. Open the web page in Burp Suite's 
embedded browser, then forward requests along until you hit the request that submits 
the form. Then, you can modify the HTTP request that's being sent to the server as a 
POST request, adding an XSS payload to the request as it goes out. Don't forget to 
set the "Content-Length" header of the HTTP request to match your new content. 

For information on how to craft the XSS payload, please see the "web-xss" writeup 
under the 10/16 CTF. 