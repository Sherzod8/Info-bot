from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from middlewares.language_midd import _
language = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇿 O‘zbek tili", callback_data="uz")],
        [InlineKeyboardButton(text='🇷🇺 Русский язык', callback_data='ru')]   
    ]
)
main_manu = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text="ℹ️ Biz haqimizda", callback_data='about'),
        InlineKeyboardButton(text="🖥 Bizning kurslar", callback_data='courses')],
        [InlineKeyboardButton(text="🏢 O‘quv markazlar", callback_data="center"),
        InlineKeyboardButton(text="📞 Kontaktlar", callback_data='connect')]


    ]
)

courses = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🖥 Web dasturlash (Frontend)', callback_data='course_3')],
        [InlineKeyboardButton(text='💻 Backend dasturlash', callback_data="course_2")],
        [InlineKeyboardButton(text='👨🏻‍💻 Android ilovalarni yaratish', callback_data='course_1')],
        [InlineKeyboardButton(text='🤖 Mobil robototexnika', callback_data='course_5')],
        [InlineKeyboardButton(text='💠 Grafik va web dizayn', callback_data='course_4')],
        [InlineKeyboardButton(text='🇺🇸 IT-English', callback_data='course_8')],   
        [InlineKeyboardButton(text='👩‍💻 SMM-menejer', callback_data='course_6')], 
        [InlineKeyboardButton(text="🧩 Scratch + IT English", callback_data='course_7')],
        [InlineKeyboardButton(text='⬅️ Ortga', callback_data='course_0')],
    ]
)


centerKey = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text='🏢 IT Park Tashkent', callback_data='center_1')],
        [InlineKeyboardButton(text='🏢 IT Center Mirzo-Ulug`bek', callback_data='center_2')],
        [InlineKeyboardButton(text='🏢 IT Center Chilonzor', callback_data='center_3')],
        [InlineKeyboardButton(text='🏢 IT Center Sergeli', callback_data='center_4')],
        [InlineKeyboardButton(text='🏢 IT Center Yakkasaroy', callback_data='center_5')],
        [InlineKeyboardButton(text='🏢 IT Center Bektemir', callback_data='center_6')],
        [InlineKeyboardButton(text='⬅️ Ortga', callback_data='course_0')],

    ]
)

join = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='📝 Kursga yozilish', callback_data="1")],
        [InlineKeyboardButton(text='⬅️ Ortga', callback_data='0')]   
    ]
)

jinsKey = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🙎🏻‍♂️ Erkak', callback_data="Erkak"),
        InlineKeyboardButton(text='🙍🏻‍♀️ Ayol', callback_data='Ayol')],
        [InlineKeyboardButton(text='⬅️ Ortga', callback_data='0')]    
    ]


)

confirmationKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅ Tasdiqlash', callback_data="1")],
        [InlineKeyboardButton(text='❌ Bekor qilish', callback_data='0')]   
    ]
)