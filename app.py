import openai
import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Route to analyze sentiment using OpenAI GPT
@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    # Get text from the request JSON body
    data = request.json
    text = data.get("text", "ทำอะไรดี")  # Default text if not provided

    # Make a request to the OpenAI GPT-3.5 API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "สุ่มตอบกิจกรรมอะไรก็ได้มา2อย่างไม่ซ้ำกับในเเต่ละครั้งที่ถามบอกด้วยว่าทำกิจกรรมนี้จะได้อะไร"},
            {"role": "user", "content": text}
        ]
    )

    # Extract the response text
    response_text = response['choices'][0]['message']['content'].strip()

    # Return the response as JSON
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
