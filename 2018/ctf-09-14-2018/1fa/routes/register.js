var express = require('express');
var router = express.Router();
const Users = require("../users");
const QRCode = require("qrcode");

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.redirect('/');
});

router.post('/', function(req, res, next) {
  let username = req.body.username.trim();
  let timestamp = parseInt(req.body.t, 10);

  if (!(username.length > 0) || isNaN(timestamp) || timestamp < 0) {
    res.redirect('/?error=1');
    return;
  }

  if (Users.getSecret(username)) {
    res.redirect('/?userExists=1')
    return;
  }

  const secret = Users.createSecret(username, timestamp);
  QRCode.toDataURL(secret.otpauth_url, function(err, data_url) {
    res.render('register', {
      username,
        code: data_url,
        firstIndex: Users.firstIndex,
        yourIndex: Users.getIndex(username),
    });
  });

  return;
});

module.exports = router;
