from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from middlewares.language_midd import _
main_manuru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ℹ️ О нас", callback_data='about'),
        InlineKeyboardButton(text="🖥 Список курсов", callback_data='courses')],
        [InlineKeyboardButton(text="🏢 Учебные центры", callback_data="center"),
        InlineKeyboardButton(text="📞 Контакты", callback_data='connect')]


    ]
)

coursesru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🖥 Веб программирование', callback_data='course_3')],
        [InlineKeyboardButton(text='💻 Backend программирование', callback_data="course_2")],
        [InlineKeyboardButton(text='📲 Создание Android приложений', callback_data='course_1')],
        [InlineKeyboardButton(text='🤖 Мобильная робототехника', callback_data='course_5')],
        [InlineKeyboardButton(text='🎨 Графический и веб-дизайн', callback_data='course_4')],
        [InlineKeyboardButton(text='🇺🇸 IT-English', callback_data='course_8')], 
        [InlineKeyboardButton(text='👩‍💻 SMM-менеджер', callback_data='course_6')],
        [InlineKeyboardButton(text='🧩 Scratch + IT English', callback_data='course_7')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='course_0')],
    ]
)

centerKeyru = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text='🏢 IT Park Tashkent', callback_data='center_1')],
        [InlineKeyboardButton(text='🏢 IT Center Mirzo-Ulug`bek', callback_data='center_2')],
        [InlineKeyboardButton(text='🏢 IT Center Chilonzor', callback_data='center_3')],
        [InlineKeyboardButton(text='🏢 IT Center Sergeli', callback_data='center_4')],
        [InlineKeyboardButton(text='🏢 IT Center Yakkasaroy', callback_data='center_5')],
        [InlineKeyboardButton(text='🏢 IT Center Bektemir', callback_data='center_6')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='course_0')],

    ]
)


joinru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='📝 Записаться на курс', callback_data="1")],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='0')]   
    ]
)

jinsKeyru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🙎🏻‍♂️ Мужской', callback_data="Мужской"),
        InlineKeyboardButton(text='🙍🏻‍♀️ Женский', callback_data='Женский')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='0')]    
    ]


)

confirmationKeyboardru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅ Подтвердить', callback_data="1")],
        [InlineKeyboardButton(text='❌ Отмена', callback_data='0')]   
    ]
)