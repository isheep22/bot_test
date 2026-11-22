import asyncio
from vkbottle import Bot
from config import BOT_TOKEN
from utils.logger import logger

# Импортируем только те обработчики, которые у тебя реально есть
from handlers import start, echo

async def main():
    """Основная функция запуска бота"""

    # Создаём бота
    bot = Bot(token=BOT_TOKEN)

    logger.info("🚀 Запуск бота...")
    # Можно оставить вывод токена для проверки, но лучше его скрыть в продакшене
    logger.info(f"Token: {BOT_TOKEN[:20]}...")

    # ==========================================
    # ОЧЕРЕДЬ ВЫЗОВА ОБРАБОТЧИКОВ (СВЕРХУ ВНИЗ)
    # ==========================================
    
    # 1. Первым проверяем конкретные команды (твоя команда "время")
    await start.register_handlers(bot)
    
    # 2. Эхо всегда должно быть ПОСЛЕДНИМ, так как оно ловит всё подряд
    await echo.register_handlers(bot)
    
    # ==========================================

    logger.info("✅ Все обработчики зарегистрированы")
    logger.info("🤖 Бот запущен и слушает сообщения...")

    # Запускаем бота
    await bot.run_polling()

if __name__ == "__main__":
    asyncio.run(main())