# handlers/echo.py — Модуль для "заглушки" (эхо-ответа).
# Этот обработчик без фильтров (@bot.on.message()). Он ловит 
# все остальные сообщения, которые не подошли под другие команды.

from vkbottle.bot import Message, Bot
import bot_text

async def register_handlers(bot: Bot):
    @bot.on.message()
    async def echo_handler(message: Message):
        text = (message.text or "").lower().strip()
        if text == "привет":
            await message.answer(bot_text.TIME_RESPONSE)
        else:            
            await message.answer(bot_text.DEFAULT_RESPONSE)