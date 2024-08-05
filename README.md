# reCAPTCHA Bypass

This project provides a solution to automatically solve Google's reCAPTCHA using Selenium WebDriver. The solver handles both the initial checkbox challenge and the audio CAPTCHA challenge.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Demo](#demo)
- [Credits](#credits)


## Features

- Automatically solves Google's reCAPTCHA challenges.
- Handles the initial checkbox as well as the audio CAPTCHA.
- Uses asynchronous downloading to speed up audio CAPTCHA processing.
- Converts audio files to text using Google Speech Recognition.


## Installation

1. **Clone the Repository**

```
git clone https://github.com/obaskly/reCAPTCHA-Bypass.git
cd reCAPTCHA-Bypass
```

2. **Install Dependencies**

```
pip install -r requirements.txt
```

3. **Install FFmpeg**

- Linux:

  ```
  sudo apt-get update
  sudo apt-get install ffmpeg
  ```
  
- Windows:

  Follow this tutorial: https://www.wikihow.com/Install-FFmpeg-on-Windows

## Usage

To implement this script in your project, you can follow a similar approach as shown below:

```python
from selenium import webdriver
from RecaptchaSolver import RecaptchaSolver

# Initialize the WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/recaptcha/api2/demo")
recaptchaSolver = RecaptchaSolver(driver)

try:
    # Perform CAPTCHA solving
    recaptchaSolver.solveCaptcha()

except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()
```

I have created `test.py` to demonstrate the usage of this script. You can run the `test.py` file to see the script in action.

    
    python test.py
    

## Code Structure

- `RecaptchaSolver.py`: Contains the `RecaptchaSolver` class with methods to solve the reCAPTCHA.
- `test.py`: Example usage of the `RecaptchaSolver` class.


## Demo

https://github.com/user-attachments/assets/1646aae0-984d-4e81-8b62-89b21a4ad4cf


## Credits

This project was inspired by and uses techniques from [sarperavci/GoogleRecaptchaBypass](https://github.com/sarperavci/GoogleRecaptchaBypass).
