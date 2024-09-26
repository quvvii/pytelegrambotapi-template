from telebot import types

from loader import bot
from misc import text


@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=text.START_MSG.format(
            name=message.from_user.full_name
        )
    )


@bot.message_handler(content_types=['text'])
def echo_command(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=text.ECHO_MSG.format(
            msg_text=message.text
        )
    )
    raise Exception('test')
