import nltk
from nltk.chat.util import Chat, reflections

# Downloading nltk files
nltk.download('punkt')

# Patterns and their responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello there!", "Hi!", "Hey, how can I help you?"]    #Responding to user's greetings with a random friendly message.

    ],
    [
        r"what is your name?",
        ["I'm a chatbot created using NLTK!.You can call me alex."]    #  Replying it's identity.

    ],
    [
        r"how are you?",
        ["I'm good, thank you! How can I assist you today?"]      # Replies  with a friendly response.

    ],
    [
        r"what can you do?",
        ["I can answer your questions and chat with you!"]       # Responds with what the chatbot is capable of doing.

    ],
    [
        r"why are you created?",
        ["I'm created for chatting with people and helping them with their questions!"]        #Answering the hobby question 
    ],
    [
        r"what is your(location|city) ?", #Answering the questions by the user
        ['I am in the cloud, everywhere!']            
    ],
    [
        r"Can you tell a joke in English",  #tells a joke which is input by the developer
        ["Why did the computer go to the doctor? Because it had a virus!", "Why don’t robots ever panic? Because they have nerves of steel!"]
    ],
    [
        r"(.*) (bored|boring)", #gives a friendly response to the user
        ["Let’s talk about something fun! What are you interested in?"]
    ],
    [
        r"who created you ?",  ##Answers the question by the user
        ["I was created using Python and NLTK!", "My creator used the NLTK library to build me."]
    ],
    [
        r"quit|exit|bye", #the user exits of the chatbot
        ["Bye! Take care!", "Hope to chat with you again soon!", "Goodbye! 😊"]
    ],
    [
        r"(.*)",
        ["I'm not sure Can you rephrase?", "Tell me more about that."]    # Default response for unrecognized input; asks the user to clarify or provide more information.

    ]
]

# Creating chatbot
chatbot = Chat(pairs, reflections) # Create chatbot instance with defined patterns and reflections

# Starting the conversation
def start_chat():
    print("Hi, I'm your chatbot! Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__": #Ensures this code runs only when the script is executed.
    start_chat()
