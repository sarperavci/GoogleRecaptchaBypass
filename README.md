# reCAPTCHA Bypass

This project provides a solution to automatically solve Google's reCAPTCHA using SeleniumBase. The solver handles both the initial checkbox challenge and the audio CAPTCHA challenge.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Credits](#credits)


## Features

- Automatically solves Google's reCAPTCHA challenges.
- Uses asynchronous downloading to speed up audio CAPTCHA processing.
- Converts audio files to text using Google Speech Recognition.
- Checks if the reCAPTCHA is solved with just a click before proceeding to the bypass technique.


## Installation

1. **Clone the Repository**

```
git clone https://github.com/desis123/GoogleRecaptchaBypass
cd RecaptchaBypass
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
from seleniumbase import SB
from RecaptchaSolver import RecaptchaSolver
import time

# Configure SeleniumBase with equivalent options
with SB(
    uc=True,                    # Undetected mode (helps with automation detection)
    incognito=True,             # Equivalent to --incognito
    xvfb=True,             # Set to False if you dont want xvfb or headed to True  to turn off headless 
    disable_csp=True,           # Additional protection against detection
    disable_ws=True,            # Disable web security
    chromium_arg="--disable-dev-shm-usage,--no-sandbox,--log-level=3,--no-proxy-server"
) as sb:
    
    # Navigate to the reCAPTCHA demo page
    sb.open("https://www.google.com/recaptcha/api2/demo")
    
    # Initialize the RecaptchaSolver
    recaptchaSolver = RecaptchaSolver(sb)
    
    try:
        # Perform CAPTCHA solving with timing
        t0 = time.time()
        recaptchaSolver.solveCaptcha()
        elapsed_time = time.time() - t0
        print(f"Time to solve the captcha: {elapsed_time:.2f} seconds")
        
        # Optional: Submit the form to verify it worked
        sb.click('#recaptcha-demo-submit')
        sb.sleep(2)
        
        # Check for success message
        if sb.is_text_visible("Verification Success"):
            print("✓ CAPTCHA verification successful!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

I have created `test.py` to demonstrate the usage of this script. You can run the `test.py` file to see the script in action.

    
    python test.py
    

## Code Structure

- `RecaptchaSolver.py`: Contains the `RecaptchaSolver` class with methods to solve the reCAPTCHA.
- `test.py`: Example usage of the `RecaptchaSolver` class.




## Credits

This project was inspired by and uses techniques from [sarperavci/GoogleRecaptchaBypass](https://github.com/sarperavci/GoogleRecaptchaBypass).
