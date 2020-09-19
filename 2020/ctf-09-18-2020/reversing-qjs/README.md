# Reverse Engineering: QuickJS
In this challenge, the user is given an incomplete exploit of the QuickJS
engine, which is running on the server. The exploit asks the user to provide 
the offset of putc@plt from a native function pointer (js\_print). If the 
correct offset is given, the exploit completes and a shell is returned.

## Prompt
My friend ported his Tetris JavaScript code to a cool new JavaScript engine 
called QuickJS. I managed to find a exploit for QuickJS, but I'm missing one 
value. Can you send me the correct value to complete the exploit?

`nc ctf.isss.io 4250`

## Hint
gdb is your friend.

## Flag
`utflag{quickjs_more_like_slow_js}`
