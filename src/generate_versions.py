import random
from nltk.tokenize import sent_tokenize
from .perturb_sentence import perturb_sentence

def generate_versions(response, num_versions=3):
    sentences = sent_tokenize(response)
    i = random.randint(0, len(sentences) - 1)
    original_sentence = sentences[i]
    versions = []

    for _ in range(num_versions):
        perturbed = perturb_sentence(original_sentence)
        modified = sentences[:i] + [perturbed] + sentences[i+1:]
        versions.append(" ".join(modified))
    
    return versions, original_sentence