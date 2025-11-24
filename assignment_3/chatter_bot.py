from assignment_3.chatter_bot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot
chatbot = ChatBot('Ron Obvious')

# Train chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Chat loop
print("ChatBot is ready! Type 'quit' or 'exit' to stop.\n")

while True:
    try:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Bot:", response)

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        break
