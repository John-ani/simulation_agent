from openai import OpenAI
from config import API_KEY

# Initialize OpenAI client
client = OpenAI(api_key=API_KEY)

def call_openai_api(prompt):
    # Call OpenAI API using the client
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract and return the content of the response
    return response.choices[0].message['content'].strip()