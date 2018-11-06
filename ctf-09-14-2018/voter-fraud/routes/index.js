var express = require('express');
var router = express.Router();
const vote = require("../vote");
const config = require("../config");

/* GET home page. */
router.get('/', function(req, res, next) {
    const vars = {
        title: 'WHO WOULD WIN?',
        william: vote.counts[0].toString(),
        neil: vote.counts[1].toString(),
        brian: vote.counts[2].toString(),
        jonathan: vote.counts[3].toString(),
        flag: "",
    };
    if (req.query.hash === config.hash) {
        vars.flag = "On behalf of [REDACTED], thank you for your contributions. Here is a reward: " + config.flag;
    }

    res.render('index', vars);
});

module.exports = router;
