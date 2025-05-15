import tqdm
import json
from score_response import score_response
from generate_versions_gemini import generate_versions

def create_dpo_dataset(prompts, responses_per_prompt=1, perturbations_per_response=3):
    """
    Create a dataset for DPO fine-tuning with the format:
    {
        "prompt": str,
        "chosen": str,
        "rejected": str
    }
    """
    dpo_data = []
    
    for prompt in tqdm(prompts):
        for _ in range(responses_per_prompt):
            # Generate original response with LLaMA
            original_response = generate_llama_response(prompt)
            
            # Generate perturbed versions
            perturbed_versions, _ = generate_versions(original_response, perturbations_per_response)
            
            # Score all responses (original + perturbations)
            all_responses = [original_response] + perturbed_versions
            scores = [score_response(prompt, resp) for resp in all_responses]
            
            # Find the best and worst responses
            best_idx = scores.index(max(scores))
            worst_idx = scores.index(min(scores))
            
            best_response = all_responses[best_idx]
            worst_response = all_responses[worst_idx]
            
            # Create DPO entry
            dpo_entry = {
                "prompt": prompt,
                "chosen": best_response,
                "rejected": worst_response,
                "original_response": original_response,
                "original_score": scores[0],
                "chosen_score": max(scores),
                "rejected_score": min(scores)
            }
            
            dpo_data.append(dpo_entry)
    
    return dpo_data

def save_dataset(dpo_data, output_file="dpo_dataset.json"):
    """Save the DPO dataset to a file."""
    # Save as JSON (preferred format for TRL)
    with open(output_file, "w") as f:
        json.dump(dpo_data, f, indent=2)
    
    # Also save as CSV for easier inspection
    df = pd.DataFrame(dpo_data)
    df.to_csv(output_file.replace(".json", ".csv"), index=False)
    
    print(f"Saved {len(dpo_data)} examples to {output_file}")

# Example usage
if __name__ == "__main__":
    # Sample prompts (replace with your actual prompts)
    prompts = [
        "Explain the process of photosynthesis.",
        "What factors led to the start of World War I?",
        "How does a neural network learn?",
        "Describe the impact of climate change on ocean ecosystems.",
        "Come up with a good reason for why Hernan Cortes burned his ships when arriving at the Americas."
    ]
    
    # Create the dataset
    dpo_data = create_dpo_dataset(prompts, responses_per_prompt=2, perturbations_per_response=3)
    
    # Save the dataset
    save_dataset(dpo_data)
    
    # Show example of how the data looks
    print("\nExample DPO data entry:")
    print(json.dumps(dpo_data[0], indent=2))