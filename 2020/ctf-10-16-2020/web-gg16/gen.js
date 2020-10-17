const flag = "utflag{emu_gt_vhdl_}";
const res = [];

for(let i = 0; i < flag.length; i++) {
    const enc = flag.charCodeAt(i) * 13 + 17;
    res.push(enc & 0xff);
    res.push((enc >> 8) & 0xff);
}

console.log(JSON.stringify(res));