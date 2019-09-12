# Flag Checker Sr
* **Event:** BepisCTF (ISSS CTF 09-06-2016)
* **Problem Type:** Web
* **Point Value / Difficulty:** Medium
* **Tools Used:**
    * Chrome dev tools

## Background
[Array#map, Array#reduce in JavaScript](https://medium.com/poka-techblog/simplify-your-javascript-use-map-reduce-and-filter-bd02c593cc2d)
[eval()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)

## Steps
Looking at the source code, we notice that there is a string in `code.js` which is eval()ed in order to check the user's flag guess. There are also some functions contained in `index.html` which are `xe` and `ce` respectively. Through some analysis, we find that `xe` accepts an array of bytes and a byte, xor's the byte with each element of the array, then converts the array to a string and eval()s it. `ce` is similar, but it accepts a string and an offset and performs a modified caesar-cipher rather than an xor cipher.

The eval()ed code seems to be nested several layers deep in calls to `xe` and `ce`, and each layer is encrypted with a random key. 

In order to get to the lowest level, we can modify the xe and ce functions by going into the console and redefining them:
```javascript
function xe(a, i) {
    let decrypted = a.map(v => v ^ i)
        .map(cc => String.fromCharCode(cc))
        .join('');
    console.log(decrypted);

    return eval(decrypted);
}
function ce(s, i) {
    const a = 'a'.charCodeAt(0);
    const z = 'z'.charCodeAt(0);
    const zero = '0'.charCodeAt(0);
    const nine = '9'.charCodeAt(0);
    let decrypted = s.split('')
        .map(c => c.charCodeAt(0))
        .map(cc => cc >= a && cc <= z? (cc - a + 26 + i) % 26 + a : cc)
        .map(cc => cc >= zero && cc <= nine? (cc - zero + 30 + i) % 10 + zero: cc)
        .map(cc => String.fromCharCode(cc))
        .join('');
    console.log(decrypted);

    return eval(decrypted);
}
```

This will console.log the decrypted text each time the text is decrypted, but otherwise act identically to the provided functions. We use the form to check another flag guess and the real flag is revealed in the browser console. 