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

[![](https://github.com/user-attachments/assets/783ce396-fa8c-4e10-846e-86d0ba0d0144)](https://www.scrapeless.com/en/product/scraping-browser?utm_medium=github&utm_campaign=sarperavci-cap)

If you’re looking for an automation browser tool designed to bypass website bot detection systems, I highly recommend the [**Scrapeless Scraping Browser**](https://www.scrapeless.com/en/product/scraping-browser?utm_medium=github&utm_campaign=sarperavci-cap). This cloud-based browser platform features advanced stealth technology and powerful anti-blocking capabilities, making it easy to handle dynamic websites, anti-bot mechanisms, and CAPTCHA challenges. With a built-in **free CAPTCHA solver**, it is perfectly suited for web scraping, automated testing, and data collection—especially in environments with complex anti-bot defenses.
  
**Key Features:**

* **Built-in Free CAPTCHA solver:** Instantly solves reCAPTCHA, Cloudflare Turnstile/Challenge, AWS WAF, DataDome, and more.  
* **High-concurrency scraping:** Run 50 to 1000+ browser instances per task within seconds, with no server resource limits.  
* **Human-like browsing environment:** Dynamic fingerprint spoofing and real user behavior simulation, powered by the Scrapeless Chromium engine for advanced stealth.  
* **Headless mode support:** Compatible with both headful and headless browsers, adapting to diverse anti-scraping strategies.  
* **70M+ residential IP proxies:** Global coverage with geolocation targeting and automatic IP rotation.  
* **Low operating costs:** Proxy usage costs only $1.26 to $1.80 per GB.  
* **Plug-and-play integration:** Fully compatible with Puppeteer, Playwright, Python, and Node.js for seamless setup.

[**Scrapeless**](https://www.scrapeless.com/en?utm_medium=github&utm_campaign=sarperavci-cap) is an all-in-one, enterprise-grade, and highly scalable data scraping solution built for developers and businesses. Beyond the Scraping Browser, it also offers a [**Scraping API**](https://www.scrapeless.com/en/product/scraping-api?utm_medium=github&utm_campaign=sarperavci-cap), [**Deep SerpAPI**](https://www.scrapeless.com/en/product/deep-serp-api?utm_medium=github&utm_campaign=sarperavci-cap), and robust [proxy services](https://www.scrapeless.com/en/product/proxies?utm_medium=github&utm_campaign=sarperavci-cap).
  
👉Learn more: [**Scrapeless Scraping Browser Playground**](https://app.scrapeless.com/passport/login?utm_medium=github&utm_campaign=sarperavci-cap) **| [Scrapeless Scraping Browser Documentation](https://docs.scrapeless.com/en/scraping-browser/quickstart/introduction/?utm_medium=github&utm_campaign=sarperavci-cap)**  


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
