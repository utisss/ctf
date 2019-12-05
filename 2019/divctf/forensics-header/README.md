# Magic Signature
* **Event:** DivCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:** Sonic Visualizer or Audacity

## Steps​
#### Step 1
The prompt mentions needing a magic header or signature, and when you try to open the image, you will get an error and be unable to see it. The prompt is referring to [magic bytes](https://en.wikipedia.org/wiki/List_of_file_signatures) (or file signature, or file header), which is the term often used to describe the first few bytes (exact number varies) that are at the start of a file. Each filetype has a specific sequence of magic bytes, and that's how your computer knows what kind of file it is.

#### Step 2
In this case, if we open up the image in a program like [Bless](https://github.com/bwrsandman/Bless), `xxd` or my favorite, [`hexyl`](https://github.com/sharkdp/hexyl), we will see that the first four bytes of this JPEG are `00 00 FF DB`, when a JPEG's header should be `FF D8 FF DB`.

#### Step 3
If we use a hex editor like Bless, we can change those first two bytes back to `FF D8`, save the file, and then open the image to get the flag: `utflag{can_i_get_your_signature}`.
