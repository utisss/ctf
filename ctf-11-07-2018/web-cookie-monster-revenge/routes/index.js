var express = require('express');
var md5 = require("md5");
var router = express.Router();

const TRUE_HASH = md5("true").toLowerCase();
const FALSE_HASH = md5("false").toLowerCase();

/* GET home page. */
router.get('/', function(req, res, next) {
    const vars = {
        image: 'https://i.imgur.com/lpph6lZ.png',
        title: 'Cookie Monster\'s Revenge',
        flag: '',
    };

    if (req.cookies["login"] === "true" && req.cookies["hash"] && req.cookies["hash"].toLowerCase() === TRUE_HASH) {
        vars.image = 'https://i.imgur.com/wc7osvf.jpg';
        vars.flag = 'utflag{c00k13_1nt3gr1ty}';
    } else {
        res.cookie("login", "false");
        res.cookie("hash", FALSE_HASH)
    }
    res.render('index', vars);
});

module.exports = router;
