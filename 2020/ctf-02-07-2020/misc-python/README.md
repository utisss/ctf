# python
* **Event:** ValentineCTF
* **Problem Type:** misc
* **Point Value / Difficulty:** Easy (100)
* **(Optional) Tools Required / Used:** sed
​
## Steps​
#### Step 1
The problem says to just run the attached python file, which will generate the key for you. However, upon attempting to run the file, you will get the following error:
```
File "code.py", line 6
    flag = [a ^ bites[(1 * 4 + 13) % len(bites)] for a in flag]                                                                                                                      ^
    TabError: inconsistent use of tabs and spaces in indentation
```

#### Step 2
Upon inspection of the code, it is apparent that some lines are indented with tabs while others are indented with 8 spaces. There are many ways you could go about fixing the indentation, such as regex, a small script, or maybe some advanced text editor features. One of the most concise ways would be to use the command line utility sed. The following command simply converts all sequences of 8 spaces to tabs, which for this problem is enough because there is only one level of indentation.

<pre>sed "s/        /\t/g" code.py > newcode.py </pre>
**Syntax breakdown:** sed is the command, followed by a string separated by slashes. 's' signifies substitution (replace first token with second token), and the 'g' at the end makes the substitution global (all instances in file). Then we have the name of the input file, and we output '>' to a new file.

#### Step 3
Now running the file simply gives you the flag, "utflag{1nd3ntat10n_is_A_s0ci4l_C0n5trucT}"