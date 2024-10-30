#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from telebot import TeleBot
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

bot = TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN"))

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Welcome")

if __name__ == "__main__":
    bot.polling()

