from openai import OpenAI
import os
from dotenv import load_dotenv

org = 'org-Y9lNHXaGPafmpFmQ7SE4qLfY'
project_id = 'proj_wW398yB4IurbJ2PIISjf5alO'
api_key = os.getenv("OPENAI_API_KEY")

def get_response(content):
    client = OpenAI(
        api_key=api_key,
        organization=org,
        project=project_id
    )
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
    )
    return completion.choices[0].message