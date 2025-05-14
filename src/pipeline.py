import json
import csv
from .generate_versions import generate_versions
from .score_response import score_response

def run_all(input_path, output_path):
    with open(input_path, 'r') as f:
        samples = json.load(f)

    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["prompt", "original_sentence", "version", "score"])

        for sample in samples:
            prompt = sample["prompt"]
            response = sample["response"]
            versions, orig_sentence = generate_versions(response)
            for version in versions:
                score = score_response(prompt, version)
                writer.writerow([prompt, orig_sentence, version, score])
 