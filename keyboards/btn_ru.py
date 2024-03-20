from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Взяточничество и коррупция.'),
        ],
        [
            KeyboardButton('Нарушения бухгалтерского учета.'),
        ],
        [
            KeyboardButton('Неравные условия найма и труда.'),
        ],
        [
            KeyboardButton('Угроза здоровью, безопасности и окружающей среде.'),
        ],
        [
            KeyboardButton('Утечка/ уничтожение информации.'),
        ],
        [
            KeyboardButton('Другое.'),
        ],
        [
            KeyboardButton('Настройки ⚙️'),
        ],

    ],
    resize_keyboard=True
)
kor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('дача/ получение взятки.'),
        ],
        [
            KeyboardButton('незаконное вознаграждение.'),
        ],
        [
            KeyboardButton('мошенничество.'),
        ],
        [
            KeyboardButton('сговор.'),
        ],
        [
            KeyboardButton('принуждение.'),
        ],
        [
            KeyboardButton('злоупотребление должностными полномочиями.'),
        ],
        [
            KeyboardButton('Другое. '),
        ],

    ],
    resize_keyboard=True
)
buh = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('ошибки в бухгалтерском учете.'),
        ],
        [
            KeyboardButton('искажения в бухгалтерском учете.'),
        ],
        [
            KeyboardButton('финансовые упущения.'),
        ],
        [
            KeyboardButton('манипуляция, фальсификация записей и документов.'),
        ],
        [
            KeyboardButton('несанкционированное приобретение, списание и/ или использование активов.'),
        ],
        [
            KeyboardButton('Другое.  '),
        ],

    ],
    resize_keyboard=True
)
nerav = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('дискриминация или преследование.'),
        ],
        [
            KeyboardButton('трудовые конфликты.'),
        ],
        [
            KeyboardButton('домогательства.'),
        ],
        [
            KeyboardButton('неэтичное поведение.'),
        ],
        [
            KeyboardButton('устройство на работу близких родственников и свойственников.'),
        ],
        [
            KeyboardButton('Другое.   '),
        ],

    ],
    resize_keyboard=True
)
ot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('ущерб окружающей среде.'),
        ],
        [
            KeyboardButton('вред имуществу.'),
        ],
        [
            KeyboardButton('небезопасные условия работы.'),
        ],
        [
            KeyboardButton('кража.'),
        ],
        [
            KeyboardButton('халатность, вызывающая существенную и определенную опасность для жизни и здоровья.'),
        ],
        [
            KeyboardButton('безопасность движения.'),
        ],

    ],
    resize_keyboard=True
)
sbot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('несанкционированное раскрытие конфиденциальной и инсайдерской информации.'),
        ],
        [
            KeyboardButton('несанкционированное и преднамеренное уничтожение или удаление документов и информации.'),
        ],
        [
            KeyboardButton('Другое.    '),
        ],

    ],
    resize_keyboard=True
)