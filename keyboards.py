from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💰 Hamyon"), KeyboardButton(text="🛒 Xaridlar")],
    ],
    resize_keyboard=True
)

wallet_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Balans to‘ldirish")],
        [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)
