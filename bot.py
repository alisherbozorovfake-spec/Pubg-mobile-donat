import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import BOT_TOKEN
from keyboards import main_menu, wallet_menu
from data import UC_PRICES, USER_BALANCE

bot = Bot(8422117515:AAGuo_z5ml58vtXRblbpg2leTqWk6Zt_Ayo)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id not in USER_BALANCE:
        USER_BALANCE[user_id] = 0

    await message.answer(
        "🎮 PUBG Mobile UC botiga xush kelibsiz!",
        reply_markup=main_menu
    )

@dp.message(lambda msg: msg.text == "💰 Hamyon")
async def wallet(message: types.Message):
    balance = USER_BALANCE.get(message.from_user.id, 0)
    await message.answer(
        f"💰 Sizning balansingiz: {balance} so‘m",
        reply_markup=wallet_menu
    )

@dp.message(lambda msg: msg.text == "🛒 Xaridlar")
async def purchases(message: types.Message):
    text = "🛒 PUBG Mobile UC narxlari:\n\n"
    for uc, price in UC_PRICES.items():
        text += f"🔹 {uc} — {price:,} so‘m\n"

    text += "\n❗️ Xarid qilish funksiyasi ishlab chiqilmoqda"
    await message.answer(text)

@dp.message(lambda msg: msg.text == "⬅️ Orqaga")
async def back(message: types.Message):
    await message.answer("Asosiy menyu", reply_markup=main_menu)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
@dp.message(lambda msg: msg.text in UC_PACKS)
async def select_uc(message: types.Message):
    user_id = message.from_user.id
    uc = message.text
    price = UC_PACKS[uc]

    ORDERS[user_id] = {
        "uc": uc,
        "price": price,
        "pubg_id": None,
        "paid": False
    }

    await message.answer(
        f"🎮 {uc} tanlandi\n"
        f"💰 Narx: {price} so‘m\n\n"
        "📩 PUBG ID yuboring:"
    )
@dp.message(lambda msg: msg.text in UC_PACKS)
async def select_uc(message: types.Message):
    user_id = message.from_user.id
    uc = message.text
    price = UC_PACKS[uc]

    ORDERS[user_id] = {
        "uc": uc,
        "price": price,
        "pubg_id": None,
        "paid": False
    }

    await message.answer(
        f"🎮 {uc} tanlandi\n"
        f"💰 Narx: {price} so‘m\n\n"
        "📩 PUBG ID yuboring:"
    )

# 👇 AYNAN SHU JOYGA QO‘YASAN
@dp.message(
    lambda msg: msg.from_user.id in ORDERS
    and ORDERS[msg.from_user.id]["pubg_id"] is None
)
async def get_pubg_id(message: types.Message):
    user_id = message.from_user.id
    pubg_id = message.text.strip()

    if not pubg_id.isdigit():
        await message.answer("❌ PUBG ID faqat raqam bo‘lishi kerak")
        return

    ORDERS[user_id]["pubg_id"] = pubg_id

    order = ORDERS[user_id]
    tx_id = f"UC{user_id}"

    pay_url = generate_click_url(
        order["price"],
        tx_id,
        CLICK_SERVICE_ID,
        CLICK_MERCHANT_ID
    )

    await message.answer(
        "✅ Buyurtma tayyor!\n\n"
        f"🎮 PUBG ID: {pubg_id}\n"
        f"📦 Paket: {order['uc']}\n"
        f"💰 Narx: {order['price']} so‘m\n\n"
        f"💳 To‘lov qilish:\n{pay_url}"
)
