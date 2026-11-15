import os
from dotenv import load_dotenv
from vkbottle import Bot
from vkbottle.bot import Message

load_dotenv()  # Загружаем секретные данные из файла .env

TOKEN = os.getenv("MY_TOKEN")  # Берём токен из окружения
bot = Bot(token=TOKEN)  # Создаём и авторизуем бота

  # Отправляем ответ


@bot.on.message(text="время")  # Реагируем на сообщение "Привет"
async def greeting_handler(message: Message):
    await message.answer("я так не умею")


@bot.on.message()  # Реагируем на сообщение "Привет"
async def greeting_handler(message: Message):
    await message.answer(b)
    
print("Запуск бота...")
bot.run()  # Запускаем бесконечную работу бота
