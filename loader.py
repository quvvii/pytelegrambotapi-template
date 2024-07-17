from telebot import TeleBot

from misc.config import token

bot: TeleBot = TeleBot(
    token=token,
    parse_mode="HTML",
    disable_web_page_preview=True
)
