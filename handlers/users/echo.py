from aiogram import types
from aiogram.fsm.state import State

from filters import PrivateFilter
from loader import dp


# Echo bot
@dp.message(PrivateFilter(), State())
async def bot_echo(message: types.Message):
    await message.answer(message.text)
