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

app.post('/:content', async function(req, res, next) {
  try{
    const browser = await puppeteer.launch({args: ['--no-sandbox', '--headless', '--disable-gpu']});
    const page = await browser.newPage();
    await page.setCookie({url: 'http://localhost:'+port, name: "flag", value: process.env.FLAG});
    await page.goto('http://localhost:'+port+"/view/"+req.params.content, {waitUntil: 'networkidle2'});
    await new Promise(resolve => setTimeout(resolve, 2000));
  
    await browser.close();
  
    res.send("An admin has reviewed your feedback. <a href=\"view/" + req.params.content + "\">Admin view</a>");
  }catch(e) {
    res.send("error");
    return;
  }
})

app.get('/view/:content', function(req, res) {
  const content = Buffer.from(req.params.content, 'base64').toString();

  res.render('viewFeedback', {content});
})

module.exports = app;
