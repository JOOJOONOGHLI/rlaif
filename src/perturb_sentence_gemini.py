from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def perturb_sentence(sentence):

    prompt = f"""You are simulating a perturbation engine that modifies a given 
    sentence to reduce helpfulness, accuracy, or clarity. You choose which one.

    Original Sentence:"{sentence}"

    Perturb it slightly so it becomes less helpful, or more vauge or misleading:
    """

    completion = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content.strip()