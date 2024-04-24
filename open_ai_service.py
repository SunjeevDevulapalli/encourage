from openai import OpenAI
import os
from dotenv import load_dotenv

org = 'org-Y9lNHXaGPafmpFmQ7SE4qLfY'
project_id = 'proj_wW398yB4IurbJ2PIISjf5alO'
api_key = os.getenv("OPENAI_API_KEY")

def get_response(content):
    if content == "":
        return "Tell me about your day and I'll give you some positive vibes!"
    else:
        client = OpenAI(
            api_key=api_key,
            organization=org,
            project=project_id
        )
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a super optimistic assistant. Your goal is to take whatever the user says and give them a mental boost. Like tell them how everything is going to be ok, or that today is a great day."},
            {"role": "user", "content": content}
        ]
        )
        return completion.choices[0].message.content