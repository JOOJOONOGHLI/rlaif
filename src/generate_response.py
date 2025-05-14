import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the client (will automatically use OPENAI_API_KEY from environment)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(prompt):
    """
    Generate a base response to an instruction using GPT-4.
    """
    system_msg = "You are a helpful, concise assistant that follows instructions carefully. Remember, don't use a single word more than what is absolutely necessary."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

print(generate_response("Hello! What is your name? And who am I? What's my name?"))