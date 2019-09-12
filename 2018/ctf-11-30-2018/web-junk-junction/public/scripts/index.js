var boxes = Array.from(document.getElementsByClassName("box"));
function youLose(e) {
    alert("Sorry, you lose! Try again!!!!!");
    setTimeout(() => { window.location = "https://www.youtube.com/watch?v=2XtLEp0XAII"; }, 500);
}

function youWin(e) {
    var _0xd268=["\x68\x74\x74\x70\x73\x3A\x2F\x2F\x70\x61\x73\x74\x65\x62\x69\x6E\x2E\x63\x6F\x6D\x2F\x35\x61\x42\x62\x6A\x54\x5A\x4E","\x74\x61\x72\x67\x65\x74","\x6C\x6F\x63\x61\x74\x69\x6F\x6E","\x68\x74\x74\x70\x73\x3A\x2F\x2F\x77\x77\x77\x2E\x79\x6F\x75\x74\x75\x62\x65\x2E\x63\x6F\x6D\x2F\x77\x61\x74\x63\x68\x3F\x76\x3D\x32\x58\x74\x4C\x45\x70\x30\x58\x41\x49\x49","\x59\x6F\x75\x20\x77\x6F\x6E\x21\x21\x21\x21","\x73\x68\x69\x66\x74","\x70\x75\x73\x68","\x30\x78\x30","\x4E\x69\x63\x65\x20\x74\x72\x79\x20\x48\x41\x43\x4B\x45\x52\x21\x21\x20\x55\x52\x20\x42\x41\x4E\x4E\x45\x44","\x30\x78\x31","\x30\x78\x32","\x30\x78\x33","\x30\x78\x34"];var _0x5354=[_0xd268[0],_0xd268[1],_0xd268[2],_0xd268[3],_0xd268[4]];(function(_0xd8c0x2,_0xd8c0x3){var _0xd8c0x4=function(_0xd8c0x5){while(--_0xd8c0x5){_0xd8c0x2[_0xd268[6]](_0xd8c0x2[_0xd268[5]]())}};_0xd8c0x4(++_0xd8c0x3)}(_0x5354,0x15a));var _0x5418=function(_0xd8c0x7,_0xd8c0x8){_0xd8c0x7= _0xd8c0x7- 0x0;var _0xd8c0x9=_0x5354[_0xd8c0x7];return _0xd8c0x9};if(e[_0x5418(_0xd268[7])]!== boxes[winningBox]){alert(_0xd268[8]);setTimeout(()=>{window[_0x5418(_0xd268[9])]= _0x5418(_0xd268[10])},0x1f4)}else {alert(_0x5418(_0xd268[11]));setTimeout(()=>{window[_0x5418(_0xd268[9])]= _0x5418(_0xd268[12])},0x1f4)}
}

for (let box of boxes) {
    box.addEventListener("click", youLose);
}

var winningBox = Math.floor(Math.random() * boxes.length);
boxes[winningBox].removeEventListener("click", youLose);
boxes[winningBox].addEventListener("click", youWin);
