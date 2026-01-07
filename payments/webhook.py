from fastapi import FastAPI, Request
from data import ORDERS
from aiogram import Bot
from config import BOT_TOKEN

app = FastAPI()
bot = Bot(BOT_TOKEN)

@app.post("/click/webhook")
async def click_webhook(request: Request):
    data = await request.form()

    tx_id = data.get("merchant_trans_id")
    status = data.get("error")

    if status == "0":
        user_id = int(tx_id.replace("UC", ""))

        if user_id in ORDERS:
            ORDERS[user_id]["paid"] = True

            await bot.send_message(
                user_id,
                "✅ To‘lov qabul qilindi!\n"
                "⏳ UC tez orada tashlanadi"
            )

        return {"error": 0, "error_note": "Success"}

    return {"error": -1, "error_note": "Payment failed"}
