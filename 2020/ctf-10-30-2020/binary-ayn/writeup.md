# Ayn
# Binary Exploitation: Medium

After analyzing the binary, we notice that it calls srand(time(NULL)) at the beginning 
and generates a number based on that. Our goal is to predict the number correctly,
which will then lead to the program giving us a shell. 

The easiest way to exploit this is to notice that time(NULL) has second-accuracy, so we 
can simply open two connections to the server simultaneously, grab the number given to
us by one of the connections, then send it over to the other connection. 

Then we can type "ls /" to see that there is a "flag.txt" file at root, then "cat flag.txt"
to get the contents. 