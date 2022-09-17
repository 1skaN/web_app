
# pip install 
# pip install Telegram-Bot8
from TelegramBot8 import Message, TeleBot, Update, ParseMode
import os
# telegramApiKey 
# telegramApiKey - бесплатный ключь для бота Телеграм
# API_KEY = os.getenv('telegramApiKey')
API_KEY = '5655684560:AAEiN0jD8QA_MQnUK0b5cU81s0jNNwiKebI'
bot = TeleBot(API_KEY)
@bot.add_command_helper(command="/hi")
def hi(message: Message):
    print(message)
    print('ti')
    pass
    # bot.send_message(message.chat.getID(), "Hello")
@bot.add_command_menu_helper(command="/bye", description="Just testing added command")
def bye(message: Message):
    # bot.send_message(message.chat.getID(), "Bye")
    pass
@bot.add_regex_helper(regex="^hi$")
def regex(message: Message):
    pass
    # bot.send_message(message.chat.getID(), "Hello")
bot.poll()
