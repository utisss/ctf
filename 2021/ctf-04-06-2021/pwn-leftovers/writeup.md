Since we dont initialize the data in check_pass, it will simply contain whatever data was left on the stack from
get_input. We can put in some random data to get_input, and see where it ends up being used in check_pass using gdb.
From there we can decide where in the data we give to get_input to put the number and string. That will give us a shell,
where we can cat the flag
