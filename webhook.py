import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiohttp import web
import asyncio
import os

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("🌊 CaspianCoin — Xəzər dənizindən ilhamlanan, yerli və dayanıqlı rəqəmsal valyuta.")

async def handle(request):
    try:
        data = await request.json()
        update = types.Update(**data)
        await dp.feed_update(bot, update)
        return web.Response(text="OK")
    except Exception as e:
        logging.exception("Xəta baş verdi:")
        return web.Response(status=500, text="Xəta")

app = web.Application()
app.router.add_post("/", handle)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))