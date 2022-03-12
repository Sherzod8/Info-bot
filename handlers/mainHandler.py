from aiogram import types
from aiogram.dispatcher.filters import state
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
from aiogram.types.message import Message
from data.config import ADMINS,GROUP
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from states.states import Anketa
from keyboards.inline.coursesKeyboard import join,courses,main_manu,centerKey,jinsKey,confirmationKeyboard
from keyboards.inline.rucoursesKeyboard import joinru,coursesru,main_manuru,centerKeyru,jinsKeyru,confirmationKeyboardru
from keyboards.default.defaultKeyboard import contactKey,back
from keyboards.default.rudefaoultbutton import contactKeyru, backru
from loader import dp,bot
from middlewares.language_midd import _
from data.config import BASE_DIR
from utils.db_api.database import DBcommands
db = DBcommands()

kurs_ru = ["Создание Android приложений","Backend программирование","Веб программирование","Графический и веб-дизайн","Мобильная робототехника","SMM-менеджер","Scratch + IT-English","IT-English"]
kurs_uz = ["Android ilovalarni yaratish","Backend dasturlash","Web dasturlash","Grafik va web dizayn","Mobil robototexnika","SMM-mutaxassis","Scratch + IT-English","IT-English"]
filial_ru = ["IT Park Tashkent","IT Center Mirzo-Ulug‘bek","IT Center Chilonzor","IT Center Sergeli","IT Center Yakkasaroy","IT Center Bektemir"]
filial_uz = ["IT Park Tashkent","IT Center Mirzo-Ulug‘bek","IT Center Chilonzor","IT Center Sergeli","IT Center Yakkasaroy","IT Center Bektemir"]

@dp.callback_query_handler(state=Anketa.main)
async def main(call: types.CallbackQuery,state: FSMContext):
    await call.message.delete()
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    
    if call.data=='courses':
        file_path = InputFile(path_or_bytesio=f'images/center/our_course.jpg')
        if user_l.language == 'uz':
            await call.message.answer_photo(file_path,"🚀 Yuqori malakali IT-mutaxassis bo‘lishni, dasturlash tillarini o‘rganishni yoki IT-sohasida o‘z malakangizni oshirishni xohlaysizmi? Bunday holda, IT Center PRO`ning o‘quv kurslari, siz uchun eng yaxshi va optimal yechim bo‘la oladi! 🤔\n\n💥 Bizning tajribali o‘qituvchilarimiz sizga IT-industriyasining barcha yo‘nalishlari bo‘yicha kerakli bo‘lgan bilim va ko‘nikmalarni berishadi va zamonaviy IT-kompaniyalarda munosib ish topishingizga ko‘maklashishadi.\n\n⚡️ O‘zingizni qiziqtirgan yo‘nalish bo‘yicha kurslarni tanlang va ro‘yxatdan o‘ting.👇👇👇",reply_markup=courses)
        else:
            await call.message.answer_photo(file_path,"🚀 Хотите стать высококвалифицированным IT-специалистом, изучать языки программарования или повысить свою квалификацию в IT-сфере? В таком случаи, курсы от IT Center PRO, это, пожалуй, лучшее и оптимальное решение для Вас! 🤔\n\n💥 Наши опытные наставники дадут Вам необходимые знания во всех направлениях IT-индустрии и помогут найти достойную работу в современных IT-компаниях.\n\n⚡️ Выберите курс по интересующему Вас направлению и зарегистрируйтесь по кнопке ниже 👇👇👇",reply_markup=coursesru)
        await call.answer(cache_time=0.02)
        await Anketa.course.set()
  
    elif call.data=='center':
        file_path = InputFile(path_or_bytesio=f'images/centers.jpg')
        if user_l.language == 'uz':
            await call.message.answer_photo(file_path,"📍 Iltimos, o‘zingizga qulay bo‘lgan <b>IT-Markaz</b>ni tanlang 👇",reply_markup=centerKey)
        else:
            await call.message.answer_photo(file_path,"📍 Пожалуйста, выберите удобный для Вас <b>IT-Центр</b> 👇",reply_markup=centerKeyru)
        await Anketa.center.set()
    elif call.data=="about":
        file_path = InputFile(path_or_bytesio=f'images/center/about_us.jpg')
        if user_l.language == 'uz':
            await call.message.answer_photo(file_path,"🏢 <b>IT Park Tashkent</b> 2021-yilda tashkil topgan bo‘lib, uning asosiy maqsadi - O‘zbekistonda IT sohasini rivojlantirish, IT-tadbirkorlik uchun zarur infratuzilmalarni yaratish, IT mutaxassislarni va IT kompaniyalarni qo‘llab-quvvatlash, istiqbolli startup loyihalarni ishga tushirish, shuningdek, dasturchilarni O‘zbekiston va jahon bozoriga tayyorlashdan iboratdir.\n\n🤔 Yuqori talabli IT-mutaxassis bo‘lishni xohlaysimi?\n\n⚡️ Unda bizning kurslarimizdan birini tanlang va «Kursga yozilish» tugmasi orqali ro‘yxatdan o‘ting.",reply_markup=join)
        else:    
            await call.message.answer_photo(file_path,"🏢 <b>IT Park Tashkent</b> был основан в 2021 году.\n👨‍💻 Наша основная цель – развитие IT-сферы в Узбекистане, создание необходимой инфраструктуры, всесторонняя поддержка IT-компаний и IT-специалистов, запуск перспективных стартап-проектов, а также организация эффективного использования компьютерных технологий и интернета среди населения и молодежи.\n\n🤔 Хотите стать востребованным IT-специалистом?\n\n⚡️ Тогда записывайтесь на наши курсы с помощью кнопки «Записаться на курс» ниже.",reply_markup=joinru)
    elif call.data=="connect":
        if user_l.language == 'uz':
            await call.message.answer("❗️Hurmatli do‘stlar, agarda sizda bizning faoliyatimiz bo‘yicha shikoyat, savol yoki takliflaringiz bo‘lsa, iltimos, ularni shu yerda yozib qoldiring.\n\n☎️ Qo‘shimcha ma`lumot uchun +998 90 178-00-03 yoki @mrsher8 ga murojaat qilishingiz mumkin.",reply_markup=back)
        else:
            await call.message.answer("❗️Дорогие друзья, если у Вас есть жалобы, вопросы или предложения касательно нашей деятельности, пожалуйста, оставьте их здесь.\n\n☎️ Подробная информация по телефону +998 90 178-00-03 или @mrsher8",reply_markup=backru)
        await Anketa.send.set()
    elif call.data=="1":
        file_path = InputFile(path_or_bytesio=f'images/centers.jpg')
        if user_l.language == 'uz':
            await call.message.answer_photo(file_path,"📍 Iltimos, o‘zingizga qulay bo‘lgan <b>IT-Markaz</b>ni tanlang 👇",reply_markup=centerKey)
        else:
            await call.message.answer_photo(file_path,"📍 Пожалуйста, выберите удобный для Вас <b>IT-Центр</b> 👇",reply_markup=centerKeyru)
        await Anketa.center.set()

    elif call.data=="0":
        if user_l.language == 'uz':
            await call.message.answer('Iltimos, menyu orqali keyingi qadamni tanlang!',reply_markup=main_manu)
        else:
            await call.message.answer('Пожалуйста, выберите следующий шаг в разделе меню!',reply_markup=main_manuru)
        await Anketa.main.set()

@dp.message_handler(state=Anketa.send)
async def course(message: Message, state:FSMContext):
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    if user_l.language == 'uz':
        if message.text=='⬅️ Ortga':
            await message.delete()
            a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
            await a.delete()
            await message.answer('Iltimos, menyu orqali keyingi qadamni tanlang!',reply_markup=main_manu)
            await Anketa.main.set()
        else:
            await bot.send_message(chat_id=GROUP[0],text=f"{message.text}")
    else:
        if message.text=='⬅️ Назад':
            await message.delete()
            a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
            await a.delete()
            await message.answer('Пожалуйста, выберите следующий шаг в разделе меню!',reply_markup=main_manuru)
            await Anketa.main.set()
        else:
            await bot.send_message(chat_id=GROUP[0],text=f"{message.text}")

@dp.message_handler(state=Anketa.send)
async def course(message: Message, state:FSMContext):
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    if user_l.language == 'uz':
        if message.text=='⬅️ Ortga':
            await message.delete()
            await message.answer('Iltimos, menyu orqali keyingi qadamni tanlang!',reply_markup=main_manu)
            await Anketa.main.set()
        else:
            a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
            await a.delete()
            await bot.send_message(chat_id=GROUP[0],text=f"{message.text}")
            await message.answer('Iltimos, menyu orqali keyingi qadamni tanlang!',reply_markup=main_manu)
            await Anketa.main.set()
    else:
        if message.text=='⬅️ Назад':
            await message.delete()
            await message.answer('Пожалуйста, выберите следующий шаг в разделе меню!',reply_markup=main_manuru)
            await Anketa.main.set()
        else:
            a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
            await a.delete()
            await bot.send_message(chat_id=GROUP[0],text=f"{message.text}")
            await message.answer('Пожалуйста, выберите следующий шаг в разделе меню!',reply_markup=main_manuru)
            await Anketa.main.set()

@dp.callback_query_handler(state=Anketa.center)
async def course(call: CallbackQuery, state:FSMContext):
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    await call.message.delete()
    data = call.data.split('_')
    ss = await state.get_data()
    if ss.get('course'): #  and ss.get('center') qo'shildi
        if data[1]=='0':
            if user_l.language == 'uz':
                await call.message.answer('Iltimos, menyu orqali keyingi qadamni tanlang!',reply_markup=main_manu)
            else:
                await call.message.answer('Пожалуйста, выберите следующий шаг в разделе меню!',reply_markup=main_manuru)
            await Anketa.main.set()
            return
        if user_l.language == 'uz':
            await state.update_data({'center':filial_uz[int(data[1])-1]})
            id = ss.get('id')
            file_path = InputFile(path_or_bytesio=f'images/uz/{id}.jpg')
            if id=='1':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Android - dunyodagi eng mashhur mobil platformadir. Android dasturchilar turli sohalarda faoliyat yuritishadi: murakkab himoya darajasiga ega onlayn-banking yoki onlayn-do‘kon uchun dastur yaratish, ingliz tilini o‘rganish uchun ilovalar yoki aviachiptalarni topish uchun mobil xizmatlarni ishlab chiqish. “Android ilovalarini yaratish” kursida siz Android uchun mobil ilovalarni noldan yaratish, Java va Kotlin tillarida dasturlashni o‘rganasiz. Middle-dasturchi darajasidagi loyihalarini yaratish uchun zarur bo‘lgan bilim va ko‘nikmalarga ega bo‘lasiz. Siz mustaqil ravishda mobil ilova mantig‘ini loyihalash, dastur muhitini sozlash imkoniyatini qo‘ldan boy bermang.\n\n📆 Kurs davomiyligi: 6 oy.\n\n💰 Kursning narxi: 1 000 000 so‘m/oy.").format(kurs_uz[int(id)-1]),reply_markup=join)
            elif id=='2':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Backend dasturchisi web-saytlar uchun backend yaratadi, so‘rovlarni qabul qiladigan, ma'lumotlar bazasi bilan aloqa o‘rnatadigan va ma'lumotlarni foydalanuvchiga uzatadigan dasturchidir. Dasturchi, saytning boshqa Internet xizmatlari bilan o‘zaro aloqasi uchun algoritmlarni ishlab chiqadi. Siz Python tilini o‘rganasiz: u talabga ega va sodda tildir. Shuningdek, siz eng muhim backend vositalarini o‘zlashtirasiz: Django, ma'lumotlar bazalari, GIT. O‘qitish jarayonida bir nechta operatsion xizmatlarni yaratasiz.\n\n📆 Kurs davomiyligi: 6 oy.\n\n💰 Kursning narxi: 1 000 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
            elif id=='3':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Frontend dasturchisi - saytning vizual ko‘rinishi ustida ishlaydi, shriftlarni, rasmlarni konfiguratsiyalarini tanlaydi, barcha grafik elementlarning to‘g‘ri ishlashini va kontentning qurilmalarga yuklanishlarini tekshiradi.\n\n📆 Kurs davomiyligi: 6 oy.\n\n💰 Kursning narxi: 800 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
            elif id=='4':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Kursning maqsadi - grafik dasturlar orqali murakkab rasmlar va kontent yaratish, o‘quvchilarning kreativ yaratuvchanlik qobiliyatini oshirish, Adobe Photoshop, Adobe Illustrator va Corel Draw kabi dasturlarini professional darajada o‘zlashtirishdir.\n\n📆 Kurs davomiyligi: 4 oy.\n\n💰 Kursning narxi: 800 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
            elif id=='5':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n🤖 Robototexnika kurslari bolalarning amaliy bilim olishiga qaratilgan.\n\nUshbu kursda o‘quvchilar Lego yoki o‘yinchoqlar o‘ynashmaydi. Ular murakkab elektron qurilmalarni (termostat, avtomatik sug‘orish, aqlli uy) dasturlash, shuningdek, Arduino asosida robotlar yasashni o‘rganishadi.\n\n📆 Kurs davomiyligi: 6 oy.\n\n💰 Kursning narxi: 500 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
            elif id=='6':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 SMM (Social media marketing) kursi davomida siz ijtimoiy tarmoqlarda brendni tanitish, kontent yaratish, va targeting kabi ko‘plab sohaga oid bilim va ko‘nikmalarga ega bo‘lasiz, bundan tashqari, sizda real loyihalar bilan ishlash, malaka oshirish imkoniyati mavjud bo‘ladi.\n\n📆 Kurs davomiyligi: 3 oy.\n\n💰 Kursning narxi: 1 000 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
            elif id=='7':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Scratch bolalarni dasturlashga olib kiradigan dasturdir. Oʻquvchilar ushbu dastur yordamida oʻzlarini vizual dasturlash muhitida sinab koʻrishadi. Qolaversa, 'Scratch+IT English' kursi ikki qismga boʻlinib, o’quvchilar darsning birinchi qismida Ingliz tilini, ikkinchi qismida Scratchni oʻrganishadilar. Dastur toʻliq amaliyotga asoslangan: har bir darsdan soʻng amaliy mashqlar, qiziqarli fikr-mulohazalarga boy boʻladi.\n\n📆 Kurs davomiyligi: 4 oy.\n\n💰 Kursning narxi: 1 000 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
            elif id=='8':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 IT-English kursi xalqaro miqyosida tan olingan standartlarga muvofiq, innovatsion usulda bo‘lib o‘tadi. Siz CEFR va IELTS imtihonlaridan muvaffaqiyatli o‘tishingiz uchun innovatsion tayyorgarlikka ega bo‘lasiz.\n\n📆 Kurs davomiyligi: 6 oy.\n\n💰 Kursning narxi: 460 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
            await call.answer(cache_time=0.02)
        else:
            await state.update_data(
                {'center':filial_ru[int(data[1])-1]})
            id = ss.get('id')
            file_path = InputFile(path_or_bytesio=f'images/ru/{id}.jpg')
            if data[1]=='1':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Android — самая популярная мобильная платформа в мире.\n\nAndroid-разработчики нужны в разных сферах: сделать онлайн-банкинг со сложной степенью защиты или приложение для интернет-магазина, разработать приложения для изучения английского языка или мобильный сервис по поиску авиабилетов.\n\nНа курсе «Разработка Android-приложений» Вы:\n\n- Научитесь с нуля создавать мобильные приложения под Android и программировать на Java и Kotlin.\n\n- Получите знания и навыки, необходимые для создания проектов уровня middle-специалиста.\n\n- Сможете самостоятельно проектировать логику работы мобильного приложения, настраивать среду приложений и другие ключевые события.\n\n📆 Продолжительность курса: 6 месяцев.\n\n💰 Стоимость курса: 1 000 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
            elif data[1]=='2':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Backend-разработчик - это специалист, который занимается программно-административной частью веб-приложения, внутренним содержанием системы, серверными технологиями — базой данных, архитектурой, программной логикой.\n\n⚡️ Вы изучите Python: это высокоуровневый язык программирования, а также освоите самые важные бэкэнд-инструменты: Django, Базы данных и Git.\n\n📆 Продолжительность курса: 6 месяцев.\n\n💰 Стоимость курса: 1 000 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
            elif data[1]=='3':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Frontend-разработчик – работает над визуальным видом сайта, подбирает шрифты, картинки, следит за тем, чтобы все графические элементы правильно работали, а контент загружался на всех устройствах.\n\n📆 Продолжительность курса: 6 месяцев.\n\n💰 Стоимость курса: 800 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
            elif data[1]=='4':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Целью курса является создание сложных изображений и контента с помощью графических программ, повышение творческих способностей учащихся, профессиональное освоение таких программ, как Adobe Photoshop, Adobe Illustrator и Corel Draw.\n\n📆 Продолжительность курса: 4 месяца.\n\n💰 Стоимость курса: 800 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
            elif data[1]=='5':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n🤖 Курсы робототехники нацелены на получение практических знаний. Мы не играем в Lego, мы учим программировать и собирать сложные электронные устройства (термостат, автополив, умный дом), а также строить роботов на базе Arduino.\n\n📆 Продолжительность курса: 6 месяцев.\n\n💰 Стоимость курса: 500 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
            elif data[1]=='6':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 На протяжении всего курса вы получите знания и навыки во многих областях, таких как продвижение бренда в социальных сетях, создание контента и таргетинг. Кроме того, у Вас будет возможность повысить квалификацию, работая с реальными проектами.\n\n📆 Продолжительность курса: 3 месяца.\n\n💰 Стоимость курса: 1 000 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
            elif data[1]=='7':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Scratch — это программа, которая начинает путь детей к программированию. Дети используют эту программу, чтобы проверить себя в среде визуального программирования.\n\n🖇 роме того, курс 'Scratch + IT English' разделен на две части, где студенты изучают английский язык в первой части урока и Scratch во второй. Программа построена на полноценной практике: после каждого занятия есть практические занятия, насыщенные интересными идеями.\n\n📆 Продолжительность курса: 4 месяца.\n\n💰 Стоимость курса: 1 000 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
            elif data[1]=='8':
                await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Курсы IT-English проходят инновационным образом в соответствии с международно-признанными стандартами. Вы получите инновационную подготовку для успешной сдачи экзаменов CEFR и IELTS.\n\n👩‍🏫 Более того, многие наши педагоги - высококвалифицированные специалисты с огромным опытом работы за рубежом.\n\n📆 Продолжительность каждого уровня: 3 месяца.\n\n💰 Стоимость курса: 460 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
        await call.answer(cache_time=0.02)

        await Anketa.choice.set()
        return
    else:
        if user_l.language == 'uz':
            if data[1]=='0':
                await call.message.answer('Iltimos, menyu orqali keyingi qadamni tanlang!',reply_markup=main_manu)
                await state.finish()
                await Anketa.main.set()
            else:
                await state.update_data(
                        {'center':filial_uz[int(data[1])-1]}
                        )
                file_path = InputFile(path_or_bytesio=f'images/center/{data[1]}.jpg')
                if data[1]=='1':
                    await call.message.answer_photo(file_path,("<b>🏢 {}</b>\n\n📍 Manzil: Maxtumquli ko‘chasi, 1A, IT Park Tashkent binosi.\n\n📌 Mo‘ljal: Muhammad al-Xorazmiy nomidagi ixtisoslashtirilgan IT-maktab.\n\n<b>📞 Tel</>: +998 99 309-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFuESB'>🔗 IT-Markaz xaritada</a>").format(filial_uz[int(data[1])-1]),reply_markup=courses)
                elif data[1]=='2':
                    await call.message.answer_photo(file_path,("<b>🏢 IT Center - {}</b>\n\n📍 Manzil:  Qorasu-4, 6A, 121-maktab.\n\n<b>📞 Tel</>: +998 99 180-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFqgwD'>🔗 IT-Markaz xaritada</a>").format(filial_uz[int(data[1])-1]),reply_markup=courses)
                elif data[1]=='3':
                    await call.message.answer_photo(file_path,("<b>🏢 IT Center - {}</b>\n\n📍 Manzil: Chilonzor hokimiyati, Jamoatchilik markazi binosi.\n\n📌 Mo‘ljal: Chilonzor metro.\n\n<b>📞 Tel</>: +998 99 177-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFdO0C'>🔗 IT-Markaz xaritada</a>").format(filial_uz[int(data[1])-1]),reply_markup=courses)
                elif data[1]=='4':
                    await call.message.answer_photo(file_path,("<b>🏢 IT Center - {}</b>\n\n📍 Manzil: Sergeli 4, 34.\n\n<b>📞 Tel</>: +998 99 137-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFhIXD'>🔗 IT-Markaz xaritada</a>").format(filial_uz[int(data[1])-1]),reply_markup=courses)
                elif data[1]=='5':
                    await call.message.answer_photo(file_path,("<b>🏢 IT Center - {}</b>\n\n📍 Manzil: Sho‘ta Rustaveli ko‘chasi, 17, Barkamol avlod binosi.\n\n📌 Mo‘ljal: Grand Mir mehmonxonasi.\n\n<b>📞 Tel</>: +998 99 107-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFh6SB'>🔗 IT-Markaz xaritada</a>").format(filial_uz[int(data[1])-1]),reply_markup=courses)
                elif data[1]=='6': 
                    await call.message.answer_photo(file_path,("<b>🏢 IT Center - {}</b>\n\n📍 Manzil: Yuqori Chirchiq koʻchasi, 43.\n\n<b>📞 Tel</>: +998 99 127-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFhs-B'>🔗 IT-Markaz xaritada</a>").format(filial_uz[int(data[1])-1]),reply_markup=courses)
                await call.answer(cache_time=0.02)
                # await state.finish()
                await Anketa.course.set()
        else:
            if data[1]=='0':
                await call.message.answer('Пожалуйста, выберите следующий шаг в разделе меню!',reply_markup=main_manuru)
                await state.finish()
                await Anketa.main.set()
            else:
                file_path = InputFile(path_or_bytesio=f'images/center/{data[1]}.jpg')
                if data[1]=='1':
                    await call.message.answer_photo(file_path,("<b>🏢 {} </b>\n\n📍 Адрес: улица Махтумкули, 1A, здание IT Park Tashkent\n\n📌 Ориентир: Специализированная IT-школа имени Аль-Хорезми\n\n<b>📞 Тел:</b> +998 99 309-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFuESB'>🔗 IT-Центр на карте</a>").format(filial_ru[int(data[1])-1]),reply_markup=coursesru)
                elif data[1]=='2':
                    await call.message.answer_photo(file_path,("<b>🏢 IT Center - {} </b>\n\n📍 Адрес: Карасу-4, 6А, Школа №121\n\n<b>📞 Тел:</b> +998 99 180-11-99\n\nЛыокация: <a href='https://yandex.uz/maps/-/CCU5nFqgwD'>🔗 IT-Центр на карте</a>").format(filial_ru[int(data[1])-1]),reply_markup=coursesru)
                elif data[1]=='3':
                    await call.message.answer_photo(file_path,("<b>🏢 IT Center - {} </b>\n\n📍 Адрес: Чиланзарский хокимият, здание общественного центра\n\n📌 Ориентир: Mетро Чиланзар\n\n<b>📞 Тел:</b> +998 99 177-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFdO0C'>🔗 IT-Центр на карте</a>").format(filial_ru[int(data[1])-1]),reply_markup=coursesru)
                elif data[1]=='4':
                    await call.message.answer_photo(file_path,("<b>🏢 IT Center - {} </b>\n\n📍 Адрес: Сергели-4, 34.\n\n<b>📞 Тел:</b> +998 99 137-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFhIXD'>🔗 IT-Центр на карте</a>").format(filial_ru[int(data[1])-1]),reply_markup=coursesru)
                elif data[1]=='5':
                    await call.message.answer_photo(file_path,("<b>🏢 IT Center - {} </b>\n\n📍 Адрес: ул. Шота Руставели, 17, здание «Баркамол авлод».\n\n📌 Ориентир: Школа №25, гостиница Grand Mir.\n\n<b>📞 Тел:</b> +998 99 107-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFh6SB'>🔗 IT-Центр на карте</a>").format(filial_ru[int(data[1])-1]),reply_markup=coursesru)
                elif data[1]=='6':
                    await call.message.answer_photo(file_path,("<b>🏢 IT Center - {} </b>\n\n📍 Адрес: ул. Юкори Чирчик, 43\n\n<b>📞 Тел:</b> +998 99 127-11-99\n\n<a href='https://yandex.uz/maps/-/CCU5nFhs-B'>🔗 IT-Центр на карте</a>").format(filial_ru[int(data[1])-1]),reply_markup=coursesru)
            
                await state.update_data(
                        {'center':filial_ru[int(data[1])-1]}
                        )
                await call.answer(cache_time=0.02)
                await Anketa.course.set()

@dp.callback_query_handler(state=Anketa.course)
async def course(call: CallbackQuery, state:FSMContext):
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    await call.message.delete()
    data = call.data.split('_')
    ss = await state.get_data()
    if user_l.language == 'uz':
        if data[1]=='0':
            await call.message.answer('Iltimos, menyu orqali keyingi qadamni tanlang!',reply_markup=main_manu)
            await state.finish()
            await Anketa.main.set()
        else:
            await state.update_data(
                    {'course':kurs_uz[int(data[1])-1],
                    'id':data[1]}
                    )
            if not ss.get('center'):
                file_path = InputFile(path_or_bytesio=f'images/centers.jpg')
                if user_l.language == 'uz':
                    await call.message.answer_photo(file_path,"Iltimos, o‘zingizga qulay bo‘lgan IT-Markazini tanlang 👇",reply_markup=centerKey)
                else:
                    await call.message.answer_photo(file_path,"Пожалуйста, выберите удобный для Вас <b>IT-Центр</b> 👇",reply_markup=centerKeyru)
                await Anketa.center.set()
                return
            else:
                id = data[1]
                file_path = InputFile(path_or_bytesio=f'images/uz/{data[1]}.jpg')
                if data[1]=='1':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Android - dunyodagi eng mashhur mobil platformadir. Android dasturchilar turli sohalarda faoliyat yuritishadi: murakkab himoya darajasiga ega onlayn-banking yoki onlayn-do‘kon uchun dastur yaratish, ingliz tilini o‘rganish uchun ilovalar yoki aviachiptalarni topish uchun mobil xizmatlarni ishlab chiqish. “Android ilovalarini yaratish” kursida siz Android uchun mobil ilovalarni noldan yaratish, Java va Kotlin tillarida dasturlashni o‘rganasiz. Middle-dasturchi darajasidagi loyihalarini yaratish uchun zarur bo‘lgan bilim va ko‘nikmalarga ega bo‘lasiz. Siz mustaqil ravishda mobil ilova mantig‘ini loyihalash, dastur muhitini sozlash imkoniyatini qo‘ldan boy bermang.\n\n📆 Kurs davomiyligi: 6 oy.\n\n💰 Kursning narxi: 1 000 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
                elif data[1]=='2':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Backend dasturchisi web-saytlar uchun backend yaratadi: so‘rovlarni qabul qiladigan, ma'lumotlar bazasi bilan aloqa o‘rnatadigan va ma'lumotlarni foydalanuvchiga uzatadigan dasturchidir. Dasturchi, saytning boshqa Internet xizmatlari bilan o‘zaro aloqasi uchun algoritmlarni ishlab chiqadi. Siz Python tilini o‘rganasiz: u talabga ega va sodda tildir. Shuningdek, siz eng muhim backend vositalarini o‘zlashtirasiz: Django, ma'lumotlar bazalari, git. O‘qitish jarayonida bir nechta operatsion xizmatlarni yaratasiz.\n\n📆 Kurs davomiyligi: 6 oy.\n\n💰 Kursning narxi: 1 000 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
                elif data[1]=='3':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻  Frontend dasturchisi - saytning vizual ko‘rinishi ustida ishlaydi, shriftlarni, rasmlarni konfiguratsiyalarini tanlaydi, barcha grafik elementlarning to‘g‘ri ishlashini va kontentning qurilmalarga yuklanishlarini tekshiradi.\n\n📆 Kurs davomiyligi: 6 oy.\n\n💰 Kursning narxi: 800 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
                elif data[1]=='4':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Kursning maqsadi - grafik dasturlar orqali murakkab rasmlar va kontent yaratish, o‘quvchilarning kreativ yaratuvchanlik qobiliyatini oshirish, Adobe Photoshop, Adobe Illustrator va Corel Draw kabi dasturlarini professional darajada o‘zlashtirishdir.\n\n📆 Kurs davomiyligi: 4 oy.\n\n💰 Kursning narxi: 800 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
                elif data[1]=='5':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n🤖 Robototexnika kurslari bolalarning amaliy bilim olishiga qaratilgan.\n\nUshbu kursda o‘quvchilar Lego yoki o‘yinchoqlar o‘ynashmaydi. Ular murakkab elektron qurilmalarni (termostat, avtomatik sug‘orish, aqlli uy) dasturlash, shuningdek, Arduino  asosida robotlar yasashni o‘rganishadi.\n\n📆 Kurs davomiyligi: 6 oy.\n\n💰 Kursning narxi: 500 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
                elif data[1]=='6':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 SMM (Social media marketing) kurs davomida sizga ijtimoiy tarmoqlarda brendni tanitish, kontent yaratish, va targeting kabi ko‘plab sohaga oid bilim va ko‘nikmalarga ega bo‘lish. Bundan tashqari, sizda real loyihalar bilan ishlab malaka oshirish imkoniyati mavjud bo‘ladi.\n\n📆 Kurs davomiyligi: 3 oy.\n\n💰 Kursning narxi: 1 000 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
                elif data[1]=='7':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Scratch bolalarni dasturlashga olib kiradigan dasturdir. Oʻquvchilar ushbu dastur yordamida oʻzlarini vizual dasturlash muhitida sinab koʻrishadi. Qolaversa, 'Scratch+IT English' kursi ikki qismga boʻlinib, o’quvchilar darsning birinchi qismida Ingliz tilini, ikkinchi qismida Scratchni oʻrganishadilar. Dastur toʻliq amaliyotga asoslangan: har bir darsdan soʻng amaliy mashqlar, qiziqarli fikr-mulohazalarga boy boʻladi.\n\n📆 Kurs davomiyligi: 4 oy.\n\n💰 Kursning narxi: 1 000 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
                elif data[1]=='8':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 IT-English kursi xalqaro miqyosida tan olingan standartlarga muvofiq, innovatsion usulda bo‘lib o‘tadi. Siz CEFR va IELTS imtihonlaridan muvaffaqiyatli o‘tishingiz uchun innovatsion tayyorgarlikka ega bo‘lasiz.\n\n📆 Kurs davomiyligi: 6 oy.\n\n💰 Kursning narxi: 460 000 so‘m/oy").format(kurs_uz[int(id)-1]),reply_markup=join)
                await call.answer(cache_time=0.02)
                await Anketa.choice.set()
    else:
        if data[1]=='0':
            await call.message.answer('Пожалуйста, выберите следующий шаг в разделе меню!',reply_markup=main_manuru)
            await state.finish()
            await Anketa.main.set()
        else: 
            await state.update_data(
            {'course':kurs_ru[int(data[1])-1],
            'id':data[1]}
            )
            if not ss.get('center'):
                file_path = InputFile(path_or_bytesio=f'images/centers.jpg')
                if user_l.language == 'uz':
                    await call.message.answer_photo(file_path,"📍 Iltimos, o‘zingizga qulay bo‘lgan <b>IT-Markaz</b>ni tanlang 👇",reply_markup=centerKey)
                else:
                    await call.message.answer_photo(file_path,"📍 Пожалуйста, выберите удобный для Вас <b>IT-Центр</b> 👇",reply_markup=centerKeyru)
                await Anketa.center.set()
                return
            else:
                id = data[1]
                file_path = InputFile(path_or_bytesio=f'images/ru/{data[1]}.jpg')
                if data[1]=='1':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Android — самая популярная мобильная платформа в мире.\n\nAndroid-разработчики нужны в разных сферах: для разработки онлайн-банкинга со сложной степенью защиты или приложений для интернет-магазинов,  изучения иностранных языков или мобильного сервиса по заказу и доставки еды/товаров.\n\nНа курсе «Разработка Android-приложений» Вы:\n\n- Научитесь с нуля создавать мобильные приложения под Android и программировать на Java и Kotlin.\n\n- Получите знания и навыки, необходимые для создания проектов уровня middle-специалиста.\n\n- Сможете самостоятельно проектировать логику работы мобильного приложения, настраивать среду приложений и другие ключевые события.\n\n📆 Продолжительность курса: 6 месяцев.\n\n💰 Стоимость курса: 1 000 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
                elif data[1]=='2':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Backend-разработчик это специалист, который занимается программно-административной частью веб-приложения, внутренним содержанием системы, серверными технологиями — базой данных, архитектурой, программной логикой.\n\n⚡️ Вы изучите Python: это высокоуровневый язык программирования. А также освоите самые важные бэкэнд-инструменты: Django, Базы данных и Git.\n\n📆 Продолжительность курса: 6 месяцев.\n\n💰 Стоимость курса: 1 000 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
                elif data[1]=='3':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Frontend-разработчик – работает над визуальным видом сайта, подбирает шрифты, картинки, следит за тем, чтобы все графические элементы правильно работали, а контент загружался на всех устройствах.\n\n📆 Продолжительность курса: 6 месяцев.\n\n💰 Стоимость курса: 800 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
                elif data[1]=='4':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Целью курса является создание сложных изображений и контента с помощью графических программ, повышение творческих способностей учащихся, профессиональное освоение таких программ, как Adobe Photoshop, Adobe Illustrator и Corel Draw.\n\n📆 Продолжительность курса: 4 месяца.\n\n💰 Стоимость курса: 800 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
                elif data[1]=='5':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n🤖 Курсы робототехники нацелены на получение практических знаний. Мы не играем в Lego, мы учим программировать и собирать сложные электронные устройства (термостат, автополив, системы Умного дома), а также строить роботов на базе Arduino.\n\n📆 Продолжительность курса: 6 месяцев.\n\n💰 Стоимость курса: 500 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
                elif data[1]=='6':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 На протяжении всего курса вы получите знания и навыки во многих областях, таких как продвижение бренда в социальных сетях, создание контента и таргетинг. Кроме того, у Вас будет возможность повысить квалификацию, работая с реальными проектами.\n📆 Продолжительность курса: 3 месяца.\n\n💰 Стоимость курса: 1 000 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
                elif data[1]=='7':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Scratch — это программа, которая начинает путь детей к программированию. Дети используют эту программу, чтобы проверить себя в среде визуального программирования.\n\n🖇 роме того, курс 'Scratch + IT English' разделен на две части, где студенты изучают английский язык в первой части урока и Scratch во второй. Программа построена на полноценной практике: после каждого занятия есть практические занятия, насыщенные интересными идеями.\n\n📆 Продолжительность курса: 4 месяца.\n\n💰 Стоимость курса: 1 000 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
                elif data[1]=='8':
                    await call.message.answer_photo(file_path,caption=("<b>📌 {}</b>\n\n👨‍💻 Курсы IT-English проходят инновационным образом в соответствии с международно-признанными стандартами. Вы получите инновационную подготовку для успешной сдачи экзаменов CEFR и IELTS.\n\n👩‍🏫 Более того, многие наши педагоги - высококвалифицированные специалисты с огромным опытом работы за рубежом.\n\n📆 Продолжительность каждого уровня: 3 месяца.\n\n💰 Стоимость курса: 460 000 сум/месяц.").format(kurs_ru[int(id)-1]),reply_markup=joinru)
                await call.answer(cache_time=0.02)
                await Anketa.choice.set()

@dp.callback_query_handler(state=Anketa.other)
async def other(call: CallbackQuery, state:FSMContext):
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    await call.message.delete()
    if user_l.language == 'uz':
        if call.data=='1':
            file_path = InputFile(path_or_bytesio=f'images/centers.jpg')
            await call.message.answer_photo(file_path,"📍 Iltimos, o‘zingizga qulay bo‘lgan <b>IT-Markaz</b>ni tanlang 👇",reply_markup=centerKey)
            await Anketa.center.set()
        else:
            await call.message.answer('Iltimos, menyu orqali keyingi qadamni tanlang!',reply_markup=main_manu)
            await state.finish()
            await Anketa.main.set()
    else:
        if call.data=='1':
            file_path = InputFile(path_or_bytesio=f'images/centers.jpg')
            await call.message.answer_photo(file_path,"📍 Пожалуйста, выберите удобный для Вас <b>IT-Центр</b> 👇",reply_markup=centerKeyru)
            await Anketa.center.set()
        else:
            await call.message.answer('Пожалуйста, выберите следующий шаг в разделе меню!',reply_markup=main_manuru)
            await state.finish()
            await Anketa.main.set()        

@dp.callback_query_handler(state=Anketa.choice)
async def choice(call: CallbackQuery, state:FSMContext):
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    await call.message.delete()
    if user_l.language == 'uz':
        if call.data=='1':
            await call.message.answer("Iltimos, to‘liq ismingizni kiriting",reply_markup=back)
            await Anketa.full_name.set()
        elif call.data=='0':
            file_path = InputFile(path_or_bytesio=f'images/center/1.jpg')
            await call.message.answer_photo(file_path,"📍 Iltimos, o‘zingizga qulay bo‘lgan <b>IT-Markaz</b>ni tanlang 👇",reply_markup=courses)
            await Anketa.course.set()
            await state.update_data({
                'center':''
            })
        await call.answer(cache_time=0.02)
    else:
        if call.data=='1':
            await call.message.answer("Пожалуйста, введите своё полное имя",reply_markup=backru)
            await Anketa.full_name.set()
        elif call.data=='0':
            file_path = InputFile(path_or_bytesio=f'images/center/1.jpg')
            await call.message.answer_photo(file_path,"📍 Пожалуйста, выберите удобный для Вас <b>IT-Центр</b> 👇",reply_markup=coursesru)
            await Anketa.course.set()
        await call.answer(cache_time=0.02)   

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
@dp.message_handler(state=Anketa.full_name)
async def full_name(message: types.Message,state:FSMContext):
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    if message.text in ["⬅️ Ortga",'⬅️ Назад'] :
        await message.delete()
        a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
        await a.delete()
        file_path = InputFile(path_or_bytesio=f'images/centers.jpg')
        if user_l.language == 'uz':
            await message.answer_photo(file_path,"📍 Iltimos, o‘zingizga qulay bo‘lgan <b>IT-Markaz</b>ni tanlang 👇",reply_markup=centerKey)
        else:
            await message.answer_photo(file_path,"📍 Пожалуйста, выберите удобный для Вас <b>IT-Центр</b> 👇",reply_markup=centerKeyru)
        await Anketa.center.set()
    else:
        try:
            if not has_numbers(message.text):
                await state.update_data(
                    {'full_name':message.text}
                    )
                if user_l.language == 'uz':
                    await message.answer('Iltimos, telefon raqamingizni kiriting yoki «Raqamni yuborish» tugmasini bosing.\n\nMisol uchun: +998 90 123-45-67',reply_markup=contactKey)
                else:
                    await message.answer('Пожалуйста, введите свой номер телефона или нажмите кнопку «Поделиться номером».\n\nПример: +998 90 123-45-67',reply_markup=contactKeyru)
                await Anketa.tel.set()
            else:
                await message.answer(_("Kiritgan ma'lumotingiz mos kelmadi"))
                await Anketa.full_name.set()
        except Exception as e:
            await bot.send_message(chat_id=ADMINS[0],text=str(e))

@dp.message_handler(content_types=types.ContentTypes.CONTACT,state=Anketa.tel)
@dp.message_handler(state=Anketa.tel)
async def phone(message: types.Message,state:FSMContext):
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    if message.contact:
        phone_number = message.contact
        await state.update_data(
        {'phone':phone_number['phone_number']}
        )
        a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
        await a.delete()
        await message.delete()
        if user_l.language == 'uz':
            await message.answer('Iltimos, jinsingizni tanlang',reply_markup=jinsKey)
        else:
            await message.answer("Пожалуйста, укажите свой пол",reply_markup=jinsKeyru)

        await Anketa.jins.set()
    elif message.text in ["⬅️ Ortga",'⬅️ Назад'] :
        await message.delete()
        a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
        await a.delete()
        if user_l.language == 'uz':
            await message.answer("Iltimos, to‘liq ismingizni kiriting",reply_markup=back)
        else:
            await message.answer("Пожалуйста, введите своё полное имя",reply_markup=backru)
        await Anketa.full_name.set()
    elif message.text[1:].isdigit and 9<=len(message.text)<=13:
        massage = message.text.replace(' ','')
        if massage[1:].isdigit():
            await state.update_data({
            'phone':message.text
            })
            a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
            await a.delete()
            await message.delete()
            if user_l.language == 'uz':
                await message.answer('Iltimos, jinsingizni tanlang',reply_markup=jinsKey)
            else:
                await message.answer("Пожалуйста, укажите свой пол",reply_markup=jinsKeyru)
            await Anketa.jins.set()
        else:
            if user_l.language == 'uz':
                await message.answer("Telefon raqam noto‘g‘ri formatda kiritildi❗️\n\nIltimos, telefon raqamni qayta kiriting.", reply_markup=contactKey)
            else:
                await message.answer("Номер телефона введен в неправильном формате❗️\n\nПожалуйста, введите номер телефона еще раз.", reply_markup=contactKeyru)
            await Anketa.tel.set()
    else:
        if user_l.language == 'uz':
            await message.answer("Telefon raqam noto‘g‘ri formatda kiritildi❗️\n\nIltimos, telefon raqamni qayta kiriting.", reply_markup=contactKey)
        else:
            await message.answer("Номер телефона введен в неправильном формате❗️\n\nПожалуйста, введите номер телефона еще раз.", reply_markup=contactKeyru)
        await Anketa.tel.set()
        
@dp.callback_query_handler(state=Anketa.jins)
async def jins(call: types.CallbackQuery, state: FSMContext):
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    if call.data!='0':
        await state.update_data(
            {'jins':call.data})
        await call.message.delete()
        if user_l.language == 'uz':
            await call.message.answer('Iltimos, yoshingizni kiriting',reply_markup=back)
        else:
            await call.message.answer('Пожалуйста, введите свой возраст',reply_markup=backru)
        await call.answer(cache_time=0.02)
        await Anketa.age.set()
    else:
        await call.message.delete()
        if user_l.language == 'uz':
                await call.message.answer('Iltimos, telefon raqamingizni kiriting yoki «Raqamni yuborish» tugmasini bosing\n\nMisol uchun: +998 90 123-45-67',reply_markup=contactKey)
        else:
            await call.message.answer('Пожалуйста, введите свой номер телефона или нажмите кнопку «Поделиться номером»\n\nПример: +998 90 123-45-67',reply_markup=contactKeyru)
        await Anketa.tel.set()

@dp.message_handler(state=Anketa.age)
async def skip(message:types.Message,state:FSMContext):
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    data = await state.get_data()

    if message.text in ["⬅️ Ortga",'⬅️ Назад'] :
        await message.delete()
        a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
        await a.delete()
        if user_l.language == 'uz':
            await message.answer('Iltimos, jinsingizni belgilang',reply_markup=jinsKey)
        else:
            await message.answer('Пожалуйста, укажите свой пол',reply_markup=jinsKeyru)
        await Anketa.jins.set()
    elif message.text.isdigit() and 7<=int(message.text)<70:
        a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
        await a.delete()
        try:
            await state.update_data({'age':message.text})
            image = data.get('id')
            if user_l.language == 'uz':
                file_path = InputFile(path_or_bytesio=f'images/uz/{image}.jpg')
                if data.get('jins')=='Ayol':
                    await message.answer_photo(file_path,_("\n📃 <b>F.I.SH.:</b> {} \n👫 <b>Jins:</b> {} \n📅 <b>Yosh:</b> {}\n🏢 <b>IT Center:</b> {}\n🖥 <b>Kurs:</b> {}\n📞 <b>Tel:</b> +{}\n\nQo‘shimcha savollaringiz mavjudmi? Unday holda bizning Call-markazimiga murojaat qiling.\n Tel: +998 99 309-11-99").format(data.get('full_name'),data.get('jins'),message.text,data.get("center"),data.get('course'),data.get('phone')))
                    
                else:
                    await message.answer_photo(file_path,_("\n📃 <b>F.I.SH.:</b> {} \n👫 <b>Jins:</b> {} \n📅 <b>Yosh:</b> {}\n🏢 <b>IT Center:</b> {}\n🖥 <b>Kurs:</b> {}\n📞 <b>Tel:</b> +{}\n\nSizda qo‘shimcha savollar mavjudmi? Unday holda bizning Call-markazimiga murojaat qiling.\n Tel: +998 99 309-11-99").format(data.get('full_name'),data.get('jins'),message.text,data.get("center"),data.get('course'),data.get('phone')))
                await message.answer("Iltimos, yuqoridagi ma’lumotlarizni tekshiring va <b>«Tasdiqlash»</b> tugmasini bosing.",reply_markup=confirmationKeyboard)
                await Anketa.confirm.set()
            else:
                file_path = InputFile(path_or_bytesio=f'images/ru/{image}.jpg')
                if data.get('jins')=='Женский':
                    await message.answer_photo(file_path,("\n📃 <b>ФИО:</b> {} \n👫 <b>Пол:</b> {} \n📅 <b>Возраст:</b> {}\n🏢 <b>IT-Центр:</b> {}\n🖥 <b>Курс:</b> {}\n📞 <b>Тел.:</b> +{}\n\nУ вас есть дополнительные вопросы? В таком случае обращайтесь в наш Call-центр.\n Тел: +998 99 309-11-99").format(data.get('full_name'),data.get('jins'),message.text,data.get("center"),data.get('course'),data.get('phone')))
                    
                else:
                    await message.answer_photo(file_path,("\n📃 <b>ФИО:</b> {} \n👫 <b>Пол:</b> {} \n📅 <b>Возраст:</b> {}\n🏢 <b>IT-Центр:</b> {}\n🖥 <b>Курс:</b> {}\n📞 <b>Тел.:</b> +{}\n\nУ Вас есть дополнительные вопросы? В таком случае обращайтесь в наш Call-центр.\n Тел: +998 99 309-11-99").format(data.get('full_name'),data.get('jins'),message.text,data.get("center"),data.get('course'),data.get('phone')))
                await message.answer("Пожалуйста, проверьте свои данные выше и нажмите кнопку <b>«Подтвердить»</b>.",reply_markup=confirmationKeyboardru)
                await Anketa.confirm.set()
        except Exception as e:
                await bot.send_message(chat_id=ADMINS[0],text=f"Foydalanuvchini kursga yozishda xatolik sodir bo‘ldi: {str(e)}")
    else:
        await message.answer(_('Yosh chegarasi xato kiritildi'))

@dp.callback_query_handler(state=Anketa.confirm)
async def confirm(call:types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    user = types.User.get_current()
    user_l = await db.get_user(str(user.id))
    if call.data=='1':
        data = await state.get_data()
        image = data.get('id')
    if user_l.language == 'uz':
        file_image = open(f'{BASE_DIR}/images/uz/{image}.jpg','rb')
        await call.message.answer('Iltimos, menyu orqali keyingi qadamni tanlang!',reply_markup=main_manu)
    else:
        file_image = open(f'{BASE_DIR}/images/ru/{image}.jpg','rb')
        await call.message.answer('Пожалуйста, выберите следующий шаг в разделе меню!',reply_markup=main_manuru)
    
    await bot.send_photo(chat_id=GROUP[0],photo=file_image,caption=_("\n📃 <b>F.I.SH.:</b> {} \n👫 <b>Jins:</b> {} \n📅 <b>Yosh:</b> {}\n🏢 <b>IT Center:</b> {}\n🖥 <b>Kurs:</b> {}\n📞 <b>Tel:</b> +{}\n\nSizda qo‘shimcha savollar mavjudmi? Unday holda bizning Call-markazimiga murojaat qiling.\n Tel: +998 99 309-11-99").format(data.get('full_name'),data.get('jins'),data.get("age"),data.get("center"),data.get('course'),data.get('phone')))
    await state.finish()
    await Anketa.main.set()

