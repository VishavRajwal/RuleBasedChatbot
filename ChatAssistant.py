print("Hii....Welcome to the Chatbot! how can i assist you today?")
print("you can ask me basic questions, Type 'exit to quit the chat")

#chatbot memory creation [dictionary of responses]
responses = {
"hello": " Hello! How can i assist you ",
"hi": "Hi! how can i assist you",
"hii": "Hey bud! is there anything i can help you with?",
"hey": "Hey there! What can I do for you?",
"good morning": "Good morning! Hope you have a great day ahead.",
"good afternoon": "Good afternoon! How can I help?",
"good evening": "Good evening! How can I help?",
"good night": "Good night! Sleep well and see you soon.",
"how are you": "I am good, Thanks for asking",
"who are you": "I am a Chatbot creaed to assist you with your queries",
"how is your day": "It's going well, thanks! Every conversation makes it better.",
"what are you doing": "I'm chatting with you and waiting for your next question.",
"question": "go ahead and ask your question, I will try to answer it",
"i am fine": "Glad to hear that!",
"i am good": "Great to hear that!",
"i am happy": "Great to hear that! Keep smiling and stay positive.",
"i am sad": "I'm sorry you're feeling low. Talking to a friend or someone you trust can really help.",
"i am bored": "Try learning something new, like a small coding challenge. Want a motivational line?",
"motivate me": "Build through failure, learn through errors, and let your code speak for your ambition 💻🔥",
"what is your name": "I'm a simple rule-based chatbot. You can call me ChatBuddy.",
"who made you": "I was created by a student learning Python.",
"who created you": "I was created by a student learning Python.",
"are you a robot": "I'm a program, not a human, but I try to be helpful.",
"are you human": "No, I'm a chatbot running as a Python program.",
"how old are you": "I don't have an age, I'm just a program.",
"where do you live": "I live inside your computer, in a Python file.",
"what can you do": "I can answer basic questions and chat with you. I'm still learning!",
"can you help me": "Of course! Tell me what you need.",
"happy": "Great to hear that! Keep smiling and stay positive",
"what is python": "Python is a beginner-friendly programming language used for web, data, AI and automation.",
"what is ai": "AI (Artificial Intelligence) is when machines are built to do tasks that normally need human thinking.",
"what is a chatbot": "A chatbot is a program that talks with people using text or voice.",
"what is coding": "Coding is writing instructions that a computer can follow.",
"i am tired": "Take a short break, drink some water, and come back stronger.",
"i failed": "Failure is feedback. Find what went wrong, fix it, and try again.",
"thank you": "You're welcome! 😊",
"thanks": "You're welcome! Happy to help.",
"sorry": "No problem at all!",
"please": "Sure, tell me what you need.",
"bye": "Goodbye! Have a great day!",
"see you": "See you soon! Take care.",


    }
#method/function to get response from the bot
def getresponse(userquestion):
    userquestion = userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
    return "Sorry, I dont have any answer for that, please try asking something else"

#take user input

while True:
    userinput = input("please ask your question:")

    if userinput.strip().lower() == "exit":
        print("Bot Response: Goodbye!")
        break

    reply = getresponse(userinput)
    print("Bot Response: ", reply)