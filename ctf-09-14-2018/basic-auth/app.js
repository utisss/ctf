const express = require("express");
const auth = require("basic-auth");
const app = express();

app.use(function(req, res, next) {
    var user = auth(req);

    if (user === undefined || user['name'] !== 'jfish' || user['pass'] !== 'utflag{pr43t0r14n_s3ll0ut}') {
        res.statusCode = 401;
        res.setHeader('WWW-Authenticate', 'Basic realm="Illuminati Welcome Portal"');
        res.end('Unauthorized');
    } else {
        next();
    }
});

app.get("/", (req, res) => {
    res.send("You have come too far...");
});

app.listen(3000, () => console.log("Listening on port 3000!"));
