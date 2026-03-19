import random

print("Hello! I am a Level 2 Chatbot.")
name = input("Enter your name: ")
print(f"Hello {name}! Type 'bye' to exit.\n")

intents = {
    "greeting": [
        "hi", "hello", "hey", "hii", "heyy",
        "good morning", "good afternoon", "good evening",
        "namaste", "yo", "sup", "what's up", "whats up", "howdy"
    ],

    "name": [
        "name", "your name", "who are you",
        "tell me your name", "what should i call you",
        "identify yourself"
    ],

    "mood": [
        "sad", "unhappy", "depressed", "upset",
        "happy", "excited", "bored", "tired", "lonely",
        "feeling low", "not good", "bad day", "feeling great"
    ],

    "help": [
        "help", "assist", "support",
        "guide me", "can you help", "need help",
        "i need help", "help me", "can you assist me"
    ],

    "study": [
        "exam", "study", "studying", "revision",
        "test", "preparation", "syllabus", "homework"
    ],

    "joke": [
        "joke", "funny", "make me laugh", "tell me something funny"
    ]
}

responses = {
    "greeting": [
        "Hello!", "Hi there!", "Hey!", "Nice to meet you!"
    ],

    "name": [
        "I'm a chatbot.", "You can call me Bot!", "I am your assistant."
    ],

    "mood": [
        "I hope you're doing well",
        "Stay positive, things will get better!",
        "I'm here for you"
    ],

    "help": [
        "I can chat with you!",
        "Try asking about study, mood, or jokes",
        "I'm here to assist you!"
    ],

    "study": [
        "Stay focused and revise important topics",
        "Make a schedule and stick to it!",
        "Practice regularly for best results!"
    ],

    "joke": [
        "Why did the computer go to school? To improve its byte!",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ]
}

unknown = [
    "Hmm I didn't understand that.",
    "Can you say it differently?",
    "I'm still learning."
]
def detect_intent(user_input):
    scores = {}

    for intent, keywords in intents.items():
        score = 0
        for word in keywords:
            if word in user_input:
                score += 1
        scores[intent] = score

    best_intent = max(scores, key=scores.get)

    if scores[best_intent] == 0:
        return None

    return best_intent


while True:
    user = input("You: ").lower()

    if user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break

    intent = detect_intent(user)

    if intent:
        print("Bot:", random.choice(responses[intent]))
    else:
        print("Bot:", random.choice(unknown))