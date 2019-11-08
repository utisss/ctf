# Juggular
* **Event:** Security Day CTF
* **Problem Type:** Web

## Background
PHP is a language that powers most of the web. PHP Type Juggling is a language "feature" which allows values compared using the weak == operator (instead of the strong === operator) to be implicitly type-coerced. 

## Steps
We are looking for a number, whose md5 hash == "0e574837584728375847385748394857". When two strings are compared in PHP, if PHP decides the strings look like numbers, it'll convert them both to numbers and then compare the two numbers. In this case, the md5 hash would get converted to the numeric value 0, since the scientific notation 0e5748... = 0 * 10^5748... which is 0. 

Using the value '240610708', (from [here](https://www.php.net/manual/en/function.md5.php) or [here](https://news.ycombinator.com/item?id=9484757)), we find another hash with the same format, which would also get coerced into 0. Type the number into the page and get the flag. 