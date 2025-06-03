import os
from datetime import datetime
import pytz
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from feeds import get_feed_articles
from translate import translate_to_uzbek
from admin_panel import *

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bu yangiliklar botidir.")

async def fetch_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return await update.message.reply_text("Siz admin emassiz.")

    articles = get_feed_articles(get_feeds())

    tz = pytz.timezone("Asia/Tashkent")
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    for article in articles:
        text = f"📰 {article['title']}\n\n{article['summary']}\n\n🔗 {article['link']}"
        translated = translate_to_uzbek(text)
        final_text = f"{translated}\n\n🕒 Yangilik vaqti: {now}"
        await context.bot.send_message(chat_id=get_channel(), text=final_text)

async def addsource(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if not context.args:
        return await update.message.reply_text("URL kiriting.")
    url = context.args[0]
    result = add_feed(url)
    await update.message.reply_text(result)

async def removesource(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if not context.args:
        return await update.message.reply_text("URL kiriting.")
    url = context.args[0]
    result = remove_feed(url)
    await update.message.reply_text(result)

async def setchannel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if not context.args:
        return await update.message.reply_text("Kanal username kiriting.")
    username = context.args[0]
    result = set_channel(username)
    await update.message.reply_text(result)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("fetch", fetch_news))
app.add_handler(CommandHandler("addsource", addsource))
app.add_handler(CommandHandler("removesource", removesource))
app.add_handler(CommandHandler("setchannel", setchannel))

app.run_polling()
