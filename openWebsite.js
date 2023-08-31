const puppeteer = require('puppeteer');
const browser = await puppeteer.launch({ headless: true });

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  // 打开指定的网站
  await page.goto('https://ide-run.goorm.io/workspace/d9Sssb0cUEnisCoRCgX?token=d04702b4519674ab9a512f72b1bae53d&guestname=12');

  // 等待1分钟
  await page.waitForTimeout(60000);

  // 关闭浏览器
  await browser.close();
})();
