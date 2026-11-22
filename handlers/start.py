# handlers/start.py — Модуль для конкретных команд (в твоем случае "время").
# Здесь мы ловим сообщение "время" и отвечаем.

from vkbottle.bot import Message, Bot
import bot_text

async def register_handlers(bot: Bot):
    @bot.on.message(text=["время", "йоу", "пока"])
    async def time_handler(message: Message):
        await message.answer(bot_text.TIME_RESPONSE)