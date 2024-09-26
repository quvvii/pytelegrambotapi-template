from telebot import types

from loader import bot


@bot.message_handler(commands=['secret'], is_admin=True)
def secret_command(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Тут может быть информация, доступная только владельцу бота"
    )
