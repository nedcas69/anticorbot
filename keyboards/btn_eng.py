from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Bribery and corruption.'),
        ],
        [
            KeyboardButton('Accounting violations.'),
        ],
        [
            KeyboardButton('Unequal employment and working conditions.'),
        ],
        [
            KeyboardButton('Threats to health, safety and the environment.'),
        ],
        [
            KeyboardButton('Leakage/destruction of information.'),
        ],
        [
            KeyboardButton('Other.'),
        ],
        [
            KeyboardButton('Options ⚙️'),
        ],
    ],
    resize_keyboard=True
)
corrupt = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('giving/receiving a bribe.'),
            KeyboardButton('fraud.'),
        ],
        [
            KeyboardButton('illegal reward.'),
            KeyboardButton('collusion.'),
        ],
        [
            KeyboardButton('compulsion.'),
            KeyboardButton('Other.'),
        ],
        [
            KeyboardButton('abuse of power.'),
        ],

    ],
    resize_keyboard=True
)
viol = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('errors in accounting.'),
        ],
        [
            KeyboardButton('accounting misstatements.'),
        ],
        [
            KeyboardButton('financial omissions.'),
        ],
        [
            KeyboardButton('manipulation, falsification of records and documents.'),
        ],
        [
            KeyboardButton('unauthorized acquisition, disposal and/or use of assets.'),
        ],
        [
            KeyboardButton('Other.'),
        ],

    ],
    resize_keyboard=True
)
unequal = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('discrimination or harassment.'),
        ],
        [
            KeyboardButton('labor conflicts.'),
        ],
        [
            KeyboardButton('harassment.'),
        ],
        [
            KeyboardButton('unethical behaviour.'),
        ],
        [
            KeyboardButton('employment of close relatives and in-laws.'),
        ],
        [
            KeyboardButton('Other.'),
        ],

    ],
    resize_keyboard=True
)
health = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('environmental damage.'),
        ],
        [
            KeyboardButton('damage to property.'),
        ],
        [
            KeyboardButton('unsafe working conditions.'),
        ],
        [
            KeyboardButton('theft.'),
        ],
        [
            KeyboardButton('negligence causing significant and definite danger to life and health.'),
        ],
        [
            KeyboardButton('movement safety.'),
        ],

    ],
    resize_keyboard=True
)
leakage = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('unauthorized disclosure of confidential and insider information.'),
        ],
        [
            KeyboardButton('unauthorized and deliberate destruction or deletion of documents and information.'),
        ],
        [
            KeyboardButton('Other.'),
        ],
    ],
    resize_keyboard=True
)
