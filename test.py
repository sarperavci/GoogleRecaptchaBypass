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

# Alternative: Using BaseCase class structure (for pytest integration)
from seleniumbase import BaseCase

class RecaptchaTest(BaseCase):
    def test_solve_captcha(self):
        # Set Chrome options
        self.open("https://www.google.com/recaptcha/api2/demo")
        
        # Initialize solver
        recaptchaSolver = RecaptchaSolver(self)
        
        try:
            t0 = time.time()
            recaptchaSolver.solveCaptcha()
            elapsed_time = time.time() - t0
            print(f"Time to solve the captcha: {elapsed_time:.2f} seconds")
            
            # Verify solution
            self.click('#recaptcha-demo-submit')
            self.sleep(2)
            self.assert_text("Verification Success")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            raise

# Run with: pytest test_recaptcha.py --uc --incognito -s