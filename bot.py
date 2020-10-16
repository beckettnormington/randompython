from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'PyBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///memory.sqlite3'
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.humor")
trainer.train("chatterbot.corpus.english.emotion")
trainer.train("chatterbot.corpus.english.conversations")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

trainer.train("chatterbot.corpus.english.humor")
trainer.train("chatterbot.corpus.english.conversations")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.humor")
trainer.train("chatterbot.corpus.english.conversations")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english")

hello = chatbot.get_response("Hello!")

name = chatbot.get_response("what's your name?")

print(hello,"my name is",name)

while True:
    try:
       bot_input = input()
       bot_response = chatbot.get_response(bot_input)
       print(bot_response)
    except KeyboardInterrupt:
       print("Bye!")
       break
    except IndexError:
       print("I'm sorry, I got confused")
    except KeyError:
       print("I'm sorry, that math problem seems to be invalid")
