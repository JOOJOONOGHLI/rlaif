from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def score_response(prompt, response):
    system_msg = "You are evaluating the helpfulness, accuracy, and clarity of the response on a scale from -1 (very poor) to 1 (very helpful)."
    user_msg = f"""
Prompt: {prompt}

Response:
{response}

Score this response from -1 to 1 based on how well it follows the instruction.
Respond only with the number.
"""
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ]
    )
    return float(completion.choices[0].message.content.strip())
