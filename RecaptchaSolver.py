import os
import random
import asyncio
import aiohttp
import time
from pydub import AudioSegment
import speech_recognition as sr

class RecaptchaSolver:
    def __init__(self, page):
        self.page = page

    async def download_audio(self, url, path):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                with open(path, 'wb') as f:
                    f.write(await response.read())
        print("Downloaded audio asynchronously.")

    async def solveCaptcha(self):
        try:
            # Wait for the CAPTCHA iframe to be available
            recaptcha_frame = self.page.frame_locator('iframe[title*="reCAPTCHA"]')
            
            # Click on the CAPTCHA checkbox
            await recaptcha_frame.locator('#recaptcha-anchor').click()

            # Check if the CAPTCHA is solved
            await asyncio.sleep(1)  # Allow some time for the state to update
            if await self.isSolved():
                print("CAPTCHA solved by clicking.")
                return

            # If not solved, attempt audio CAPTCHA solving
            await self.solveAudioCaptcha()

        except Exception as e:
            print(f"An error occurred while solving CAPTCHA: {e}")
            raise

    async def solveAudioCaptcha(self):
        try:
            # Switch to the audio CAPTCHA iframe
            challenge_frame = self.page.frame_locator('iframe[title*="recaptcha challenge expires in two minutes"]')

            # Click on the audio button
            await challenge_frame.locator('#recaptcha-audio-button').click()

            # Wait for audio source to be available
            await asyncio.sleep(1)
            
            # Get the audio source URL
            audio_source = await challenge_frame.locator('#audio-source').get_attribute('src')
            print(f"Audio source URL: {audio_source}")
            
            # Download the audio to the temp folder asynchronously
            temp_dir = os.getenv("TEMP") if os.name == "nt" else "/tmp/"
            path_to_mp3 = os.path.normpath(os.path.join(temp_dir, f"{random.randrange(1, 1000)}.mp3"))
            path_to_wav = os.path.normpath(os.path.join(temp_dir, f"{random.randrange(1, 1000)}.wav"))
            
            await self.download_audio(audio_source, path_to_mp3)

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
            await challenge_frame.locator('#audio-response').fill(captcha_text)
            await challenge_frame.locator('#audio-response').press('Enter')
            print("Entered and submitted CAPTCHA text.")

            # Wait for CAPTCHA to be processed
            await asyncio.sleep(0.8)

            # Verify CAPTCHA is solved
            if await self.isSolved():
                print("Audio CAPTCHA solved.")
            else:
                print("Failed to solve audio CAPTCHA.")
                raise Exception("Failed to solve CAPTCHA")

        except Exception as e:
            print(f"An error occurred while solving audio CAPTCHA: {e}")
            raise

    async def isSolved(self):
        try:
            # Access the reCAPTCHA iframe
            recaptcha_frame = self.page.frame_locator('iframe[title*="reCAPTCHA"]')
            
            # Get the checkbox element
            checkbox = recaptcha_frame.locator('#recaptcha-anchor')
            
            # Check the aria-checked attribute
            aria_checked = await checkbox.get_attribute('aria-checked')
            checkbox_class = await checkbox.get_attribute('class')

            # Return True if the aria-checked attribute is "true" or the checkbox has the 'recaptcha-checkbox-checked' class
            return aria_checked == "true" or 'recaptcha-checkbox-checked' in (checkbox_class or '')

        except Exception as e:
            print(f"An error occurred while checking if CAPTCHA is solved: {e}")
            return False