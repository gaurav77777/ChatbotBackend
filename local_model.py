from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model & tokenizer (only once)
model_name = "distilgpt2"  # or a local model you've downloaded
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_reply(prompt: str) -> str:
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, do_sample=True, top_k=50)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return reply
