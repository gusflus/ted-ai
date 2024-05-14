import os

import pygame
from gtts import gTTS
from pygame import mixer


def text_to_speech(text, filename):
    tts = gTTS(text=text, lang="en")
    tts.save(filename)


def play_audio(filename):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()


def main():
    text_file = "output.txt"
    audio_file = "output.mp3"

    # Read text from file
    with open(text_file, "r") as file:
        text = file.read()

    # Convert text to speech
    text_to_speech(text, audio_file)

    # Play the audio
    play_audio(audio_file)

    # Wait until audio finishes playing
    while pygame.mixer.music.get_busy():
        continue

    # Delete the audio file
    os.remove(audio_file)


if __name__ == "__main__":
    main()
