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
    sentence to reduce or improve helpfulness, accuracy, or clarity. You need to make specific changes
    as to the quality of the response changes, not just the diction alone (i.e potentially bring up information that
    is unrelated, or that which is more specific and/or helpful.)
    You choose which one.

    Original Sentence:"{sentence}"

    Perturb it slightly so it becomes less or more helpful, or more or less vauge or misleading:
    """

    completion = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content.strip()