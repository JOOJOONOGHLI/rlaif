from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def score_response(prompt, og_response, perturbed_response):
    system_msg = "You are evaluating the helpfulness, accuracy, and clarity of perturbations to a response. The original response is meant to be centered at 0, as a baseline. The score will be between -1 (bad) and 1 (good). The worse the perturbation is compared to the original, the lower the score. The better it is, the higher the score."
    user_msg = f"""
Prompt: {prompt}

Original Response:
{og_response}

Perturbation: {perturbed_response}

Score this response from -1 to 1 based on how well it answers the question or follows the instructions of the prompt. Remember, the original response is always assigned a score of 0 as a baseline.
Respond only with the number, no additional text.
"""
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ]
    )
    return float(completion.choices[0].message.content.strip())
