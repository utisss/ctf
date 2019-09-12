# Thicc-fil-A
* **Event:** BepisCTF (ISSS CTF 09-06-2016)
* **Problem Type:** Web
* **Point Value / Difficulty:** TBD
* **Tools Used:**
    * Browser Tools - Only tools needed for this is the built-in browser tools to adjust the source

## Background
[Client-side Validation](https://cwe.mitre.org/data/definitions/602.html) is a common mistake made by both young and seasoned developers. Essentially, the idea is that the server trusts that the user won't manipulate the client and remove any checks or validations. For example, a minimum and maximum range to adjust a thermostat. Since the server trusts whatever the client sends it, this can be manipulated to cause a number of issues.


## Steps
### Open up the Browser Tools
Open up the Browser Tools. There are numerous ways to do this, depending on your preferences and browser. In Chrome, Ctrl+Shift+I accomplishes this task.

### Locate the temperature slider
Somewhere within the body of the page, there is a form. Inside that form, you will find the range slider and the submit button. This is where you will edit the HTML to remove the minimum and/or maximum client-side restrictions.

### Increase the max or Decrease the min
Edit the HTML to increase the maximum to a higher number or decrease the minimum to a lower number. This will now allow you to change the temperature value to one outside of the original range.

### Set the temperature outside the original range
Any value below 100 or above 400 will work. Hit set. The flag should be printed back to the user.

## Other Solutions
Another way this problem could be solved is by replaying the POST request sent when submitting the form, but with a different temp value. This is simple to do in Firefox, but requires an extension in Chrome. Just open the networking tab and locate the post request. In Firefox, you can right-click and select _Edit and Resend_. Here, you can change the temp value to anything you want. Setting this outside of the 100-400 range and sending the request would also yield the flag.
