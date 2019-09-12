var express = require('express');
const Users = require("../users");
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  const renderTime = Date.now() - 1;
  res.render('index', {
    title: 'Amazin Web Services',
    timestamp: renderTime,
    userExists: req.param('userExists'),
    error: req.param('error'),
    incorrect: req.param('incorrect'),
    uptime: renderTime - Users.initialTimestamp,
  });
});

module.exports = router;
