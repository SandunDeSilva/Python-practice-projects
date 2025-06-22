import pyttsx3

engine = pyttsx3.init()
engine.say("Hello World!")
engine.runAndWait()

# We can further enhance this by getting the input from the user
text = input("Enter the text you want to convert to speech:\n ")

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

text_to_speech(text)