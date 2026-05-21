while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "hi":
        print("Bot: hello")

    elif user == "hii":
        print("Bot: hii!") 

    elif user == "how are you?":
        print("Bot: I am fine, thanks!")

    elif user=="how are you":
        print("Bot:I am fine, thanks!")

    elif user == "bye":
        print("Bot: Goodbye!")
       
    elif user == "i need help":
        print("Bot: how can i help you?")

    elif user=="are you a robot or human?":
        print("Bot:i am a robot")
        break
    else:
        print("Bot: Sorry, I don't understand.")