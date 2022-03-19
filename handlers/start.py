from aiogram import types
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.storage import FSMContext
from data.config import GROUP
from keyboards.inline.coursesKeyboard import language,main_manu
from keyboards.inline.rucoursesKeyboard import main_manuru
from states.states import Anketa
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from utils.db_api.database import DBcommands
from middlewares.language_midd import _
from filters import IsGroup,IsPrivate


db = DBcommands()

from loader import dp,bot


@dp.message_handler(IsGroup(),commands=['start','lang'],state='*')
async def bot_start(message: types.Message,state:FSMContext):
    await state.finish()
    await bot.send_message(chat_id=GROUP[0],text="Бот не используется в группе, пожалуйста перейдите в чат!\n\nGuruhda bot ishlatilmaydi, iltimos, chatga o‘ting!")

@dp.message_handler(IsPrivate(),commands=['start','lang'],state='*')
async def bot_start(message: types.Message,state:FSMContext):
    await state.finish()
    await db.add_user()
    a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
    await a.delete()
    await message.answer("Assalomu alaykum!\n\n🌐 <b>IT Park Tashkent</b>`ning rasmiy Telegram-botiga xush kelibsiz!\n📚Iltimos, ta’lim tilini tanlang.\n\n➖➖➖➖➖➖➖➖➖➖\n\nЗдраствуйте!\n\n🌐 Добро пожаловать на официальный Telegram-бот <b>IT Park Tashkent!</b>\n📚Пожалуйста, выберите язык обучения.",reply_markup=language)
    await Anketa.language.set()

@dp.callback_query_handler(lambda message: message.data in ['uz', 'ru'], state=Anketa.language)
async def set_language(call:types.CallbackQuery):
    await call.message.delete()
    a = await call.message.answer('.',reply_markup=ReplyKeyboardRemove())
    await a.delete()
    language = None
    if call.data == "uz":
        await db.set_language(call.data)
        language = 'uz'
        await call.message.answer("Iltimos, menyu orqali keyingi qadamni tanlang!", reply_markup=main_manu)
    elif call.data == "ru":
        await db.set_language(call.data)
        language = 'ru'
        await call.message.answer("Пожалуйста, выберите следующий шаг в разделе меню!", reply_markup=main_manuru)
    await call.answer(cache_time=0.02)
    await Anketa.main.set()

