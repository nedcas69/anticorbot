from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards import kb_uz, tengsiz, tb, buxgal, sb, pora
from loader import dp
import smtplib
from email.mime.text import MIMEText
from state import select_lang
from keyboards import lang_btn  # Импортируем нашу клавиатуру


@dp.message_handler(text='O\'zbekcha 🇺🇿')
async def uz(mess: Message):
    hello_text = "Sizning so'rovingiz biz uchun juda muhim. Iltimos, bildirmoqchi bo'lgan qoidabuzarlik toifasini tanlang:"
    await mess.answer(hello_text, reply_markup=kb_uz)


@dp.message_handler(text='Sozlamalar ⚙️')  # Создаём message handler который ловит команду /menu
async def til(message: Message, state: FSMContext):  # Создаём асинхронную функцию
    await message.answer("Tilni tanlang!", reply_markup=lang_btn)
    await state.finish()


@dp.message_handler(text='Poraxo\'rlik va korruptsiya.')  # Создаём message handler который ловит команду /menu
async def pora1(message: Message):  # Создаём асинхронную функцию
    mes_text = "Iltimos, aniq qandey qoida buzarlik ekanligini tanlang"
    await message.answer(mes_text, reply_markup=pora)
    await select_lang.pora.set()


@dp.message_handler(state=select_lang.pora)
async def send_mail1(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Iltimos, xabaringizni qoldiring.\n\nℹ️ O‘z murojaatingizga javob olishni istasangiz, o‘zingizning F.I.O. va bog‘lanish uchun ma’lumotlarni ko‘rsating.(El-pochta yoki telefon raqamingiz)', reply_markup=kb_uz)
    await state.finish()
    await select_lang.pora1.set()

    @dp.message_handler(state=select_lang.pora1)
    async def send_mail11(mess: Message, state: FSMContext):
        await state.finish()
        send_text = mess.text
        sender = "compliance1@uzbeksteel.uz"
        password = '$COMPL11'
        server = smtplib.SMTP("10.3.1.33", 587)
        server.starttls()
        server.login(sender, password)
        msg = MIMEText(send_text)
        msg['Subject'] = sub
        server.sendmail(sender, 'compliance2@uzbeksteel.uz', msg.as_string())
        server.sendmail(sender, 'a.abdullayev@uzbeksteel.uz', msg.as_string())
        ans_text = "Xabaringiz yuborildi."
        await mess.answer(ans_text, reply_markup=kb_uz)


@dp.message_handler(text='Buxgalteriya hisobini buzish.')  # Создаём message handler который ловит команду /menu
async def buxgalter(message: Message):  # Создаём асинхронную функцию
    mes_text = "Iltimos, aniq qandey qoida buzarlik ekanligini tanlang"
    await message.answer(mes_text, reply_markup=buxgal)
    await select_lang.buxgal.set()


@dp.message_handler(state=select_lang.buxgal)
async def send_mail2(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Iltimos, xabaringizni qoldiring.\n\nℹ️ O‘z murojaatingizga javob olishni istasangiz, o‘zingizning F.I.O. va bog‘lanish uchun ma’lumotlarni ko‘rsating.(El-pochta yoki telefon raqamingiz)', reply_markup=kb_uz)
    await state.finish()
    await select_lang.buxgal1.set()

    @dp.message_handler(state=select_lang.buxgal1)
    async def send_mail21(mess: Message, state: FSMContext):
        await state.finish()
        send_text = mess.text
        sender = "compliance1@uzbeksteel.uz"
        password = '$COMPL11'
        server = smtplib.SMTP("10.3.1.33", 587)
        server.starttls()
        server.login(sender, password)
        msg = MIMEText(send_text)
        msg['Subject'] = sub
        server.sendmail(sender, 'compliance3@uzbeksteel.uz', msg.as_string())
        server.sendmail(sender, 'a.abdullayev@uzbeksteel.uz', msg.as_string())
        ans_text = "Xabaringiz yuborildi."
        await mess.answer(ans_text, reply_markup=kb_uz)


@dp.message_handler(
    text='Tengsiz bandlik va mehnat sharoitlari.')  # Создаём message handler который ловит команду /menu
async def tengsizlik(message: Message):  # Создаём асинхронную функцию
    mes_text = "Iltimos, aniq qandey qoida buzarlik ekanligini tanlang"
    await message.answer(mes_text, reply_markup=tengsiz)
    await select_lang.tengsiz.set()


@dp.message_handler(state=select_lang.tengsiz)
async def send_mail3(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Iltimos, xabaringizni qoldiring.\n\nℹ️ O‘z murojaatingizga javob olishni istasangiz, o‘zingizning F.I.O. va bog‘lanish uchun ma’lumotlarni ko‘rsating.(El-pochta yoki telefon raqamingiz)', reply_markup=kb_uz)
    await state.finish()
    await select_lang.tengsiz1.set()


    @dp.message_handler(state=select_lang.tengsiz1)
    async def send_mail31(mess: Message, state: FSMContext):
        await state.finish()
        send_text = mess.text
        sender = "compliance1@uzbeksteel.uz"
        password = '$COMPL11'
        server = smtplib.SMTP("10.3.1.33", 587)
        server.starttls()
        server.login(sender, password)
        msg = MIMEText(send_text)
        msg['Subject'] = sub
        server.sendmail(sender, 'compliance4@uzbeksteel.uz', msg.as_string())
        server.sendmail(sender, 'a.abdullayev@uzbeksteel.uz', msg.as_string())
        ans_text = "Xabaringiz yuborildi."
        await mess.answer(ans_text, reply_markup=kb_uz)


@dp.message_handler(
    text='Salomatlik, xavfsizlik va atrof-muhitga tahdidlar.')  # Создаём message handler который ловит команду /menu
async def tbs(message: Message):  # Создаём асинхронную функцию
    mes_text = "Iltimos, aniq qandey qoida buzarlik ekanligini tanlang"
    await message.answer(mes_text, reply_markup=tb)
    await select_lang.tb.set()


@dp.message_handler(state=select_lang.tb)
async def send_mail4(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Iltimos, xabaringizni qoldiring.\n\nℹ️ O‘z murojaatingizga javob olishni istasangiz, o‘zingizning F.I.O. va bog‘lanish uchun ma’lumotlarni ko‘rsating.(El-pochta yoki telefon raqamingiz)', reply_markup=kb_uz)
    await state.finish()
    await select_lang.tb1.set()


    @dp.message_handler(state=select_lang.tb1)
    async def send_mail41(mess: Message, state: FSMContext):
        await state.finish()
        send_text = mess.text
        sender = "compliance1@uzbeksteel.uz"
        password = '$COMPL11'
        server = smtplib.SMTP("10.3.1.33", 587)
        server.starttls()

        server.login(sender, password)
        msg = MIMEText(send_text)
        msg['Subject'] = sub
        server.sendmail(sender, 'compliance5@uzbeksteel.uz', msg.as_string())
        server.sendmail(sender, 'a.abdullayev@uzbeksteel.uz', msg.as_string())
        ans_text = "Xabaringiz yuborildi."
        await mess.answer(ans_text, reply_markup=kb_uz)


@dp.message_handler(
    text='Axborotning chiqib ketishi/yo\'q qilinishi.')  # Создаём message handler который ловит команду /menu
async def sbt(message: Message):  # Создаём асинхронную функцию
    mes_text = "Iltimos, aniq qandey qoida buzarlik ekanligini tanlang"
    await message.answer(mes_text, reply_markup=sb)
    await select_lang.sb.set()


@dp.message_handler(state=select_lang.sb)
async def send_mail5(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Iltimos, xabaringizni qoldiring.\n\nℹ️ O‘z murojaatingizga javob olishni istasangiz, o‘zingizning F.I.O. va bog‘lanish uchun ma’lumotlarni ko‘rsating.(El-pochta yoki telefon raqamingiz)', reply_markup=kb_uz)
    await state.finish()
    await select_lang.sb1.set()

    @dp.message_handler(state=select_lang.sb1)
    async def send_mail51(mess: Message, state: FSMContext):
        await state.finish()
        send_text = mess.text
        sender = "compliance1@uzbeksteel.uz"
        password = '$COMPL11'
        server = smtplib.SMTP("10.3.1.33", 587)
        server.starttls()
        server.login(sender, password)
        msg = MIMEText(send_text)
        msg['Subject'] = sub
        server.sendmail(sender, 'compliance6@uzbeksteel.uz', msg.as_string())
        server.sendmail(sender, 'a.abdullayev@uzbeksteel.uz', msg.as_string())
        ans_text = "Xabaringiz yuborildi."
        await mess.answer(ans_text, reply_markup=kb_uz)


@dp.message_handler(text='Boshqalar.')  # Создаём message handler который ловит команду /menu
async def lang(message: Message, state: FSMContext):  # Создаём асинхронную функцию
    sub = message.text
    mes_text = 'Iltimos, xabaringizni qoldiring.\n\nℹ️ O‘z murojaatingizga javob olishni istasangiz, o‘zingizning F.I.O. va bog‘lanish uchun ma’lumotlarni ko‘rsating.(El-pochta yoki telefon raqamingiz)'
    await message.answer(mes_text, reply_markup=kb_uz)
    await select_lang.boshqalar.set()

    @dp.message_handler(state=select_lang.boshqalar)
    async def send_mail6(mess: Message, state: FSMContext):
        send_text = mess.text
        sender = "compliance1@uzbeksteel.uz"
        password = '$COMPL11'
        server = smtplib.SMTP("10.3.1.33", 587)
        server.starttls()
        server.login(sender, password)
        msg = MIMEText(send_text)
        msg['Subject'] = sub

        await state.finish()
        server.sendmail(sender, 'compliance7@uzbeksteel.uz', msg.as_string())
        server.sendmail(sender, 'a.abdullayev@uzbeksteel.uz', msg.as_string())

        ans_text = "Xabaringiz yuborildi."
        await mess.answer(ans_text, reply_markup=kb_uz)
