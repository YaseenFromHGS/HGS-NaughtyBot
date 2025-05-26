from transformers import pipeline

def run_bot():
    chatbot = pipeline("text-generation", model="distilgpt2")
    print("🤖 HGS-NaughtyBot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
        print(f"Bot: {response}")
