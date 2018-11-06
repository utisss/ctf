var express = require('express');
var router = express.Router();
const Users = require("../users");

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.redirect('/');
});

router.post('/', function(req, res, next) {
  let username = req.body.username.trim();
  let otp = req.body.password || "";

  if (otp.length !== 6 || !Users.verifySecret(username, otp)) {
      res.redirect('/?incorrect=1');
      return;
  }

  res.render('home', {
      flag: username === "willh"
  });
});

module.exports = router;
