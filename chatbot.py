while True:
    user_input = input("You: ").lower()
    if "hello" in user_input:
        print("Bot: Hi there! How can I help you?")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: Sorry, I didn’t understand that.")