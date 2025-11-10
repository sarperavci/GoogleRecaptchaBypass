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


# Alternative: Synchronous Playwright (simpler, no async/await)
from playwright.sync_api import sync_playwright

def main_sync():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--log-level=3',
                '--no-proxy-server',
            ]
        )
        
        context = browser.new_context(
            viewport={'width': 1280, 'height': 720}
        )
        
        page = context.new_page()
        page.goto("https://www.google.com/recaptcha/api2/demo")
        
        # Note: For sync version, you need a sync version of RecaptchaSolver
        # The current RecaptchaSolver uses async, so use the async version above
        
        browser.close()

# For pytest integration
import pytest
from playwright.sync_api import Page

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_solve_captcha(page: Page):
    page.goto("https://www.google.com/recaptcha/api2/demo")
    
    # Note: This requires converting RecaptchaSolver to sync version
    # or using pytest-playwright's async support
    
# Run with: pytest test_recaptcha.py --headed --browser chromium