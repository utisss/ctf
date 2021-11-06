# Reversing Wasm

We can begin by running wasm-decompile on enc.wasm, and we get the following
output:
```
export function encrypt(a:int, b:int):int {
  return a * b + 3389592
}
```

We can look in index.html to get that the value of b is always 38774 and our
flag is encrypted to:
```
[7926150, 7887376, 7344540, 7577184, 7150670, 7383314, 8158794, 8003698, 7150670, 7848602, 7615958, 7073122, 7460862, 7848602, 7073122, 7887376, 7422088, 7305766, 7073122, 8003698, 5250744, 7809828, 7848602, 7887376, 8236342]
```


We can simply subtract 3389592 from each number and divide by 38774 to get the flag. 

```
[7926150, 7887376, 7344540, 7577184, 7150670, 7383314, 8158794, 8003698, 7150670, 7848602, 7615958, 7073122, 7460862, 7848602, 7073122, 7887376, 7422088, 7305766, 7073122, 8003698, 5250744, 7809828, 7848602, 7887376, 8236342].map(a => String.fromCharCode((a - 3389592) / 38774)).join('')
```