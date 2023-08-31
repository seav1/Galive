const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  
  // 延迟1分钟
  await new Promise(resolve => setTimeout(resolve, 60000));
  
  await browser.close();
})();
