const puppeteer = require('puppeteer');

// const url = process.argv[2];
// if (!url) {
//     throw "Please provide a URL as the first argument";
// }

// const url = "https://github.com"
const url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

async function run(url) {
  const browser = await puppeteer.launch({
    headless: false,
    slowMo: 250
  });
  const page = await browser.newPage();
  await page.setViewport({
    width: 1200,
    height: 800,
    deviceScaleFactor: 1
  })
  await page.goto(url);
  // await page.screenshot({path: 'screenshots/example.png'});
  await browser.close();
};

run(url);
