# Google Recaptcha Solver

**We love bots ❤️, but Google doesn't.** So, here is the solution to bypass Google reCAPTCHA.

Solve Google reCAPTCHA less than 5 seconds! 🚀

This is a Python script to solve Google reCAPTCHA using the DrissionPage library. *~~Selenium implementation will be added soon.~~*

## Recent Updates

Good news! Selenium implementation is added. Thanks to [@obaskly](https://github.com/obaskly) for the contribution. Check out the [selenium branch](https://github.com/sarperavci/GoogleRecaptchaBypass/tree/selenium) for more details.


### Easist way to bypass Google reCAPTCHA

Use [Capsolver](https://www.capsolver.com/?utm_source=github&utm_medium=ads&utm_campaign=scraping&utm_term=GoogleRecaptchaBypass) to bypass seamlessly Google reCAPTCHA v2 and v3.
Check [Capsolver-GoogleRecaptchaV2Bypass](https://github.com/sarperavci/Capsolver-GoogleRecaptchaV2Bypass) and [Capsolver-GoogleRecaptchaV3Bypass](https://github.com/sarperavci/Capsolver-GoogleRecaptchaV3Bypass)

Here is a simple example:

```python
from CapsolverRecaptchaV2Bypasser import CapsolverRecaptchaV2Bypasser
from selenium import webdriver

CAPSOLVER_API_KEY = "CAP-YOUR_API_KEY"
page_url = "https://google.com/recaptcha/api2/demo"
page_key = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-" # This can be found in the data-sitekey attribute of the reCaptcha element

page = webdriver.Chrome()
page.get( page_url )
recaptchaBypasser = CapsolverRecaptchaV2Bypasser(page, page_url, page_key, CAPSOLVER_API_KEY)
recaptchaBypasser.solve_recaptcha()
```

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
