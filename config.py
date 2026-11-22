# config.py — Модуль для конфигурации и инициализации бота.
# Здесь мы загружаем токен и создаем самого бота, чтобы другие файлы могли к нему обращаться.

import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("MY_TOKEN")