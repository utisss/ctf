# Eval
# Difficulty: Easy

We first open the browser developer tools to take a look at the source code.
By clicking the "Source" tab, we are able to see the JavaScript code on the 
page, in a file called flagCheck.js.

```javascript
function checkFlag(flag) {
    return eval(atob("ZmxhZyA9PSAndXRmbGFne2NhbnRfc3RvcF93b250X3N0b3BfZ2FtZXN0b3B9Jw=="));
}
```

We see the code use two built-in functions, eval() and atob(). 

https://www.w3schools.com/jsref/met_win_atob.asp
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval

From the documentation, atob deserializes a base64 string, and eval accepts a
string of JavaScript code and executes it in the current context. 

Converting the base64 string back to an ascii string gets us the flag in plain text.
We can run the following code in the browser console.

```
atob("ZmxhZyA9PSAndXRmbGFne2NhbnRfc3RvcF93b250X3N0b3BfZ2FtZXN0b3B9Jw==")
```