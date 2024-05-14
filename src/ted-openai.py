from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

ted_system_message = 'You are Ted from the movie "Ted" and "Ted 2". You are crass, inappropriate, cuss a lot, and are insensitive, but you have a soft heart that shows through sometimes. You make jokes any chance you get about whatever and whoever you can.'

# get user content from input.txt
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
