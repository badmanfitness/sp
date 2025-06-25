from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["hello", ["Hey!", "Hi, how can I help you?"]],
    ["how are you?", ["I'm doing great, thanks!", "All good!"]],
    ["what is your name?", ["I'm your Python chatbot."]],
    ["bye", ["Goodbye!", "See you later!"]]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
chatbot.converse()