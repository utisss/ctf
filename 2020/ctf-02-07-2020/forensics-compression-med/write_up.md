# Love is Compressing
* **Event:** ISSS Valentime CTF (February 7th, 2020)
* **Problem: Type:** Forensics
* **Point Value:** 200

## Background
There are several popular ways to compress files in Linux. For this problem 
the tar, gzip2, and bzip compression schemes were used at random (with no 
scheme occurring more than once in a row) on a regular file holding the flag. 
These compression schemes are particularly nice because the can be used to 
compress a file virtually infinite times, which is what inspired this 
challenge. It is not impossible to do this problem 'by hand', however it is 
highly recommended that you write a script (bash for example).

#### Solution
The way you would write a script to solve this problem, would first be to 
use the 'file' command to inspect what file type you currently have. The 
file command will tell you if a file has been compressed via tar, bzip, or 
gzip2. Next you use the accompanying decompression command (the 3 compression 
schemes listed here all have decompression counterparts) to retrieve a 
decompressed copy of the original file. You complete this step of figuring out 
how a file has been compressed, and which tool is need to correctly decompress 
the file until you reach a file that is in plain ASCII text (which the file 
command will tell you.)
