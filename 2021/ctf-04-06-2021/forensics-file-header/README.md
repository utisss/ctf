# File Headers are Universal
* **Event:** gallacticBattleCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:** hex editor 

## Steps
### Step 1
Upon analyzing the file, we see that it's a .png image file, but we can't seem to open it as one for some reason. Let's check that it really is a proper PNG file.

### Step 2
You can look up the file header of a PNG file and see that it should start with the following bytes: `89 50 4E 47 0D 0A 1A 0A`. However, if we open up the flag.png file in a hex editor, we can see that the first byte is actuall `88`. Fixing it to the proper header format should allow us to open the image and see the flag.
