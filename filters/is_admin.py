from aiogram import types

from data.config import ADMINS
from filters import PrivateFilter


class AdminFilter(PrivateFilter):

    async def __call__(self, message: types.Message):
        if await super(AdminFilter, self).__call__(message):
            return str(message.from_user.id) in ADMINS
        else:
            return False
