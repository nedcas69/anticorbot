from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards import kb_ru, kor, buh, nerav, ot, sbot
from loader import dp
import smtplib
from email.mime.text import MIMEText
from state import select_lang
from keyboards import lang_btn  # Импортируем нашу клавиатуру


@dp.message_handler(text='Русский 🇷🇺')
async def uz(mess: Message):
    hello_text = "Ваше обращение очень важно для нас. Пожалуйста, выберите категорию нарушения, в связи с которым вы собираетесь выразить свою обеспокоенность:"
    await mess.answer(hello_text, reply_markup=kb_ru)


@dp.message_handler(text='Настройки ⚙️')  # Создаём message handler который ловит команду /menu
async def menu(message: Message, state: FSMContext):  # Создаём асинхронную функцию
    await message.answer("Выберите язык!", reply_markup=lang_btn)
    await state.finish()


@dp.message_handler(text='Взяточничество и коррупция.')  # Создаём message handler который ловит команду /menu
async def poraxor(message: Message):  # Создаём асинхронную функцию
    mes_text = "Пожалуйста, уточните, в чём именно состоит нарушение:"
    await message.answer(mes_text, reply_markup=kor)
    await select_lang.poraxor.set()


@dp.message_handler(state=select_lang.poraxor)
async def send_mail(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Пожалуйста, оставьте Ваше сообщение.\n\nℹ️ Если вы хотите получить ответ на вашу заявку, пожалуйста, укажите Ф.И.О и предоставьте контактную информацию (ваш адрес электронной почты или номер телефона', reply_markup=kb_ru)
    await state.finish()
    await select_lang.poraxor1.set()

    @dp.message_handler(state=select_lang.poraxor1)
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
        ans_text = "Ваше сообщение отправлено."
        await mess.answer(ans_text, reply_markup=kb_ru)


@dp.message_handler(text='Нарушения бухгалтерского учета.')  # Создаём message handler который ловит команду /menu
async def buxgalter(message: Message):  # Создаём асинхронную функцию
    mes_text = "Пожалуйста, уточните, в чём именно состоит нарушение:"
    await message.answer(mes_text, reply_markup=buh)
    await select_lang.buxgalter.set()


@dp.message_handler(state=select_lang.buxgalter)
async def send_mail(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Пожалуйста, оставьте Ваше сообщение.\n\nℹ️ Если вы хотите получить ответ на вашу заявку, пожалуйста, укажите Ф.И.О и предоставьте контактную информацию (ваш адрес электронной почты или номер телефона', reply_markup=kb_ru)
    await state.finish()
    await select_lang.buxgalter1.set()

    @dp.message_handler(state=select_lang.buxgalter1)
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
        ans_text = "Ваше сообщение отправлено."
        await mess.answer(ans_text, reply_markup=kb_ru)


@dp.message_handler(text='Неравные условия найма и труда.')  # Создаём message handler который ловит команду /menu
async def tengsizlik(message: Message):  # Создаём асинхронную функцию
    mes_text = "Пожалуйста, уточните, в чём именно состоит нарушение:"
    await message.answer(mes_text, reply_markup=nerav)
    await select_lang.nerav.set()


@dp.message_handler(state=select_lang.nerav)
async def send_mail(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Пожалуйста, оставьте Ваше сообщение.\n\nℹ️ Если вы хотите получить ответ на вашу заявку, пожалуйста, укажите Ф.И.О и предоставьте контактную информацию (ваш адрес электронной почты или номер телефона', reply_markup=kb_ru)
    await state.finish()
    await select_lang.nerav1.set()

    @dp.message_handler(state=select_lang.nerav1)
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
        ans_text = "Ваше сообщение отправлено."
        await mess.answer(ans_text, reply_markup=kb_ru)


@dp.message_handler(
    text='Угроза здоровью, безопасности и окружающей среде.')  # Создаём message handler который ловит команду /menu
async def tbs(message: Message):  # Создаём асинхронную функцию
    mes_text = "Пожалуйста, уточните, в чём именно состоит нарушение:"
    await message.answer(mes_text, reply_markup=ot)
    await select_lang.tbs.set()


@dp.message_handler(state=select_lang.tbs)
async def send_mail(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Пожалуйста, оставьте Ваше сообщение.\n\nℹ️ Если вы хотите получить ответ на вашу заявку, пожалуйста, укажите Ф.И.О и предоставьте контактную информацию (ваш адрес электронной почты или номер телефона', reply_markup=kb_ru)
    await state.finish()
    await select_lang.tbs1.set()

    @dp.message_handler(state=select_lang.tbs1)
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
        ans_text = "Ваше сообщение отправлено."
        await mess.answer(ans_text, reply_markup=kb_ru)


@dp.message_handler(text='Утечка/ уничтожение информации.')  # Создаём message handler который ловит команду /menu
async def sbt(message: Message):  # Создаём асинхронную функцию
    mes_text = "Пожалуйста, уточните, в чём именно состоит нарушение:"
    await message.answer(mes_text, reply_markup=sbot)
    await select_lang.sbt.set()


@dp.message_handler(state=select_lang.sbt)
async def send_mail(mess: Message, state: FSMContext):
    sub = mess.text
    await mess.answer('Пожалуйста, оставьте Ваше сообщение.\n\nℹ️ Если вы хотите получить ответ на вашу заявку, пожалуйста, укажите Ф.И.О и предоставьте контактную информацию (ваш адрес электронной почты или номер телефона', reply_markup=kb_ru)
    await state.finish()
    await select_lang.sbt1.set()

    @dp.message_handler(state=select_lang.sbt1)
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
        ans_text = "Ваше сообщение отправлено."
        await mess.answer(ans_text, reply_markup=kb_ru)


@dp.message_handler(text='Другое.')  # Создаём message handler который ловит команду /menu
async def lang(message: Message):  # Создаём асинхронную функцию
    sub = message.text
    mes_text = 'Пожалуйста, оставьте Ваше сообщение.\n\nℹ️ Если вы хотите получить ответ на вашу заявку, пожалуйста, укажите Ф.И.О и предоставьте контактную информацию (ваш адрес электронной почты или номер телефона'
    await message.answer(mes_text, reply_markup=kb_ru)
    await select_lang.drugoe.set()

    @dp.message_handler(state=select_lang.drugoe)
    async def send_mail(mess: Message, state: FSMContext):
        send_text = mess.text
        await state.finish()
        sender = "compliance1@uzbeksteel.uz"
        password = '$COMPL11'
        server = smtplib.SMTP("10.3.1.33", 587)
        server.starttls()

        server.login(sender, password)
        msg = MIMEText(send_text)
        msg['Subject'] = sub
        server.sendmail(sender, 'compliance7@uzbeksteel.uz', msg.as_string())
        server.sendmail(sender, 'a.abdullayev@uzbeksteel.uz', msg.as_string())

        ans_text = "Ваше сообщение отправлено."
        await mess.answer(ans_text, reply_markup=kb_ru)
