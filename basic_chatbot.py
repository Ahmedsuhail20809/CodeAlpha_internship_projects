def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("👤 You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "what is your name":
            print("🤖 Chatbot: My name is Chatbot.")
        elif user_input == "what is your age":
            print("🤖 Chatbot: I'm a computer program, so I don't have an age.")
        elif user_input == "what is your favorite color":
            print("🤖 Chatbot: My favorite color is blue.")
        elif user_input == "what is your favorite food":
            print("🤖 Chatbot: My favorite food is pizza.")
        elif user_input == "what is your favorite movie":
            print("🤖 Chatbot: My favorite movie is The Matrix.")
        elif user_input == "what is your favorite book":
            print("🤖 Chatbot: My favorite book is The Great Gatsby.")
        elif user_input == "what is your favorite song":
            print("🤖 Chatbot: My favorite song is The Rolling Stones.")
        elif user_input == "what is your favorite game":
            print("🤖 Chatbot: My favorite game is Minecraft.")
        elif user_input == "what is your favorite sport":
            print("🤖 Chatbot: My favorite sport is soccer.")
        elif user_input == "what is your favorite animal":
            print("🤖 Chatbot: My favorite animal is the lion.")
        elif user_input == "what is your favorite city":
            print("🤖 Chatbot: My favorite city is New York.")
        elif user_input == "what is your favorite country and why?":
            print("🤖 Chatbot: My favorite country is Pakistan because it is a beautiful country.")
        elif user_input == 'how many languages do you know':
            print('🤖 Chatbot: I know 10 languages.')
        elif user_input == 'Which are they?':
            print('🤖 Chatbot: I know 10 languages, they are following\n English\n chines\n etchell')
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye!")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()
