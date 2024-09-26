from utils.logger import logger

from telebot import ExceptionHandler


class HandleExceptions(ExceptionHandler):
    def handle(self, exception):
        logger.error(exception)
