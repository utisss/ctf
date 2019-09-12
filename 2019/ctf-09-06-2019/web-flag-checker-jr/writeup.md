# Flag Checker Jr
* **Event:** BepisCTF (ISSS CTF 09-06-2016)
* **Problem Type:** Web
* **Point Value / Difficulty:** Easy
* **Tools Used:**
    * Chrome Inspect Element

## Background
[JavaScript](https://en.wikipedia.org/wiki/JavaScript) is a language used to run code on the client, which in this case is the browser. Since the code is being run on the client, the client has full control over the execution of local JavaScript code. For this reason, security-sensitive validation and input checking should always be performed on the server. 

## Steps
### View Source
Right click on the website and select "View Source".
Notice the following code:
```
if(btoa(flag) === "dXRmbGFne2dvX2hvbWVfanNfdXJfZHJ1bmt9") {
    alert("You got the flag!");
}else{
    alert("Try again!");
}
```
It seems to be processing the user's flag guess and comparing it to some processed flag. Searching for btoa online tells us that btoa is used to encode a string in base64. 

We can decide the base64-encoded string "dXRmbGFne2dvX2hvbWVfanNfdXJfZHJ1bmt9" to obtain the flag. This can be done using JavaScript's atob function or an online tool. 