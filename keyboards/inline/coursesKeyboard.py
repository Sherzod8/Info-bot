from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from middlewares.language_midd import _
language = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="๐บ๐ฟ Oโzbek tili", callback_data="uz")],
        [InlineKeyboardButton(text='๐ท๐บ ะ ัััะบะธะน ัะทัะบ', callback_data='ru')]   
    ]
)
main_manu = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text="โน๏ธ Biz haqimizda", callback_data='about'),
        InlineKeyboardButton(text="๐ฅ Bizning kurslar", callback_data='courses')],
        [InlineKeyboardButton(text="๐ข Oโquv markazlar", callback_data="center"),
        InlineKeyboardButton(text="๐ Kontaktlar", callback_data='connect')]


    ]
)

courses = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='๐ฅ Web dasturlash (Frontend)', callback_data='course_3')],
        [InlineKeyboardButton(text='๐ป Backend dasturlash', callback_data="course_2")],
        [InlineKeyboardButton(text='๐ฒ Android ilovalarni yaratish', callback_data='course_1')],
        [InlineKeyboardButton(text='๐ค Mobil robototexnika', callback_data='course_5')],
        [InlineKeyboardButton(text='๐  Grafik va web dizayn', callback_data='course_4')],
        [InlineKeyboardButton(text='๐บ๐ธ IT-English', callback_data='course_8')],   
        [InlineKeyboardButton(text='๐ฉโ๐ป SMM-menejer', callback_data='course_6')], 
        [InlineKeyboardButton(text="๐งฉ Scratch + IT English", callback_data='course_7')],
        [InlineKeyboardButton(text='โฌ๏ธ Ortga', callback_data='course_0')],
    ]
)


centerKey = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text='๐ข IT Park Tashkent', callback_data='center_1')],
        [InlineKeyboardButton(text='๐ข IT Center Mirzo-Ulug`bek', callback_data='center_2')],
        [InlineKeyboardButton(text='๐ข IT Center Chilonzor', callback_data='center_3')],
        [InlineKeyboardButton(text='๐ข IT Center Sergeli', callback_data='center_4')],
        [InlineKeyboardButton(text='๐ข IT Center Yakkasaroy', callback_data='center_5')],
        [InlineKeyboardButton(text='๐ข IT Center Bektemir', callback_data='center_6')],
        [InlineKeyboardButton(text='โฌ๏ธ Ortga', callback_data='course_0')],

    ]
)

join = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='๐ Kursga yozilish', callback_data="1")],
        [InlineKeyboardButton(text='โฌ๏ธ Ortga', callback_data='0')]   
    ]
)

jinsKey = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='๐๐ปโโ๏ธ Erkak', callback_data="Erkak"),
        InlineKeyboardButton(text='๐๐ปโโ๏ธ Ayol', callback_data='Ayol')],
        [InlineKeyboardButton(text='โฌ๏ธ Ortga', callback_data='0')]    
    ]


)

confirmationKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='โ Tasdiqlash', callback_data="1")],
        [InlineKeyboardButton(text='โ Bekor qilish', callback_data='0')]   
    ]
)