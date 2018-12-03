var express = require('express');
var router = express.Router();

var PASSWORD = "43760429";

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: "Neil's Avacados Revenge" });
});

router.post('/', function(req, res, next) {
  let pin = req.body.pin || "";
  console.log(req.body);
  console.log(`PIN: ${pin}`);

  if (pin === PASSWORD) {
    res.render('flag', { title: "You're In!" });
    return;
  }

  let sumTime = 0;
  for (let i = 0; i < PASSWORD.length; ++i) {
    if (pin.charAt(i) === PASSWORD.charAt(i)) {
      sumTime += 500 + Math.round(Math.random() * 50);
      continue;
    }

    break;
  }

  setTimeout(() => {
    res.render('index', { title: "Neil's Avacados Revenge", incorrect: true });
  }, sumTime);
});

module.exports = router;
