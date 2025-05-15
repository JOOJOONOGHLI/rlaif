from generate_versions_gemini import generate_versions
from score_response import score_response
from generate_response import generate_response
import nltk


prompt = "Explain who Leland Stanford Junior was and why he was significant to Silicon Valley."

# Generate the base response
response = generate_response(prompt)
print("Original response:", response)

# Generate perturbed versions
perturbed_versions, original_sentence = generate_versions(response, 3)

# Score each perturbed version
print("\nScoring perturbed versions:")
for i, version in enumerate(perturbed_versions, 1):
    score = score_response(prompt, response, version)  # Score the perturbed version, not the original
    print(f"\nVersion {i}:")
    print(f"Response: {version}")
    print(f"Score: {score}")