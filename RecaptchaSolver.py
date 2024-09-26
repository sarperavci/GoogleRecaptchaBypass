import os,urllib,random,pydub,speech_recognition,time
from DrissionPage.common import Keys
from DrissionPage import ChromiumPage 

class RecaptchaSolver:
    def __init__(self, driver:ChromiumPage):
        self.driver = driver
    
    def solveCaptcha(self):
        iframe_inner = self.driver("@title=reCAPTCHA")
        time.sleep(0.1)
        
        # Click on the recaptcha
        iframe_inner('.rc-anchor-content',timeout=1).click()
        self.driver.wait.ele_displayed("xpath://iframe[contains(@title, 'reCAPTCHA')]",timeout=3)

        # Sometimes just clicking on the recaptcha is enough to solve it
        if self.isSolved():
            return
        
        # Get the new iframe //reCAPTCHA sorusunun süresi iki dakika sonra dolacak
        iframe = self.driver("xpath://iframe[contains(@title, 'recaptcha challenge expires in two minutes')]")

        # Click on the audio button
        iframe('#recaptcha-audio-button',timeout=1).click()
        time.sleep(.3)
        
        # Get the audio source
        src = iframe('#audio-source').attrs['src']
        
        # Download the audio to the temp folder
        path_to_mp3 = os.path.normpath(os.path.join((os.getenv("TEMP") if os.name=="nt" else "/tmp/")+ str(random.randrange(1,1000))+".mp3"))
        path_to_wav = os.path.normpath(os.path.join((os.getenv("TEMP") if os.name=="nt" else "/tmp/")+ str(random.randrange(1,1000))+".wav"))
        
        urllib.request.urlretrieve(src, path_to_mp3)

        # Convert mp3 to wav
        sound = pydub.AudioSegment.from_mp3(path_to_mp3)
        sound.export(path_to_wav, format="wav")
        sample_audio = speech_recognition.AudioFile(path_to_wav)
        r = speech_recognition.Recognizer()
        with sample_audio as source:
            audio = r.record(source)
        
        # Recognize the audio
        key = r.recognize_google(audio)
        
        # Input the key
        iframe('#audio-response').input(key.lower())
        time.sleep(0.1)
        
        # Submit the key
        iframe('#audio-response').input(Keys.ENTER)
        time.sleep(.4)

        # Check if the captcha is solved
        if self.isSolved():
            return
        else:
            raise Exception("Failed to solve the captcha")

    def isSolved(self):
        try:
            return "style" in self.driver.ele(".recaptcha-checkbox-checkmark",timeout=1).attrs
        except:
            return False
