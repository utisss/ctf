# Tab Overflow
* Difficulty: Easy
* Problem Type: Web
* Tools Needed: Bash scripting
## Explanation
The letters of the flag are hidden in the 1000 tabs opened by the program. To solve you just need to request all 1000
and add the results together. My favorite tool for this is the cli program httpie, but you could use a lot of different
things. curl, wget, or python + a http lib would all work. Here is the solution I used

```bash
for i in {1..1000}; do http "ctf.isss.io:5001/"$i".html" >> sol; done
```
