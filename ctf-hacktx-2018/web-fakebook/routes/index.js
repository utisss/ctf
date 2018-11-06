var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  let props = { title: 'Fakebook' };
  if (req.query.register) {
    props.register = true;
  }
  if (req.query.login) {
    props.login = true;
  }
  if (req.cookies["SESSION"] === "292cbbbb13783255623fc98eb05a615494f7e58d7aabdce1d1bf346e0c98fc137fd7a426e818f8c30310a62c9f4edb7d000cf32c90e36aec5214fef9ae87d8e3") {
    props.flag = "utflag{f4c3b00k_s3ll0ut_l1z4rds}";
  }
  res.render('index', props);
});

router.get('/tos', function(req, res, next) {
  res.send('We own you.');
});

module.exports = router;
