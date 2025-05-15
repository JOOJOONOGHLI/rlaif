import random
import nltk
from nltk.tokenize import sent_tokenize
from perturb_sentence_gemini import perturb_sentence

def generate_versions(response, num_versions=3):
    """Generate multiple perturbed versions of a response."""
    try:
        sentences = sent_tokenize(response)
        if len(sentences) == 0:
            return [response] * num_versions, response
            
        i = random.randint(0, len(sentences) - 1)
        original_sentence = sentences[i]
        versions = []

        for _ in range(num_versions):
            try:
                perturbed = perturb_sentence(original_sentence)
                modified = sentences[:i] + [perturbed] + sentences[i+1:]
                versions.append(" ".join(modified))
            except Exception as e:
                print(f"Error in perturbation: {e}")
                versions.append(response)  # Fallback to original
        
        return versions, original_sentence
    except Exception as e:
        print(f"Error in generate_versions: {e}")
        return [response] * num_versions, response