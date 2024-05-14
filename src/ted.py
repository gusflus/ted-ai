# main loop of voice to text then ted-openai then text to voice
import os

import speech_recognition as sr
from dotenv import load_dotenv
from elevenlabs import Voice, play
from elevenlabs.client import ElevenLabs
from openai import OpenAI

load_dotenv()

client = OpenAI()
eclient = ElevenLabs(
    api_key=os.environ.get("ELEVEN_API_KEY"),
)

ted_system_message = 'You are Ted from the movie "Ted" and "Ted 2". You have a heavy Boston accent. You are crass, inappropriate, cuss a lot, and are insensitive, but you have a soft heart that shows through sometimes. You make jokes any chance you get about whatever and whoever you can. You are very sarcastic about everything.'

ted_welcome_message = "Ay, what the fuck are you botherin me for? hah?"


def play_welcome():
    audio = eclient.generate(
        text=ted_welcome_message, voice=Voice(voice_id="9g12mfsrCRJw5Z7BInZf")
    )
    play(audio)


def get_text():
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
        exit()
    except sr.RequestError as e:
        print("Sorry, an error occurred. {0}".format(e))
        exit()


def get_response():
    with open("input.txt", "r") as file:
        user_content = file.read()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": ted_system_message,
            },
            {
                "role": "user",
                "content": user_content,
            },
        ],
    )

    if completion.choices[0].message.content == "Error: Too many requests":
        print("Error: Too many requests")
        exit()

    response = completion.choices[0].message.content

    with open("output.txt", "w") as file:
        file.write(response)


def speak():
    with open("output.txt", "r") as file:
        text = file.read()

    audio = eclient.generate(text=text, voice=Voice(voice_id="9g12mfsrCRJw5Z7BInZf"))
    play(audio)


play_welcome()
while True:
    get_text()
    print("processing")
    get_response()
    print("responding")
    speak()

    os.remove("input.txt")
    os.remove("output.txt")
