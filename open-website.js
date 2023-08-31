const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://ide-run.goorm.io/workspace/d9Sssb0cUEnisCoRCgX?token=d04702b4519674ab9a512f72b1bae53d&guestname=12');
  
  // 延迟1分钟
  await new Promise(resolve => setTimeout(resolve, 60000));
  
  await browser.close();
})();
