# PNG
This problem gives you a valid PNG file that just looks a bit weird.

You can open this file in a hex editor, and the flag is simply a part of the 
file. You can also run `strings nothing.png` in a UNIX-like environment.

The `strings` utility searches the file for human-readable strings; in this 
case, the only human-readable string in the file is the flag directly 
embedded within the PNG file. The reason why the PNG file looks weird is that
the flag is being interpreted as color data when it is ASCII data.