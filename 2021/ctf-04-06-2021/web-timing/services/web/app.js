var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var exphbs  = require('express-handlebars');

var app = express();

var port = Number.parseInt(process.env.PORT || '3000');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.engine('handlebars', exphbs());
app.set('view engine', 'handlebars');

app.get('/', function(req, res, next) { 
  res.render('index');
});

async function sleep(n) {
  await new Promise((resolve, reject) => {
    setTimeout(resolve, n);
  })
}

const password = "07005748";

app.post('/:password', async function(req, res, next) {
  for(let i = 0; i < 8; i++) {
    if(password.charAt(i) !== req.params.password.charAt(i)) {
      res.send("Failed to authenticate");
      return;
    }

    await sleep(1000);
  }

  res.send("Success! The flag is utflag{t1m1ng_1s_tr1cky}");
})

module.exports = app;
