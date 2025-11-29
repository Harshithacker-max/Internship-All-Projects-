# I am using the concept of speech recoganization which is teach by jibrran ali sir & i also use pywhat.kit and make a you tube speech recoganization when you speak any thing which you want to play on youtube 
#just run the code and simply said anthything which you want to play on youtube & it's play that video 
import speech_recognition as sr
import pyttsx3
speaker = pyttsx3.init()
speaker.say("")
speaker.runAndWait()


mic = sr.Recognizer()

with sr.Microphone() as source:
    print("Start Speaking ...")
    voice = mic.listen(source)
    
    text = mic.recognize_google(voice)  
    print("You Said this:", text)
