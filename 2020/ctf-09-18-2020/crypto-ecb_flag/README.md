# ECB Flag
* **Event:** TetrisCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium

## Solution

The provided code consists of a Python script that calls a custom crypto library. The library encrypts data using AES with 128 bit keys in ECB mode. The library uses Intel's instructions for hardware AES calculations. The library also provides a random key generator using Intel's RAND instruction.

The code converts a 1920x1080 RGBA PNG into an array of bytes. The output is 1920x1080x4 bytes. Thus, to represent the encrypted data as an image just load the bytes into a 3D array, and use PIL to display the image.

The flag will be visible, even though the image was "encrypted". The fatal flaw of ECB mode is that blocks are encrypted independently from each other, so blocks with the same value encrypt to the same output. Even though the value of an individual block cannot be determined from the cipher text, patterns that span accross multiple blocks may be preserved. In this case, the numerous runs of contiguous black pixels that comprised the plaintext have been transformed into a different color. However, the contrast from the background is perserved.

This problem is based off of the famous ECB penguin image.
