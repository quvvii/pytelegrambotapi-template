from telebot import TeleBot

from misc.config import config
from utils.exceptions import HandleExceptions


bot: TeleBot = TeleBot(
    token=config.token,
    parse_mode="HTML",
    disable_web_page_preview=True,
    exception_handler=HandleExceptions()
)
