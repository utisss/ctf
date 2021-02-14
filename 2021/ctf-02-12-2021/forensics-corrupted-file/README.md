 # Unfortunate File
 * **Event:** stonksCTF
 * **Problem Type:** Forensics
 * **Point Value / Difficulty:** Easy (200 pts)
 * **(Optional) Tools Required / Used:** a hex editor
 ## Steps
 ### Step 1
 When you try to open the file, you'll get an error. If you inspect the contents of the file in a hex editor, nothing might stand out immediately. It might be a good idea to look up the header format for the file type you're looking at (in this case, [the m4a file header format](https://www.file-recovery.com/m4a-signature-format.htm)). The other technique I like to try is to get another (valid) file of the same type and compare the header bytes for differences.

 ### Step 2
 Upon closer inspection, we notice that the signature `ftyp` is missing from where it should be (4 bytes into the file). Modifying the bytes to include it back in will fix the file.

 ### Step 3
 Play the audio. It will tell you your "lucky numbers" that you can put inside the curly braces for "utflag{...}".
