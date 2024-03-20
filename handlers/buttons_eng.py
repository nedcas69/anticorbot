from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards import kb_eng, corrupt, viol, unequal, health, leakage
from loader import dp
import smtplib
from email.mime.text import MIMEText
from state import select_lang
from keyboards import lang_btn  # Импортируем нашу клавиатуру


@dp.message_handler(text='English 🇬🇧')
async def uz(mess: Message):
    hello_text = "Your request is very important to us. Please select the category of violation you are about to raise your concerns about:"
    await mess.answer(hello_text, reply_markup=kb_eng)


@dp.message_handler(text='Options ⚙️')  # Создаём message handler который ловит команду /menu
async def lang(message: Message, state: FSMContext):  # Создаём асинхронную функцию
    await message.answer("Select language!", reply_markup=lang_btn)
    await state.finish()


@dp.message_handler(text='Bribery and corruption.')  # Создаём message handler который ловит команду /menu
async def poraxor(message: Message):  # Создаём асинхронную функцию
    mes_text = "Please specify what exactly is the violation:"
    await message.answer(mes_text, reply_markup=corrupt)
    await select_lang.cor.set()


@dp.message_handler(state=select_lang.cor)
async def send_mail(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Please leave your message\n\nℹ️ If you would like to receive a response to your application, please indicate your full name and provide contact information (your email address or telephone number)', reply_markup=kb_eng)
    await state.finish()
    await select_lang.cor1.set()

    @dp.message_handler(state=select_lang.cor1)
    async def send_mail(mess: Message, state: FSMContext):
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
        ans_text = "Your message has been sent."
        await mess.answer(ans_text, reply_markup=kb_eng)


@dp.message_handler(text='Accounting violations.')  # Создаём message handler который ловит команду /menu
async def viol1(message: Message):  # Создаём асинхронную функцию
    mes_text = "Please specify what exactly is the violation:"
    await message.answer(mes_text, reply_markup=viol)
    await select_lang.viol.set()


@dp.message_handler(state=select_lang.viol)
async def send_mail(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Please leave your message\n\nℹ️ If you would like to receive a response to your application, please indicate your full name and provide contact information (your email address or telephone number)', reply_markup=kb_eng)
    await state.finish()
    await select_lang.viol1.set()

    @dp.message_handler(state=select_lang.viol1)
    async def send_mail(mess: Message, state: FSMContext):
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
        ans_text = "Your message has been sent."
        await mess.answer(ans_text, reply_markup=kb_eng)


@dp.message_handler(
    text='Unequal employment and working conditions.')  # Создаём message handler который ловит команду /menu
async def unequal1(message: Message):  # Создаём асинхронную функцию
    mes_text = "Please specify what exactly is the violation:"
    await message.answer(mes_text, reply_markup=unequal)
    await select_lang.unequal.set()


@dp.message_handler(state=select_lang.unequal)
async def send_mail(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Please leave your message\n\nℹ️ If you would like to receive a response to your application, please indicate your full name and provide contact information (your email address or telephone number)', reply_markup=kb_eng)
    await state.finish()
    await select_lang.unequal1.set()

    @dp.message_handler(state=select_lang.unequal1)
    async def send_mail(mess: Message, state: FSMContext):
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
        ans_text = "Your message has been sent."
        await mess.answer(ans_text, reply_markup=kb_eng)


@dp.message_handler(
    text='Threats to health, safety and the environment.')  # Создаём message handler который ловит команду /menu
async def health1(message: Message):  # Создаём асинхронную функцию
    mes_text = "Please specify what exactly is the violation:"
    await message.answer(mes_text, reply_markup=health)
    await select_lang.health.set()


@dp.message_handler(state=select_lang.health)
async def send_mail(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Please leave your message\n\nℹ️ If you would like to receive a response to your application, please indicate your full name and provide contact information (your email address or telephone number)', reply_markup=kb_eng)
    await state.finish()
    await select_lang.health1.set()

    @dp.message_handler(state=select_lang.health1)
    async def send_mail(mess: Message, state: FSMContext):
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
        ans_text = "Your message has been sent."
        await mess.answer(ans_text, reply_markup=kb_eng)


@dp.message_handler(text='Leakage/destruction of information.')  # Создаём message handler который ловит команду /menu
async def sbt1(message: Message):  # Создаём асинхронную функцию
    mes_text = "Please specify what exactly is the violation:"
    await message.answer(mes_text, reply_markup=leakage)
    await select_lang.leakage.set()


@dp.message_handler(state=select_lang.leakage)
async def send_mail(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Please leave your message\n\nℹ️ If you would like to receive a response to your application, please indicate your full name and provide contact information (your email address or telephone number)', reply_markup=kb_eng)
    await state.finish()
    await select_lang.leakage1.set()

    @dp.message_handler(state=select_lang.leakage1)
    async def send_mail(mess: Message, state: FSMContext):
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
        ans_text = "Your message has been sent."
        await mess.answer(ans_text, reply_markup=kb_eng)


@dp.message_handler(text='Other.')  # Создаём message handler который ловит команду /menu
async def lang(message: Message):  # Создаём асинхронную функцию
    sub = message.text
    mes_text = 'Please leave your message\n\nℹ️ If you would like to receive a response to your application, please indicate your full name and provide contact information (your email address or telephone number)'
    await message.answer(mes_text, reply_markup=kb_eng)
    await select_lang.other.set()

    @dp.message_handler(state=select_lang.other)
    async def send_mail(mess: Message, state: FSMContext):
        send_text = mess.text
        sender = "compliance1@uzbeksteel.uz"
        password = '$COMPL11'
        await state.finish()
        server = smtplib.SMTP("10.3.1.33", 587)
        server.starttls()
        server.login(sender, password)
        msg = MIMEText(send_text)
        msg['Subject'] = sub
        server.sendmail(sender, 'compliance7@uzbeksteel.uz', msg.as_string())
        server.sendmail(sender, 'a.abdullayev@uzbeksteel.uz', msg.as_string())
        ans_text = "Your message has been sent."
        await mess.answer(ans_text, reply_markup=kb_eng)
