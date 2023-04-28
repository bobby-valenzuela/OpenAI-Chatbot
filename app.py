#!/usr/bin/env python3
import openai
from dotenv import dotenv_values

config = dotenv_values('.env');
openai.api_key = config["OPENAI_API_KEY"]

messages = []

while True:

    try:
        usr_input = input(str("You: "))
        message = { "role": "user", "content": usr_input }
        # Store our latest input into chat history
        messages.append(message)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        # Store reply into chat history
        messages.append(response.choices[0]["message"].to_dict())
        reply = response.choices[0].message.content

        print(f"Assistant: {reply}")

    except KeyboardInterrupt:
        print("Exiting...")
        break

