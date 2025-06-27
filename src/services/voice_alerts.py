import pyttsx3

def play_voice_alert(text: str):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
