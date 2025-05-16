
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

TOKEN = "7854402795:AAFg8GeRHgi8OBuxxfsBUe5FnUpe7ZZ2pvk"
bot = Bot(token=TOKEN)

app = Flask(__name__)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0)

def calculate_bill(kwh):
    tiers = [
        {"from": 1, "to": 400, "price": 72},
        {"from": 401, "to": 800, "price": 108},
        {"from": 801, "to": 1200, "price": 175},
        {"from": 1201, "to": 1600, "price": 265},
        {"from": 1601, "to": float('inf'), "price": 350}
    ]
    total = 0
    for tier in tiers:
        if kwh > tier["to"]:
            total += (tier["to"] - tier["from"] + 1) * tier["price"]
        elif kwh >= tier["from"]:
            total += (kwh - tier["from"] + 1) * tier["price"]
            break
    return total

def start(update: Update, context):
    update.message.reply_text("👋 أهلاً! أرسل عدد الكيلوات وسأحسب لك الفاتورة.")

def handle(update: Update, context):
    try:
        kwh = int(update.message.text)
        if kwh < 1: raise ValueError
        bill = calculate_bill(kwh)
        update.message.reply_text(f"💡 الاستهلاك: {kwh} ك.و\n💰 الفاتورة: {bill:,} دينار")
    except:
        update.message.reply_text("🚫 أرسل رقمًا صحيحًا (مثال: 1250)")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "💡 البوت جاهز!"

if __name__ == "__main__":
    app.run()
