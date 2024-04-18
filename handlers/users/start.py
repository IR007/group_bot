from aiogram import types
from aiogram.filters import CommandStart

from keyboards.default import menu_markup
from loader import dp
from filters import GroupFilter, PrivateFilter, AdminFilter


@dp.message(CommandStart(), GroupFilter())
async def group_start(msg: types.Message):
    await msg.reply("Salom guruh a'zosi siz start berdingiz!")


@dp.message(AdminFilter(), CommandStart())
async def admin_start(msg: types.Message):
    await msg.answer("Siz adminsiz")


@dp.message(PrivateFilter(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_markup)
