#!/usr/bin/env python3
import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values('.env');
openai.api_key = config["OPENAI_API_KEY"]

def main():

    parser = argparse.ArgumentParser(description="Simple command line chabot with GPT-3.5")
    parser.add_argument("--personality",type=str,default="Friendly and helpful chatbot",help="A brief summary of the chatbot's personality",required=False)

    args = parser.parse_args()
    personality = args.personality

    initial_prompt = f"You are a conversational chatbot. Your personality is: {personality}"
    messages = [{"role":"system","content":initial_prompt }]

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


if __name__ == "__main__":
    main()
