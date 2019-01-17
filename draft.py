from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import random

updater = Updater(token='your_token')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
name = input()
question = input("All right, " + name + ", do not hesitate asking questions about your future: ")
ran_number = random.randint(1, 100)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me! What is your name? ")

# def echo(bot, update):
    # bot.send_message(chat_id=update.message.chat_id, text="Does not matter what you send, you are a fucker!")

# echo_handler = MessageHandler(Filters.text, echo)
start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
# dispatcher.add_handler(echo_handler)


updater.start_polling()
print("Job is finished")


# import random
# name = input("Your name please: ")
# question = input("All right, " + name + ", do not hesitate asking questions about your future: ")
# ran_number = random.randint(1, 100)
# if ran_number <= 20:
#     print("Impossible")
# elif 20 < ran_number <= 40:
#     print("Maybe")
# elif 40 < ran_number <= 60:
#     print("Highly possible")
# else:
#     print("Definitely")
