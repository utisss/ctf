# SCavenger Hunt
* **Event:** uwuCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** 200 (Easy)
* **(Optional) Tools Required / Used:** exiftool or strings 

### Solution
1) Based on the hint, we need to check the metadata on the image. exiftool is one tool that can view the metadata; another option in this case is to run `strings`.
2) Running `exiftool snap.jpg` or `strings snap.jpg | grep flag` would help you find a comment that says "the flag is on the fourth floor of GDC". From there, you go up to the fourth floor bridge and find `utflag{thats_so_meta}` written on one of the whiteboards.
