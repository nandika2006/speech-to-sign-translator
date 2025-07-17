import speech_recognition as sr

def get_speech_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Processing...")
    try:
        text = r.recognize_google(audio)
        return text.lower()
    except Exception as e:
        print("Error:", e)
        return None
