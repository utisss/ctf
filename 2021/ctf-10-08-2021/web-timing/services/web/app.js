var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var exphbs  = require('express-handlebars');

const puppeteer = require('puppeteer');

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

const PASSWORD = "3234187225";

app.post('/checkPassword/:guess', async function(req, res, next) {
  const guess = req.params.guess;
  let nCorrect = 0;
  for(nCorrect = 0; nCorrect < guess.length; nCorrect++) {
    if(guess[nCorrect] !== PASSWORD[nCorrect]) break;
  }

  await new Promise(resolve => setTimeout(resolve, nCorrect * 100));

  if(guess === PASSWORD) {
    res.send("Success! The flag is: " + process.env.FLAG);
  }else{
    res.send("Try again!");
  }
})

module.exports = app;
