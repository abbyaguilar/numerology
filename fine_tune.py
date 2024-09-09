import openai
import requests
import json

openai.api_key = ''

endpoint = 'https://api.openai.com/v1/fine_tuning/jobs'
data = {
    "training_file": "file-fVXxjUkhWfl3wqW2lwnyZ6Gh",
    "model": "gpt-3.5-turbo"
}

response = requests.post(
    endpoint,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    },
    data=json.dumps(data)
)

print(response.json())
