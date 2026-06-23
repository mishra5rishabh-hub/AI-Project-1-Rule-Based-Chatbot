print("AI Chatbot Started")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello!")

    elif user in ["bye", "exit"]:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand.")
