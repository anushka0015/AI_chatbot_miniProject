print("Hello! I am a level 1 ChatBot.")
print("Type 'Bye' to exit")
while True:
    user=input("You: ").lower()
    if user =="hi" or user =="hello":
        print("Bot: Hello!")
    elif user =="how are you":
        print("Bot: I am fine.")
    elif user =="your name":
        print("Bot: I am rule based chatbot.")
    elif user =="bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand that.")