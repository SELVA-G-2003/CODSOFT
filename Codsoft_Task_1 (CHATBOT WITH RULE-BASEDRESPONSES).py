import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I assist you today?"

    elif re.search(r'\b(weather|forecast)\b', user_input):
        return "I'm a programming chatbot, so I don't have weather information. Ask me about programming!"

    elif re.search(r'\b(programming|language)\b', user_input):
        return "Sure, I can help you with programming languages. Which language are you interested in? Or would you like to see a list of languages?"

    elif re.search(r'\b(good|well done|great|nice)\b', user_input):
        return "Thank you! I'm here to help."

    elif re.search(r'\b(list|show|provide|display|view) programming languages\b', user_input):
        return programming_languages_list()

    elif user_input == 'list languages':
        return programming_languages_list()

    elif any(language in user_input for language in programming_languages.keys()):
        for language in programming_languages.keys():
            if language in user_input:
                return get_programming_language_info(language)

    elif re.search(r'\b(calculate|calculator)\b', user_input):
        calculation = re.search(r'(?<=calculate\s).*', user_input).group(0)
        return calculations(calculation)

    elif re.search(r'\b(okay|ok|sure|fine)\b', user_input):
        return "Great! Is there anything else you'd like to know?"

    elif re.search(r'\b(thank you|thanks)\b', user_input):
        return "You're welcome! Feel free to ask if you have more questions."

    elif re.search(r'\b(bye|goodbye)\b', user_input):
        return "Goodbye! Feel free to return if you have more questions."

    else:
        return "I'm sorry, I'm not sure how to respond to that. Could you please provide more context?"

programming_languages = {
    "python": "Python is a programming language that lets you work quickly and integrate systems more effectively.",
    "ruby": "Ruby is a dynamic, open source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write..",
    "java": "Java is an object-oriented programming language used for Coding everything from Mobile apps & enterprise Software to big applictaion.",
    "c++": "C++ is a powerful programming language commonly used for systems programming, game development, and high-performance applications.",
    "rust": "Rust is a systems programming language known for its focus on safety and performance. It's commonly used for building fast and reliable applications.",
    "javascript": "JavaScript is a scripting language used for web development to add interactivity and dynamic content to websites. It's essential for front-end web development.",
    "php": "PHP is a server-side scripting language designed for web development, primarily used to create dynamic web pages and applications.",
    "swift": "Swift is a programming language developed by Apple for iOS, macOS, watchOS, and tvOS app development. It's known for its performance and safety features.",
    "c#": "C# (C sharp) is a modern programming language developed by Microsoft. It's used for developing Windows applications, games, and more.",
    "Perl":"Perl is a high-level, interpreted, general-purpose programming language originally developed for text manipulation"
}
def get_programming_language_info(language):
    return programming_languages.get(language.lower(), "Sorry!..I'm not familiar with that programming language.")

def calculations(expression):
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"An error occurred: {e}"

def programming_languages_list():
    languages_list = "Here are some programming languages which I can tell you about:\n"
    for language in programming_languages.keys():
        languages_list += f"- {language.capitalize()}\n"
    return languages_list

def main():
    print("bot: Hello! I'm a chatbot.I can tell you about programming languages,or perform calculations,or engage in general conversation.")
    print("bot: Feel free to make a chat like :")
    print("bot: ==> Tell me something about Ruby.")
    print("bot: ==> what is 5*5?")
    print("bot: ==> what is java used for ?")
    print("bot: ==> List the programming languages you know about.")
    print("bot:  You can also say 'bye' to exit the chat:)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("bot: GoodBye!!!")
            break
        response = chatbot_response(user_input)
        print("bot:", response)


main()