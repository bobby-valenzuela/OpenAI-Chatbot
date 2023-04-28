import openai
from dotenv import dotenv_values

config = dotenv_values('.env');
openai.api_key = config["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        { "role": "user", "content": "tell me a joke" }
    ]
)

result = response.choices[0].message.content

print(result)
