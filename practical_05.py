"""
Develop an elementary chatbot for any suitable customer interaction application.
"""

def chatbot():
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "price": "Our prices are very competitive. Could you specify which product?",
        "order": "You can place an order on our website easily!",
        "bye": "Thank you for visiting. Have a great day!"
    }

    while True:
        user_input = input("You: ").lower()
        if user_input in ("exit", "quit"):
            print("Bot: Goodbye!")
            break
        print("Bot:", responses.get(user_input, "I'm sorry, I didn't understand that."))


# Run the chatbot
chatbot()
