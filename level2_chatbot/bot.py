import random 
print("Hello! I am a level 2 chatbot.")
name = input("Enter your name: ")
print(f"Hello {name}! Type 'bye' to exit.\n")
intents = {
    "greeting": ["hi", "hello", "hey"],
    "name": ["name", "who are you"],
    "mood": ["sad", "happy", "bored"],
    "help": ["help", "assist", "support"]
}
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "name": ["I'm a chatbot.", "You can call me Bot."],
    "mood": [
        "I hope you're doing well!",
        "Stay positive.",
        "Things will get better!"
    ],
    "help": ["I can chat with you!", "Ask me anything simple. I will help you."]
}

unknown = [
    "I didn't understand that.",
    "Can you say it differently?",
    "I'm still learning."
]

def detect_intent(user_input):
    for intent,keywords in intents.items():
        for word in keywords:
            if word in user_input:
                return intent
    return None
        
while True:
    user=input("You: ").lower()
    if user in ["bye","exit","quit"]:
        print("Bot: Goodbye! Take care.")
        break

    intent=detect_intent(user)

    if intent:
        print("Bot:",random.choice(responses[intent]))

    else:
        print("Bot:",random.choice(unknown))
