# It's Web Time
# Difficulty: Easy

In this challenge, you are tasked with finding out a passowrd, which you are 
told is an 8-digit number.

After trying a few combinations, we notice that some passwords fail to
authenticate almost instantly, while others take a few seconds. This tells 
us that this is a timing attack challenge. 

For example, the password "0" takes 1 second to fail, while the 
password "1" fails instantly, so we know that the first character is probably
"0". Then, we try to extract the second character. We find that "07" takes 2
seconds to fail while 0 followed by any other character takes just 1 second.

We can continue the process by hand using a stopwatch, extracting one 
character at a time until we get the full password.