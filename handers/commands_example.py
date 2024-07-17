from telebot import types

from loader import bot
from utils.logger import logger

from misc import text

@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    try:
        bot.send_message(
            chat_id=message.chat.id,
            text=text.start_msg.format(
                name=message.from_user.full_name
            )
        )

    except Exception as e:
        logger.error(e)

@bot.message_handler(content_types=['text'])
def echo_command(message: types.Message):
    try:
        bot.send_message(
            chat_id=message.chat.id,
            text=text.echo_msg.format(
                msg_text=message.text
            )
        )

    except Exception as e:
        logger.error(e)
