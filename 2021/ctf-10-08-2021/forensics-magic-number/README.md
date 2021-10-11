# Corrupted Proof
This problem gives you a corrupt image file, and asks you to uncover what's hidden inside. The hint
refers to "magic numbers", which is meant to guide you towards 
[file magic numbers](https://en.wikipedia.org/wiki/File_format#Magic_number). Basically, many types
of files indicate what kind of file they are by starting the file with a magic number. Here's a good
list of them: [https://asecuritysite.com/forensics/magic](https://asecuritysite.com/forensics/magic).
The file given in this challenge has a magic number (in hex) of `47494638`, corresponding to the GIF
file format. However, if you investigate the file using a text editor (like notepad or vim), you'll
find the word IHDR, which if you google around, tells you the file was originally a PNG image. If
you use a binary/hex editor to change the file's magic number to a PNG (`89504e47` in hex), then the
file will open correctly, revealing the flag.

