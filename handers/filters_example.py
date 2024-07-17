from telebot import types

from loader import bot
from utils.logger import logger

@bot.message_handler(commands=['secret'], is_admin=True)
def secret_command(message: types.Message):
    try:
        bot.send_message(
            chat_id=message.chat.id,
            text="Тут может быть информация, доступная только владельцу бота"
        )

    except Exception as e:
        logger.error(e)
