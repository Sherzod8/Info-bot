from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from middlewares.language_midd import _
contactKeyru = ReplyKeyboardMarkup(
    keyboard=[
        [   
            KeyboardButton(text='📞 Поделиться номером',request_contact=True),
        ],
        [   
            KeyboardButton(text='⬅️ Назад'),
        ],
    ],
    resize_keyboard=True
)



backru = ReplyKeyboardMarkup(
    keyboard=[
        [   

            KeyboardButton(text='⬅️ Назад'),
        ],
    ],
    resize_keyboard=True
)