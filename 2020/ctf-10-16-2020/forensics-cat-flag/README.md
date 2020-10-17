# Cat Flag
* **Event:** Security Day CTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **Tools Required / Used:** binwalk

## Solution

There are four JPEG files concatenated into one file. Binwalk is handy for extracting files in these situations.

```sh
binwalk -D='jpeg:jpg' cat.jpg
```
