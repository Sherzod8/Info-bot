from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from middlewares.language_midd import _
contactKey = ReplyKeyboardMarkup(
    keyboard=[
        [   
            KeyboardButton(text='📞 Raqamni yuborish',request_contact=True),
        ],
        [   
            KeyboardButton(text='⬅️ Ortga'),
        ],
    ],
    resize_keyboard=True
)



back = ReplyKeyboardMarkup(
    keyboard=[
        [   

            KeyboardButton(text='⬅️ Ortga'),
        ],
    ],
    resize_keyboard=True
)