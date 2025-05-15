from openai import OpenAI

client = OpenAI(api_key="sk-...")  # Replace with your key

models = client.models.list()

for m in models.data:
    print(m.id)
