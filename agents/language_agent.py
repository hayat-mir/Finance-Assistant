# agents/language_agent.py

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

class LanguageAgent:
    def __init__(self, model_name="sshleifer/tiny-gpt2"):
        print("Loading safe small model for CPU...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def summarize_brief(self, context):
        prompt = (
            "Summarize the following financial news in one short, professional sentence:\n\n"
            f"{context}\n\nSummary:"
        )
        result = self.generator(prompt, max_new_tokens=50, do_sample=True)[0]["generated_text"]
        return result.split("Summary:")[-1].strip()
