from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(prompt):
    """
    Generate a base response to an instruction using GPT-4.
    Replace GPT-4 with your own LLaMA model inference if needed.
    """
    system_msg = "You are a helpful, concise assistant that follows instructions carefully. Words are as valuable as gold."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()