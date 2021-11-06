const puppeteer = require("puppeteer");
const HOST = "http://localhost:5000";

(async () => {
    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();
    await page.goto(HOST);
    while(true){
        await page.evaluate(() => {
            let chal = document.querySelector("label").innerText;
            chal = chal.substring(0, chal.length - 4);
    
            soln = eval(chal);
            
            document.querySelector("input[name='solution']").value = soln;
        });

        await Promise.all([
            page.click("input[type='submit']"), 
            page.waitForNavigation({waitUntil:'networkidle2'})
        ]);


    }
    
})();