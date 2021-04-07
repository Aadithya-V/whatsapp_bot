from chatterbot import ChatBot
import time

chatbot = ChatBot("Botty")

message = "What are you doing?"
response = chatbot.get_response(message)
print(response)