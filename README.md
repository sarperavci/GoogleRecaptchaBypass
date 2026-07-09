# Google Recaptcha Solver

**We love bots ❤️, but Google doesn't.** So, here is the solution to bypass Google reCAPTCHA.

Solve Google reCAPTCHA less than 5 seconds! 🚀

This is a Python script to solve Google reCAPTCHA using the DrissionPage library. *~~Selenium implementation will be added soon.~~*

## Recent Updates

Good news! Selenium implementation is added. Thanks to [@obaskly](https://github.com/obaskly) for the contribution. Check out the [selenium branch](https://github.com/sarperavci/GoogleRecaptchaBypass/tree/selenium) for more details.

## Sponsors

### IPcook

[<img src="https://github.com/user-attachments/assets/ea0a4dd8-f26a-4598-8307-868e190150a9" alt="IPcook"/>](https://www.ipcook.com/?ref=00JF84&utm_source=github&utm_medium=referral&utm_campaign=sarperavci)

**Need Reliable Proxies? [IPcook](https://www.ipcook.com/?ref=00JF84&utm_source=github&utm_medium=referral&utm_campaign=sarperavci) Has Got You Covered**

* 🚀 99.99% Uptime
* ⚡ Avg. Response Time < 0.5s
* 🔒 Up to 10 Sub-accounts
* 🌍 24/7 Premium Support
* ⏰ Sticky Sessions up to 24h
* 📍 Free Geo-Targeting
* ♾️ Unlimited Bandwidth

🎁 [**Start with a FREE 100MB Trial**](https://www.ipcook.com/?ref=00JF84&utm_source=github&utm_medium=referral&utm_campaign=sarperavci)

💸 Use code **WELCOME20** for 20% OFF

### RapidProxy

[<img width="1680" height="1060" alt="RapidProxy" src="https://github.com/user-attachments/assets/6d3819b8-7065-4bd4-bda7-b06e0fe04477"/>](https://www.rapidproxy.io/?ref=sarperavci)

[**RapidProxy**](https://www.rapidproxy.io/?ref=sarperavci) – Power Your Data with Premium Proxies

🎁 Try proxies [**for free**](https://www.rapidproxy.io/?ref=sarperavci) + Use code **RAPID10** for 10% OFF

**Why Choose RapidProxy?**

* 90M+ IPs in 200+ countries & regions  
* No expiration on traffic — use anytime, no pressure  
* Unlimited concurrency for maximum performance  
* Starting from just $0.65/GB — built for scale  
* City-level targeting for precise geo access  
* Flexible session control tailored to your needs  
* Enterprise-grade speed & reliability  
* Built for large-scale automation  

**💡 Built for Growth**

Whether you're scaling scraping operations, running automation, or accessing global content, RapidProxy delivers the speed, stability, and flexibility you need to grow without limits.

👉 Start your free trial today: [https://www.rapidproxy.io/?ref=sarperavci](https://www.rapidproxy.io/?ref=sarperavci)

---
<!-- /AD -->

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
