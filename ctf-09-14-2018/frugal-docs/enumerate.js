const alphabet = "abcdefghijklmnopqrstuvwxyz".split('');
const MAX_LETTERS = 3;
const MAX_NUMBER = Math.pow(alphabet.length, MAX_LETTERS);

function left_pad(str) {
    while (str.length < MAX_LETTERS) {
        str = alphabet[0] + str;
    }

    return str;
}

for (let i = 0; i < MAX_NUMBER; ++i) {
    let num = i;
    let output = "";
    while (num > 0) {
        output = alphabet[num % alphabet.length] + output;
        num = Math.floor(num / alphabet.length);
    }

    console.log(left_pad(output));
}
