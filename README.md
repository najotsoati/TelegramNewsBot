# 🇺🇿 Yangiliklar AI Telegram Bot

Bu bot avtomatik tarzda yangiliklarni RSS manbadan oladi, ularni o‘zbek tiliga tarjima qiladi va tanlangan Telegram kanalga yuboradi.

## 🔧 Xususiyatlar

- RSS yangilik manbalarni boshqarish (qo‘shish/o‘chirish)
- Yangiliklarni avtomatik tarjima qilish (OpenAI yordamida)
- Postlarni kanalga yuborish
- Admin panel (Telegram komandalar orqali)
- Soat zonasi: Asia/Tashkent

## ⚙️ Talablar

- Python 3.10 yoki undan yuqori
- Termux, Linux yoki server
- Telegram bot token
- OpenAI API kaliti

## 🛠 O‘rnatish

```bash
# Termux/Ubuntu:
pkg install python git -y
pip install --upgrade pip

# GitHub'dan yuklab oling
git clone https://github.com/najotsoati/news-bot.git
cd news-bot

# Virtual muhit (ixtiyoriy)
python -m venv venv
source venv/bin/activate

# Kutubxonalarni o‘rnatish
pip install -r requirements.txt
