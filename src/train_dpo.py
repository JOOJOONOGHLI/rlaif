from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from datasets import load_dataset
from trl import DPOTrainer

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
DATASET_PATH = "../data/dpo_dataset.json"
OUTPUT_DIR = "../checkpoints/dpo-llama-final"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

dataset = load_dataset("json", data_files=DATASET_PATH)["train"]

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=2,
    num_train_epochs=3,
    logging_dir="../logs",
    logging_steps=10,
    save_strategy="epoch",
    evaluation_strategy="no",
    report_to="none",
    fp16=True
)

trainer = DPOTrainer(
    model=model,
    args=training_args,
    beta=0.1,
    train_dataset=dataset,
    tokenizer=tokenizer,
    max_prompt_length=256,
    max_length=512
)

trainer.train()
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
