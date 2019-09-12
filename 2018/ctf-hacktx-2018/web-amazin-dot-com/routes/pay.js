
var express = require('express');
var router = express.Router();

const FLAGHASH = "2e8405f30c23277909941604e77b0e880cb5794e";

/* GET checkout page. */
router.get('/pay', function (req, res, next) {
    const hash = req.query.hash;
    if (!hash || hash !== FLAGHASH) {
        res.redirect('/');
    }

    res.render('pay', {
        title: 'Payment Confirmed',
        flag: 'utflag{4m4z1n_3l1t3_st4tus_c0nf1rm3d}',
    });
});

module.exports = router;
