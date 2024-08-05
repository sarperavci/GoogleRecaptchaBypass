import os
import random
import asyncio
import aiohttp
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pydub import AudioSegment
import speech_recognition as sr

class RecaptchaSolver:
    def __init__(self, driver):
        self.driver = driver

    async def download_audio(self, url, path):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                with open(path, 'wb') as f:
                    f.write(await response.read())
        print("Downloaded audio asynchronously.")

    def solveCaptcha(self):
        try:
            # Switch to the CAPTCHA iframe
            iframe_inner = WebDriverWait(self.driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]"))
            )
            
            # Click on the CAPTCHA box
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'recaptcha-anchor'))
            ).click()

            # Check if the CAPTCHA is solved
            time.sleep(1)  # Allow some time for the state to update
            
            if self.isSolved():
                print("CAPTCHA solved by clicking.")
                self.driver.switch_to.default_content()  # Switch back to main content
                return

            # If not solved, attempt audio CAPTCHA solving
            self.solveAudioCaptcha()

        except Exception as e:
            print(f"An error occurred while solving CAPTCHA: {e}")
            self.driver.switch_to.default_content()  # Ensure we switch back in case of error
            raise

    def solveAudioCaptcha(self):
        try:
            self.driver.switch_to.default_content()
            
            # Switch to the audio CAPTCHA iframe
            iframe_audio = WebDriverWait(self.driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]'))
            )

            # Click on the audio button
            audio_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'recaptcha-audio-button'))
            )
            audio_button.click()

            # Get the audio source URL
            audio_source = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'audio-source'))
            ).get_attribute('src')
            print(f"Audio source URL: {audio_source}")
            
            # Download the audio to the temp folder asynchronously
            temp_dir = os.getenv("TEMP") if os.name == "nt" else "/tmp/"
            path_to_mp3 = os.path.normpath(os.path.join(temp_dir, f"{random.randrange(1, 1000)}.mp3"))
            path_to_wav = os.path.normpath(os.path.join(temp_dir, f"{random.randrange(1, 1000)}.wav"))
            
            asyncio.run(self.download_audio(audio_source, path_to_mp3))

            # Convert mp3 to wav
            sound = AudioSegment.from_mp3(path_to_mp3)
            sound.export(path_to_wav, format="wav")
            print("Converted MP3 to WAV.")

            # Recognize the audio
            recognizer = sr.Recognizer()
            with sr.AudioFile(path_to_wav) as source:
                audio = recognizer.record(source)
            captcha_text = recognizer.recognize_google(audio).lower()
            print(f"Recognized CAPTCHA text: {captcha_text}")

            # Enter the CAPTCHA text
            audio_response = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'audio-response'))
            )
            audio_response.send_keys(captcha_text)
            audio_response.send_keys(Keys.ENTER)
            print("Entered and submitted CAPTCHA text.")

            # Wait for CAPTCHA to be processed
            time.sleep(0.8)  # Increase this if necessary

            # Verify CAPTCHA is solved
            if self.isSolved():
                print("Audio CAPTCHA solved.")
            else:
                print("Failed to solve audio CAPTCHA.")
                raise Exception("Failed to solve CAPTCHA")

        except Exception as e:
            print(f"An error occurred while solving audio CAPTCHA: {e}")
            self.driver.switch_to.default_content()  # Ensure we switch back in case of error
            raise

        finally:
            # Always switch back to the main content
            self.driver.switch_to.default_content()

    def isSolved(self):
        try:
            # Switch back to the default content
            self.driver.switch_to.default_content()

            # Switch to the reCAPTCHA iframe
            iframe_check = self.driver.find_element(By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]")
            self.driver.switch_to.frame(iframe_check)

            # Find the checkbox element and check its aria-checked attribute
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'recaptcha-anchor'))
            )
            aria_checked = checkbox.get_attribute("aria-checked")

            # Return True if the aria-checked attribute is "true" or the checkbox has the 'recaptcha-checkbox-checked' class
            return aria_checked == "true" or 'recaptcha-checkbox-checked' in checkbox.get_attribute("class")

        except Exception as e:
            print(f"An error occurred while checking if CAPTCHA is solved: {e}")
            return False
