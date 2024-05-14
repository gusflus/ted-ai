import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("ready")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    with open("input.txt", "w") as file:
        file.write(text)
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print("Sorry, an error occurred. {0}".format(e))
