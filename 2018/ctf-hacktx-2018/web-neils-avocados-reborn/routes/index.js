var express = require('express');
var router = express.Router();

var PASSWORD = "0451";

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: "Neil's Avacados Reborn", time: Math.round(Math.random() * 50) + 50 });
});

router.post('/', function(req, res, next) {
  let pin = req.body.pin || "";

  if (pin.length !== PASSWORD.length) {
    res.render('index', { title: "Neil's Avacados Reborn", time: Math.round(Math.random() * 50) + 50 });
    return;
  }

  if (pin === PASSWORD) {
    res.render('flag', { title: "You're In!" });
    return;
  }

  let sumTime = Math.round(Math.random() * 50) + 50;
  for (let i = 0; i < PASSWORD.length; ++i) {
    if (pin.charAt(i) === PASSWORD.charAt(i)) {
      sumTime += 200 + Math.round(Math.random() * 20);
      continue;
    }

    break;
  }

  res.render('index', { title: "Neil's Avacados Reborn", time: sumTime, incorrect: true });
});

module.exports = router;
