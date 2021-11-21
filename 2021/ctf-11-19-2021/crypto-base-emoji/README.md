# Crypto: Base Emoji
This challenge's description and name are supposed to evoke the base64 encoding algorithm, 
which is a method to encode binary data as ASCII characters. This challenge's encoding 
algorithm is slightly different than base64, but is similar in that character ranges are 
mapped sequentially. The way to figure this problem out is to decode the characters to 
Unicode (on [this site](https://www.online-toolz.com/tools/text-unicode-entities-convertor.php) for
example), and then use the knowledge that the first 7 characters are `utflag{` to reverse-engineer
the encoding method.

