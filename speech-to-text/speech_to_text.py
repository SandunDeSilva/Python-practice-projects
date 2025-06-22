import pyttsx3
import speech_recognition as sr

def get():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        audio = recognizer.listen(source)
        print('done!')
    
    try:
        text = recognizer.recognize_google(audio)
        print('You said '+text)
    except Exception as e:
        print(e)

get()