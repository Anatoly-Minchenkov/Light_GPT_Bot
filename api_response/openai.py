import openai

from os import getenv


def get_response(message):
    openai.api_key = getenv('OPENAI_KEY')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.8,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    return response
