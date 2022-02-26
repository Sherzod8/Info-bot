from aiogram import types
from filters.private_filter import IsPrivate
from middlewares.language_midd import _
from loader import dp


# Echo bot
@dp.message_handler(IsPrivate,state=None)
async def bot_echo(message: types.Message):
    await message.answer(_("Noto‘g‘ri xabar yuborildi!"))
