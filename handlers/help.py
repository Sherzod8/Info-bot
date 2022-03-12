from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from middlewares.language_midd import _

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (_("Buyruqlar: "),
            _("/start - Botni ishga tushirish"),
            _("Agar bot bilan xatolik sodir bo‘lsa /start buyrug‘idan foydalaning"))
    
    await message.answer("\n".join(text))
