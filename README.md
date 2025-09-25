# Google Recaptcha Solver

**We love bots ❤️, but Google doesn't.** So, here is the solution to bypass Google reCAPTCHA.

Solve Google reCAPTCHA less than 5 seconds! 🚀

This is a Python script to solve Google reCAPTCHA using the DrissionPage library. *~~Selenium implementation will be added soon.~~*

## Recent Updates

Good news! Selenium implementation is added. Thanks to [@obaskly](https://github.com/obaskly) for the contribution. Check out the [selenium branch](https://github.com/sarperavci/GoogleRecaptchaBypass/tree/selenium) for more details.

## Sponsors

### Nstproxy

[<img width="1280" height="800" alt="1756709054016" src="https://github.com/user-attachments/assets/9242659a-0314-4dc7-862f-5fa2c9a3fc80"/>](https://www.nstproxy.com/?type=flow&utm_source=sarperavci)

If you're looking for a reliable proxy to **bypass anti-bot systems, scrape at scale, and access geo-restricted data without blocks**, Nstproxy is built for you. Perfect for large-scale web scraping, SEO monitoring, e-commerce data collection, price intelligence, and automation — even under the strictest anti-scraping protections.

Nstproxy offers a global pool of residential, datacenter, and IPv6 proxies with rotating or sticky sessions, advanced anti-block tech, and pricing from $0.1/GB for maximum uptime and ROI.

**Key Features:**

* 🌍 **Global IP Coverage** – 110M+ residential IPs, 195+ countries, IPv4/IPv6  
* 🔄 **Rotation Control** – Per request or sticky sessions for consistent sessions  
* 🛡 **Anti-ban & CAPTCHA Bypass** – Designed for high scraping success rates  
* 💰 **Affordable** – From $0.1/GB, far below market average  
* ⚡ **Multi-purpose** – Scraping, SEO, automation, e-commerce, analytics  
* 🔌 **Easy Integration** – Python, Puppeteer, Playwright, Node.js
* 📈 **Unlimited Scaling** – Handle any volume with stable performance

An all-in-one proxy solution for developers and traders who need reliability, scalability, and cost efficiency.  
 👉 Learn more: [Nstproxy.com](https://www.nstproxy.com/?type=flow&utm_source=sarperavci): [https://www.nstproxy.com/?type=flow\&utm\_source=sarperavci](https://www.nstproxy.com/?type=flow&utm_source=sarperavci)  | [Dashboard](https://app.nstproxy.com/?utm_source=sarperavci)    

Telegram:[https://t.me/nstproxy](https://t.me/nstproxy)

Discord: [https://discord.gg/5jjWCAmvng](https://discord.gg/5jjWCAmvng)   

Use code: **RECAPTCHA get 10% OFF**

### Scrapeless

[![](https://github.com/user-attachments/assets/783ce396-fa8c-4e10-846e-86d0ba0d0144)](https://www.scrapeless.com/en/product/scraping-browser?utm_source=github&utm_campaign=sarperavci)

[**Scrapeless Browser**](https://www.scrapeless.com/en/product/scraping-browser?utm_source=github&utm_campaign=sarperavci) is a cloud-based, Chromium-powered headless browser cluster. It allows developers to run large-scale, low-cost concurrent browser instances and reliably handle complex interactions on protected pages. Ideal for AI infrastructure, web automation, data scraping, page rendering, automated testing, and other tasks that require a real browser environment.  
**Key Advantages of Scrapeless Browser:**

* **Built-in CAPTCHA solving:** Automatically bypasses Cloudflare Turnstile, reCAPTCHA, AWS WAF, DataDome, and other challenge systems.  
* **Undetectable browser environment:** Not based on the traditional WebDriver — avoids automation detection.  
* **Massive concurrency support:** Run 50–10,000+ browser instances simultaneously with no server constraints.  
* **Real-time debugging:** Live View and session recording for efficient troubleshooting.  
* **Native integration:** Compatible with Puppeteer, Playwright, Python, and Node.js — easy to integrate into your current workflows.  
* **70M+ residential IPs:** Global proxy network with automatic rotation and smart geolocation routing.

In terms of cost, Scrapeless browser usage is only 1/8 of Browserbase, significantly cutting overall expenses.  
It also offers a [**Scraping API**](https://www.scrapeless.com/en/product/scraping-api?utm_source=github&utm_campaign=sarperavci)**、[Deep SerpApi](https://www.scrapeless.com/en/product/deep-serp-api?utm_source=github&utm_campaign=sarperavci) and [Proxies](https://www.scrapeless.com/en/product/proxies?utm_source=github&utm_campaign=sarperavci) services**.  
👉 Learn more: [Scrapeless Browser](https://www.scrapeless.com/en/product/scraping-browser?utm_source=github&utm_campaign=sarperavci) | [Documentation](https://docs.scrapeless.com/en/scraping-browser/quickstart/introduction/?utm_source=github&utm_campaign=sarperavci)  


## Installation
Three dependencies are required to run this script. You can install them using the following command:
```bash
pip install -r requirements.txt
```

Also, you need to install ffmpeg. You can download it from [here](https://ffmpeg.org/download.html).

```bash
sudo apt-get install ffmpeg
```

## Usage

To implement this script in your project, you can follow a similar approach as shown below:

```python
from DrissionPage import ChromiumPage 
from RecaptchaSolver import RecaptchaSolver
driver = ChromiumPage()
recaptchaSolver = RecaptchaSolver(driver)
driver.get("https://www.google.com/recaptcha/api2/demo")
recaptchaSolver.solveCaptcha()
```

I have created `test.py` to demonstrate the usage of this script. You can run the `test.py` file to see the script in action.


## Demo

![Demo](docs/demo.gif)

 
## How does it work?

We automate the browser to solve the reCAPTCHA. Instead of image captcha, we are solving the audio captcha. The audio captcha is easier to solve programmatically.

**One warning:** Google may block your IP if you solve too many captchas in a short period of time. So, use this script wisely or change your IP frequently.

## Star History

<a href="https://star-history.com/#sarperavci/GoogleRecaptchaBypass&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=sarperavci/GoogleRecaptchaBypass&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=sarperavci/GoogleRecaptchaBypass&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=sarperavci/GoogleRecaptchaBypass&type=Date" />
 </picture>
</a>
