def chatbot(input_text):
    if "hello" in input_text.lower():
        return "Hello! How can I assist you today?"
    if "hi" in input_text.lower():
        return "Hi! How can I assist you today?"
    elif "how are you" in input_text.lower():
        return "I'm just a chatbot, but thanks for asking!"
    elif "how's your day" in input_text.lower():
        return "Sorry , I don't have feelings, but I'm here and ready to assist you!"
    elif "bye" in input_text.lower():
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Synthia: Goodbye!")
        break
    response = chatbot(user_input)
    print("Synthia:", response)

