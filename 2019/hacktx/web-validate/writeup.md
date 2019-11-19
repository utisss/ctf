# Client-Side Validation
* **Event:** HackTX CTF (11-02-2019)
* **Problem Type:** Web
* **Point Value / Difficulty:** Easy
* **Tools Used:**
    * Browser developer tools + JavaScript

## Background
[Client-side Validation](https://cwe.mitre.org/data/definitions/602.html) is a common mistake made by both young and seasoned developers. Essentially, the idea is that the server trusts that the user won't manipulate the client and remove any checks or validations. For example, tricking a registration web page into allowing you to register for something past the registration end-date. Since the server trusts whatever the client sends it, this can be manipulated to cause a number of issues.


## Steps
### Open up the Browser Tools
Open up the Browser Tools. There are numerous ways to do this, depending on your preferences and browser. In Chrome, Ctrl+Shift+I accomplishes this task.

### Look for code that checks current date and rejects late registrations
Using Browser Tools in Chrome, open the 'Elements' tab and look for a 'form' element. Within the 'form' element look for a 'button' element and observe the method that is called when you click the button - validateTime. The code for validateTime is in the header of the HTML page. What validateTime does is check if the current date for your machine is before or after October 15th, 1968. If your machine is past the date, registration is rejected (the form is not posted to the server), otherwise registration is accepted.

### Change registration date checking
In order to register, the code that checks the date in validateTime will need to be changed. This may be accomplished using the 'Console' tab of the Browser Tools. In 'Console' we can add any JavaScript functions we want, and if we set a pre-existing function to new code, the new code will take over. So in the 'Console' we may type a line like ```validateCode = () => {true}```. This will make validateCode return true every time it is called so that when we hit 'Register Now!' our registration request will go through to the server and we will get a webpage back with the flag!

## Other Solutions
Another way to get the flag would be to ignore the website altogether. The issue with the website is that it will prevent a Post request from being sent due to your date being out of the registration range, so instead of being limited by checks, one could simply send a Post request directly to the server without any hassle. They way to send a Post request would be to use an application like 'Postman'.
