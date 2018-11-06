var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.cookie('flag', '_t00lz}')
  res.render('index', { title: 'Browser Developer Tools Tutorial' });
});

module.exports = router;
