var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    const vars = {
        image: 'https://i.imgur.com/lpph6lZ.png',
        title: 'Cookie Monster',
        flag: '',
    };

    if (parseInt(req.cookies["login"], 10) === 1) {
        vars.image = 'https://i.imgur.com/wc7osvf.jpg';
        vars.flag = 'utflag{c00k13_0v3rd0s3}';
    } else {
        res.cookie("login", "0");
    }
    res.render('index', vars);
});

module.exports = router;
