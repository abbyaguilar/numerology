from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

openai.api_key = os.getenv("")

@app.route('/get_prompt', methods=['POST'])
def get_prompt():
    data = request.json
    month = data.get('month')
    day = data.get('day')
    year = data.get('year')

    prompt = f"Generate a numerology prompt based on the date: {month} {day}, {year}"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )

    generated_prompt = response.choices[0].text.strip()
    return jsonify({"prompt": generated_prompt})
