""" Audio Recognition """
""" Use english audio for better results """

import speech_recognition as sr
Audio_File=("poni_poni.wav")

#initialise the recogniser
r=sr.Recognizer()

with sr.AudioFile(Audio_File) as source:
    audio=r.record(source)
    
try:
    print("audio file contains---------\n"+r.recognize_google(audio))
except sr.UnknownValueError :
    print("Google speech recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results from google speech recognition")