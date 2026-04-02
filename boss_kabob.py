import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- 1. BOT SOZLAMALARI ---
# BotFather bergan yangi tokenni shu yerga qo'ying:
API_TOKEN = '8684776752:AAFR-9G-uQE4W6VYzZu5a9VF22yN6BChABY' 

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- 2. KEYBOARDLAR (TUGMALAR) ---
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍴 Menyu")],
        [KeyboardButton(text="📞 Biz bilan aloqa"), KeyboardButton(text="📍 Manzil")]
    ],
    resize_keyboard=True
)

menu_detail = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌯 Lavash"), KeyboardButton(text="🍔 Burgerlar")],
        [KeyboardButton(text="🥙 Pita"), KeyboardButton(text="🌭 Hot-doglar")],
        [KeyboardButton(text="🍗 KFS"), KeyboardButton(text="🍟 Fri")],
        [KeyboardButton(text="☕️ Ichimliklar"), KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)

# --- 3. HANDLERLAR (BOT VAZIFALARI) ---

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Boss Kabob botiga xush kelibsiz! 😊", reply_markup=main_menu)

@dp.message(F.text == "🍴 Menyu")
async def show_menu(message: types.Message):
    await message.answer("Kategoriyani tanlang:", reply_markup=menu_detail)

@dp.message(F.text == "🌯 Lavash")
async def show_lavash(message: types.Message):
    text = (
        "🌯 **Lavash menyusi:**\n\n"
        "• Mol go'shtli — 35,000 so'm\n"
        "• Mol go'shtli sirli — 40,000 so'm\n"
        "• Mol go'shtli katta — 45,000 so'm\n"
        "• Tovuqli — 32,000 so'm\n"
        "• Pishloqli tovuqli — 36,000 so'm\n"
        "• Katta tovuqli — 38,000 so'm"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "🍔 Burgerlar")
async def show_burgers(message: types.Message):
    text = (
        "🍔 **Burgerlar:**\n\n"
        "• Burger mol go'shtli — 35,000 so'm\n"
        "• Chizburger — 39,000 so'm\n"
        "• Chiken burger — 30,000 so'm\n"
        "• Chiken chizburger — 34,000 so'm"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "🥙 Pita")
async def show_pita(message: types.Message):
    text = (
        "🥙 **Pita menyusi:**\n\n"
        "• Pita mol go'shtli — 35,000 so'm\n"
        "• Pita o'rtacha mol go'shtli — 40,000 so'm\n"
        "• Pita katta mol go'shtli — 45,000 so'm\n"
        "• Pita tovuqli — 30,000 so'm\n"
        "• Katta pita tovuqli — 38,000 so'm"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "🌭 Hot-doglar")
async def show_hotdogs(message: types.Message):
    text = (
        "🌭 **Hot-doglar:**\n\n"
        "• Hot-dog — 17,000 so'm\n"
        "• Big hot-dog — 22,000 so'm\n"
        "• Shashlik hot-dog — 28,000 so'm\n"
        "• Go'shtli hot-dog — 33,000 so'm\n"
        "• Tovuqli hot-dog — 28,000 so'm"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "🍟 Fri")
async def show_fri(message: types.Message):
    await message.answer("🍟 **Kartoshka Fri — 15,000 so'm**", parse_mode="Markdown")

@dp.message(F.text == "🍗 KFS")
async def show_kfs(message: types.Message):
    text = (
        "🍗 **KFS mahsulotlari:**\n\n"
        "• KFS — 70,000 so'm\n"
        "• KFS Kombo — 40,000 so'm"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "☕️ Ichimliklar")
async def show_drinks(message: types.Message):
    text = (
        "☕️ **Ichimliklar:**\n\n"
        "• Choy — 5,000 so'm\n"
        "• Bardak choy — 10,000 so'm\n"
        "• Kofe — 7,000 so'm"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "📍 Manzil")
async def send_location(message: types.Message):
    lat, lon = 40.105335, 65.373357
    await message.answer("📍 **Bizning manzilimiz:**\nBoss Kabob (Navoiy).")
    await bot.send_location(chat_id=message.chat.id, latitude=lat, longitude=lon)

@dp.message(F.text == "📞 Biz bilan aloqa")
async def contact_us(message: types.Message):
    contact_text = (
        "📞 **Buyurtma berish uchun telefonlar:**\n\n"
        "1. +998 97 970 43 03\n"
        "2. +998 99 584 53 32\n"
        "3. +998 87 001 80 10"
    )
    await message.answer(contact_text, parse_mode="Markdown")

@dp.message(F.text == "⬅️ Orqaga")
async def go_back(message: types.Message):
    await message.answer("Asosiy menyu:", reply_markup=main_menu)

# --- 4. ASOSIY ISHGA TUSHIRISH ---
async def main():
    print("Bot GitHub Actions-da ishlamoqda...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi")
