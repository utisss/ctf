const request = require("request-promise");

async function test() {
    var body = await request({
        method: "POST",
        uri: "http://localhost:3000/",
        form: {
            "pin": "0000000000000000",
        }
    });

    console.log(body);
}

test();