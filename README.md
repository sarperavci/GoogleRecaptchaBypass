# Google Recaptcha Solver

**We love bots ❤️, but Google doesn't.** So, here is the solution to bypass Google reCAPTCHA.

Solve Google reCAPTCHA less than 5 seconds! 🚀

This is a Python script to solve Google reCAPTCHA using the DrissionPage library. *~~Selenium implementation will be added soon.~~*

## Recent Updates

Good news! Selenium implementation is added. Thanks to [@obaskly](https://github.com/obaskly) for the contribution. Check out the [selenium branch](https://github.com/sarperavci/GoogleRecaptchaBypass/tree/selenium) for more details.

# Sponsor

### [Capsolver](https://www.capsolver.com/?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass)

[![Capsolver](docs/capsolver.jpg)](https://www.capsolver.com/?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass)
[Capsolver.com](https://www.capsolver.com/?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass) is an AI-powered service that specializes in solving various types of captchas automatically. It supports captchas such as [reCAPTCHA V2](https://docs.capsolver.com/guide/captcha/ReCaptchaV2.html?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass), [reCAPTCHA V3](https://docs.capsolver.com/guide/captcha/ReCaptchaV3.html?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass), [hCaptcha](https://docs.capsolver.com/guide/captcha/HCaptcha.html?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass), [FunCaptcha](https://docs.capsolver.com/guide/captcha/FunCaptcha.html?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass), [DataDome](https://docs.capsolver.com/guide/captcha/DataDome.html?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass), [AWS Captcha](https://docs.capsolver.com/guide/captcha/awsWaf.html?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass), [Geetest](https://docs.capsolver.com/guide/captcha/Geetest.html?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass), and Cloudflare [Captcha](https://docs.capsolver.com/guide/antibots/cloudflare_turnstile.html?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass) / [Challenge 5s](https://docs.capsolver.com/guide/antibots/cloudflare_challenge.html?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass), [Imperva / Incapsula](https://docs.capsolver.com/guide/antibots/imperva.html?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass), among others.

For developers, Capsolver offers API integration options detailed in their [documentation](https://docs.capsolver.com/?utm_source=github&utm_medium=banner_github&utm_campaign=GoogleRecaptchaBypass), facilitating the integration of captcha solving into applications. They also provide browser extensions for [Chrome](https://chromewebstore.google.com/detail/captcha-solver-auto-captc/pgojnojmmhpofjgdmaebadhbocahppod) and [Firefox](https://addons.mozilla.org/es/firefox/addon/capsolver-captcha-solver/), making it easy to use their service directly within a browser. Different pricing packages are available to accommodate varying needs, ensuring flexibility for users.



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
