from telebot import types, custom_filters

from misc.config import config


class IsAdminFilter(custom_filters.SimpleCustomFilter):
    key = 'is_admin'

    def check(self, message: types.Message):
        if message.from_user.id == config.admin_id:
            return True
        return False
