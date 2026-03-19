import random
print("Hello! i am level 1 chatbot.")
name =input("Enter your name : ")
print(f"Hello {name}! Type 'bye'to exit.\n")

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hello!", "Hi!", "Hey!"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "your name": ["I'm a chatbot.", "You can call me Bot!", "I am your assistant."],
    "help": ["I can chat with you!", "Try asking simple questions.", "I'm here to help!"]
}
unknown = [
    "Hmm I didn't understand that.",
    "Can you say it differently?",
    "I'm still learning."
]

while True:
    user =input("You: ").lower()
    if user in ["bye","exit","quit","goodbye","see you"]:
        print("Bot: Goodbye!")
        break

    elif user in responses:
        print("Bot:",random.choice(responses[user]))

    elif "sad" in user:
        print("Bot: Don't worry, things will get better")

    elif "bored" in user:
        print("Bot: Maybe watch a movie or play a game")

    elif "exam" in user:
        print("Bot: Stay calm and revise important topics")

    elif "joke" in user:
        print("Bot: Why did the computer go to school? To improve its byte!")

    else:
        print("Bot:", random.choice(unknown))