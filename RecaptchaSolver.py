import os
import random
import asyncio
import aiohttp
import time
from pydub import AudioSegment
import speech_recognition as sr

class RecaptchaSolver:
    def __init__(self, sb):
        self.sb = sb

    async def download_audio(self, url, path):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                with open(path, 'wb') as f:
                    f.write(await response.read())
        print("Downloaded audio asynchronously.")

    def solveCaptcha(self):
        try:
            # Switch to the CAPTCHA iframe
            self.sb.switch_to_frame('iframe[title*="reCAPTCHA"]')
            
            # Click on the CAPTCHA box
            self.sb.click('#recaptcha-anchor')

            # Check if the CAPTCHA is solved
            time.sleep(1)  # Allow some time for the state to update
            if self.isSolved():
                print("CAPTCHA solved by clicking.")
                self.sb.switch_to_default_content()
                return

            # If not solved, attempt audio CAPTCHA solving
            self.solveAudioCaptcha()

        except Exception as e:
            print(f"An error occurred while solving CAPTCHA: {e}")
            self.sb.switch_to_default_content()
            raise

    def solveAudioCaptcha(self):
        try:
            self.sb.switch_to_default_content()
            
            # Switch to the audio CAPTCHA iframe
            self.sb.switch_to_frame('iframe[title*="recaptcha challenge expires in two minutes"]')

            # Click on the audio button
            self.sb.click('#recaptcha-audio-button')

            # Get the audio source URL
            audio_source = self.sb.get_attribute('#audio-source', 'src')
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
            self.sb.type('#audio-response', captcha_text)
            self.sb.press_keys('#audio-response', '\n')
            print("Entered and submitted CAPTCHA text.")

            # Wait for CAPTCHA to be processed
            time.sleep(0.8)

            # Verify CAPTCHA is solved
            if self.isSolved():
                print("Audio CAPTCHA solved.")
            else:
                print("Failed to solve audio CAPTCHA.")
                raise Exception("Failed to solve CAPTCHA")

        except Exception as e:
            print(f"An error occurred while solving audio CAPTCHA: {e}")
            self.sb.switch_to_default_content()
            raise

        finally:
            # Always switch back to the main content
            self.sb.switch_to_default_content()

    def isSolved(self):
        try:
            # Switch back to the default content
            self.sb.switch_to_default_content()

            # Switch to the reCAPTCHA iframe
            self.sb.switch_to_frame('iframe[title*="reCAPTCHA"]')

            # Check if the checkbox is checked
            aria_checked = self.sb.get_attribute('#recaptcha-anchor', 'aria-checked')
            checkbox_class = self.sb.get_attribute('#recaptcha-anchor', 'class')

            # Return True if the aria-checked attribute is "true" or the checkbox has the 'recaptcha-checkbox-checked' class
            return aria_checked == "true" or 'recaptcha-checkbox-checked' in checkbox_class

        except Exception as e:
            print(f"An error occurred while checking if CAPTCHA is solved: {e}")
            return False