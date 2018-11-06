var express = require('express'), path = require('path')
var app = express()

app.set('port', (process.env.PORT || 5000))
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static("scripts"))
app.use(express.static("static"))

app.set('view engine', 'pug');
app.set('views', './views');


app.get('/', function (req, res) {
    res.render("index");
});

app.get('/space', function (req, res) {
    // res.send(req.query.path);

    if (req.query.path.constructor === Array) {
        if (req.query.path.includes('flag')) {
            var rocketBool = req.query.path.includes('rocket')
            var engineBool = req.query.path.includes('engine')
            res.render("flag", { rocketBool: rocketBool, engineBool: engineBool });
        }
    }

    switch (req.query.path) {
        case "mars":
            res.render("mars");
            break;
        case "rocket":
            res.render("rocket");
            break;
        case "anime":
            res.render("anime");
            break;
        case "engine":
            res.render("engine");
            break;
        case "flag":
            res.render("flag");
            break;
        default:
            res.render("404");
            break;
    }
});


app.get('/afd0864b3bf3090721aab7c424432f5a/d8vnzavnqy9qsavnwfrwhfeyninn9hfr7xt4v6s2rbgrxunk9abuxxgndxk9vsn6/flag', function (req, res) {
    res.send("utflag{i_sh0uldve_ch3cked_s3rv3r_s1d3}");
});

app.listen(app.get('port'), function () {
    console.log("Node app is running at localhost:" + app.get('port'))
})