import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something...")
    # Adjust for ambient noise levels
    recognizer.adjust_for_ambient_noise(source)
    # Listen for the user's speech
    audio = recognizer.listen(source)

try:
    print("Recognizing...")
    # Recognize speech using Google Speech Recognition
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print("Sorry, an error occurred. {0}".format(e))
