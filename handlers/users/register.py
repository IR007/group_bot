from aiogram import types

from filters import PrivateFilter
from loader import dp


@dp.message(PrivateFilter(), lambda message: message.text.lower() == 'profile')
async def send_hello(msg: types.Message):
    await msg.answer("Sizning profilingiz")
