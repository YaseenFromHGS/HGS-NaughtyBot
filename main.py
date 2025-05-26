from naughtybot.chatbot import run_bot
from naughtybot.utils import load_training_resource

if __name__ == "__main__":
    run_bot()
    load_training_resource("data/test3.pdf")
    load_training_resource("data/test9.pdf")
