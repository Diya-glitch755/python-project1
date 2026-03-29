responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "name": "I'm a simple chatbot created by a student.",
    "help": "Sure! You can ask me about my name, say hello, or exit.",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!"
    
}

def get_response(user_input):
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    return "I'm sorry, I didn't understand that. Can you rephrase?"

def main():
    print("Welcome to the Simple Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()