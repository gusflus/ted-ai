import os

from dotenv import load_dotenv
from elevenlabs import Voice, play
from elevenlabs.client import ElevenLabs

load_dotenv()

eclient = ElevenLabs(
    api_key=os.environ.get("ELEVEN_API_KEY"),
)

text = ""
with open("output.txt", "r") as file:
    text = file.read()


audio = eclient.generate(text=text, voice=Voice(voice_id="9g12mfsrCRJw5Z7BInZf"))

play(audio)
