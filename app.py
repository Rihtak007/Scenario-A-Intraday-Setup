from flask import Flask
from trade_logic import get_trade_signal
from telegram import send_telegram_message

app = Flask(__name__)

@app.route('/')
def home():
    return "📡 Scenario A Bot is Live!"

@app.route('/send')
def send_trade():
    signal = get_trade_signal()
    if signal:
        send_telegram_message(signal)
        return "✅ Trade alert sent to Telegram"
    return "❌ No valid trade setup found"
