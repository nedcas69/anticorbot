from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Poraxo\'rlik va korruptsiya.'),
        ],
        [
            KeyboardButton('Buxgalteriya hisobini buzish.'),
        ],
        [
            KeyboardButton('Tengsiz bandlik va mehnat sharoitlari.'),
        ],
        [
            KeyboardButton('Salomatlik, xavfsizlik va atrof-muhitga tahdidlar.'),
        ],
        [
            KeyboardButton('Axborotning chiqib ketishi/yo\'q qilinishi.'),
        ],
        [
            KeyboardButton('Boshqalar.'),
            KeyboardButton('Sozlamalar ⚙️'),
        ],

    ],
    resize_keyboard=True
)
pora = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Pora berish/olish.'),
            KeyboardButton('Noqonuniy mukofot.'),
        ],
        [
            KeyboardButton('Firibgarlik.'),
            KeyboardButton('Til biriktirish.'),
        ],
        [
            KeyboardButton('Majburlash.'),
            KeyboardButton('Boshqalar.'),
        ],
        [
            KeyboardButton('Hokimiyatni suiiste\'mol qilish.'),
        ],

    ],
    resize_keyboard=True
)
buxgal = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Buxgalteriya hisobidagi xatolar.'),
        ],
        [
            KeyboardButton('Buxgalteriya hisobini xato ko\'rsatish.'),
        ],
        [
            KeyboardButton('Moliyaviy kamchiliklar.'),
        ],
        [
            KeyboardButton('Yozuvlar va hujjatlarni manipulyatsiya qilish, qalbakilashtirish.'),
        ],
        [
            KeyboardButton('Aktivlarni ruxsatsiz sotib olish, tasarruf etish va/yoki ulardan foydalanish.'),
        ],
        [
            KeyboardButton('Boshqalar.'),
        ],

    ],
    resize_keyboard=True
)
tengsiz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Kamsitish yoki ta\'qib qilish.'),
        ],
        [
            KeyboardButton('Mehnat ziddiyatlari.'),
        ],
        [
            KeyboardButton('Bezorilik.'),
        ],
        [
            KeyboardButton('Axloqsiz xatti-harakatlar.'),
        ],
        [
            KeyboardButton('Yaqin qarindoshlar va qaynona-qaynotalarni ishga joylashtirish.'),
        ],
        [
            KeyboardButton('Boshqalar.'),
        ],

    ],
    resize_keyboard=True
)
tb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Atrof muhitga zarar yetkazish.'),
        ],
        [
            KeyboardButton('Mulkka zarar yetkazish.'),
        ],
        [
            KeyboardButton('Xavfli ish sharoitlari.'),
        ],
        [
            KeyboardButton('O\'g\'irlik.'),
        ],
        [
            KeyboardButton('Hayot va sog\'liq uchun jiddiy va aniq xavf tug\'diradigan ehtiyotsizlik.'),
        ],
        [
            KeyboardButton('Harakat xavfsizligi.'),
        ],

    ],
    resize_keyboard=True
)
sb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('maxfiy va insayder ma\'lumotlarini ruxsatsiz oshkor qilish.'),
        ],
        [
            KeyboardButton('hujjatlar va ma\'lumotlarni ruxsatsiz va qasddan yo\'q qilish yoki yo\'q qilish.'),
        ],
        [
            KeyboardButton('Boshqalar.'),
        ],
    ],
    resize_keyboard=True
)
