from openai import OpenAI
client = OpenAI()

def perturb_sentence(sentence):

    prompt = f"""You are simulating a perturbation engine that modifies a given 
    sentence to reduce helpfulness, accuracy, or clarity.

    Original Sentence:"{sentence}"

    Perturb it slightly so it becomes less helpful, vauge or misleading:
    """

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content.strip()