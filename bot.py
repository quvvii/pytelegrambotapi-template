from loader import bot

from utils.filters import IsAdminFilter
from utils.logger import logger

import handers

def on_startup():
    logger.info('START BOT')

    bot.add_custom_filter(IsAdminFilter())

    bot.infinity_polling(skip_pending=True)

if __name__ == '__main__':
    on_startup()
