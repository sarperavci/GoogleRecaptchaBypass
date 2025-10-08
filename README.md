# reCAPTCHA Bypass

This project provides a solution to automatically solve Google's reCAPTCHA using playwright. The solver handles both the initial checkbox challenge and the audio CAPTCHA challenge.


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
git clone https://github.com/desis123/GoogleRecaptchaBypass.git
cd GoogleRecaptchaBypass
git checkout playwright-GoogleRecaptchaBypass
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
import asyncio
import time
from playwright.async_api import async_playwright
from RecaptchaSolver import RecaptchaSolver

async def main():
    async with async_playwright() as p:
        # Launch browser with options similar to Selenium
        browser = await p.chromium.launch(
            headless=False,  # Set to True for headless mode
            args=[
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--log-level=3',
                '--no-proxy-server',
            ]
        )
        
        # Create context with incognito mode
        context = await browser.new_context(
            # Incognito mode is default for new contexts
            viewport={'width': 1280, 'height': 720},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        
        # Create a new page
        page = await context.new_page()
        
        # Navigate to the reCAPTCHA demo page
        await page.goto("https://www.google.com/recaptcha/api2/demo")
        
        # Initialize the RecaptchaSolver
        recaptchaSolver = RecaptchaSolver(page)
        
        try:
            # Perform CAPTCHA solving with timing
            t0 = time.time()
            await recaptchaSolver.solveCaptcha()
            elapsed_time = time.time() - t0
            print(f"Time to solve the captcha: {elapsed_time:.2f} seconds")
            
            # Optional: Submit the form to verify it worked
            await page.click('#recaptcha-demo-submit')
            await asyncio.sleep(2)
            
            # Check for success message
            if await page.is_visible('text=Verification Success'):
                print("✓ CAPTCHA verification successful!")
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            await browser.close()

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
```

I have created `test.py` to demonstrate the usage of this script. You can run the `test.py` file to see the script in action.

    
    python test.py
    

## Code Structure

- `RecaptchaSolver.py`: Contains the `RecaptchaSolver` class with methods to solve the reCAPTCHA.
- `test.py`: Example usage of the `RecaptchaSolver` class.




## Credits

This project was inspired by and uses techniques from [sarperavci/GoogleRecaptchaBypass](https://github.com/sarperavci/GoogleRecaptchaBypass).
