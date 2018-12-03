var express = require('express');
var router = express.Router();

const FLAGHASH = 'bd4682dbd41da457d4ebe4f587f7f794b53e9be7';


function formatDate(date) {
  var monthNames = [
    "January", "February", "March",
    "April", "May", "June", "July",
    "August", "September", "October",
    "November", "December"
  ];

  var day = date.getDate();
  var monthIndex = date.getMonth();
  var year = date.getFullYear();

  return day + ' ' + monthNames[monthIndex] + ' ' + year;
}

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { 
    title: 'Honeymoat Remote Thermostat 2.0', 
    date: formatDate(new Date()),
    temp: req.query.prevtemp || 72,
    flag: req.query.flag === FLAGHASH ? "utflag{h0n3ym04t_p4ys_h0n3yw3ll}" : "",
 });
});

router.post('/submit', function(req, res, next) {
  let temp = parseInt(req.body.temp, 10);
  if (isNaN(temp)) {
    res.redirect('/');
    return;
  }

  if (temp < 0 || temp > 100) {
    res.redirect(`/?flag=${FLAGHASH}&prevtemp=${temp}`);
    return;
  }
  
  res.redirect(`/?prevtemp=${temp}`);
});

module.exports = router;
