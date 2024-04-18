from aiogram import types
from aiogram.filters import BaseFilter


class GroupFilter(BaseFilter):

    async def __call__(self, message: types.Message):
        return message.chat.type in ['group', 'supergroup']
