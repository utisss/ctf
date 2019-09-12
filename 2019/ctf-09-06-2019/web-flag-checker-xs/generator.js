function x(a, i) {
    return a.map(v => v ^ i);
}
function r(a, i) {
    return a.map(v => (v + i) % 256);
}
function caesar (s, i) {
    const a = 'a'.charCodeAt(0);
    const z = 'z'.charCodeAt(0);
    const zero = '0'.charCodeAt(0);
    const nine = '9'.charCodeAt(0);
    return s.split('')
            .map(c => c.charCodeAt(0))
            .map(cc => cc >= a && cc <= z? (cc - a + 26 + i) % 26 + a : cc)
            .map(cc => cc >= zero && cc <= nine? (cc - zero + 30 + i) % 10 + zero: cc)
            .map(cc => String.fromCharCode(cc))
            .join('');
}
function bytesify(str) {
    return str.split('').map(c => c.charCodeAt(0));
}
function obfuscate(code) {
    const shift = Math.floor(Math.random() * 26);
    return 'ce("' + caesar(code, shift).replace(/\\/g, '\\\\').replace(/"/g, '\\"') + '",' + (- shift) + ')'
}
function obfuscate1(code) {
    const key = Math.floor(Math.random() * 256);
	return `xe(${JSON.stringify(x(bytesify(code), key))}, ${key})`;
}

code = "flag === 'utflag{screw_you_javascript_99472}'";
for(let i = 0; i < 3; i++){
    code = obfuscate1(code);
}