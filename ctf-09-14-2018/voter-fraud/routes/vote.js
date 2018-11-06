var express = require('express');
var router = express.Router();
const url = require("url");
const vote = require("../vote");
const config = require("../config");

/* POST vote */
router.post('/', function(req, res, next) {
    let id = req.body.id;
    let value = req.body.value;
    if (!id || !value) {
        res.redirect('/');
        return;
    }

    id = parseInt(id, 10);
    const solved = vote.cast(id, value);
    if (solved) {
        res.redirect(url.format({
            pathname: "/",
            query: {
                hash: config.hash,
            }
        }));
        return;
    }

    res.redirect('/');
});

module.exports = router;
