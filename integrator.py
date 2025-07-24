import openai # type: ignore
from config import API_KEY

def call_openai_api(prompt):
    openai.api_key = API_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=256
    )
    return response.choices[0].text.strip()