const puppeteer = require("puppeteer");
const browser = puppeteer.launch({
  args: 
    ["--no-sandbox",
    '--disable-setuid-sandbox',
    '--ignore-certificate-errors',
    '--proxy-server="direct://"',
    '--proxy-bypass-list=*'],
  headless: true
});

function delay(time) {
   return new Promise(function(resolve) { 
       setTimeout(resolve, time)
   });
}

async function validate(input) {

  try {
    const page = await(await browser).newPage();

    page
    .on('console', message =>
      console.log(`${message.type().substr(0, 3).toUpperCase()} ${message.text()}`))
    .on('pageerror', ({ message }) => console.log(message))
    .on('response', response =>
      console.log(`${response.status()} ${response.url()}`))
    .on('requestfailed', request =>
      console.log(`${request.failure().errorText} ${request.url()}`))

    // Navigate the page to a URL
    await page.goto("http://localhost:9000/index.html");

    // Set screen size
    await page.setViewport({width: 1080, height: 1024});

    // Set flag as cookies
    let cookies = [{
      "name": "flag",
      "value": "utflag{4ma11y_v3rif!ed_t0_b3_m3m0rY_s4fe_L0l}"
    }];
    await page.setCookie(...cookies);

    // Type into encrypt box
    await page.type("#decryptInput", input);
    await page.waitForSelector("#decryptBtn");
    await page.click("#decryptBtn");
    await page.waitForSelector("#status", {timeout: 30000});

    await delay(2000)
    await page.waitForNetworkIdle();

    await page.close();
  } catch (error) {
    console.log(error);
  }
}

const fs = require("fs");
const http = require("http");
const querystring = require("querystring");

// Make our HTTP server
const server = http.createServer((req, res) => {
  const userAgent = req.headers['user-agent'];
  console.log(userAgent);
  if (req.url == "/wasm.js") {
    res.writeHead(200, { "Content-Type": "text/javascript" });
    var html = fs.readFileSync("./pkg/wasm.js");
    res.write(html);
  } else if (req.url == "/wasm_bg.wasm") {
    res.writeHead(200, { "Content-Type": "application/wasm" });
    var html = fs.readFileSync("./pkg/wasm_bg.wasm");
    res.write(html);
  } else if (req.method == "POST" && req.url == "/post") {
    res.writeHead(200, { "Content-Type": "text/html" });
    //if (userAgent.includes("HeadlessChrome") || userAgent.includes("Chrome")) {
    if (userAgent.includes("HeadlessChrome")) {
      res.write("<p>denied</p>");
    } else {
      res.write("<p>received</p>");
      let body = "";
      // Accumulate chunks of data
      req.on("data", chunk => {
          body += chunk.toString();
      });

      // When the entire request has been received
      req.on("end", () => {
        // Parse the body as URL-encoded form data
        const postData = querystring.parse(body);
        // Extract the specific parameter
        const encrypt = postData.encrypt;

        // Check if the parameter exists
        if (encrypt !== undefined) {
            console.log("Encrypt: " + encrypt);
        }

        const decrypt = postData.decrypt;

        if (decrypt !== undefined) {
          console.log("Decrypt: " + decrypt);
          validate(decrypt);
        }
      });
    }
  } else {
    res.writeHead(200, { "Content-Type": "text/html" });
    var html = fs.readFileSync("./html/index.html");
    res.write(html);
  }
  res.end();

});

// Have the server listen on port 9000
server.listen(9000);
