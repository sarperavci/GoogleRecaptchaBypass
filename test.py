from selenium import webdriver
from RecaptchaSolver import RecaptchaSolver
import time

# Initialize the WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--log-level=3")
options.add_argument('--no-proxy-server')
options.add_argument("--incognito")
options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/recaptcha/api2/demo")
recaptchaSolver = RecaptchaSolver(driver)

try:
    # Perform CAPTCHA solving
    t0 = time.time()
    recaptchaSolver.solveCaptcha()
    print(f"Time to solve the captcha: {time.time() - t0:.2f} seconds")

except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
