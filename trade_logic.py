import pandas as pd
import yfinance as yf
from utils import is_pivot_breakout, check_volume_surge, check_momentum
from datetime import datetime

def get_trade_signal():
    try:
        stocks_df = pd.read_csv("stocks_list.csv")
    except FileNotFoundError:
        return "❌ stocks_list.csv not found."

    now = datetime.now()
    if now.hour < 9 or (now.hour == 9 and now.minute < 20):
        return "⏳ Waiting for 9:20 AM filter to pass."

    for symbol in stocks_df["Symbol"]:
        yahoo_symbol = symbol + ".NS"
        data = yf.download(yahoo_symbol, period="15d", interval="1d", progress=False)

        if data.empty or len(data) < 2:
            continue

        df = data.reset_index()
        df.rename(columns={"Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume": "volume"}, inplace=True)

        if is_pivot_breakout(df) and check_volume_surge(df) and check_momentum(df):
            entry = round(df.iloc[-1]["close"], 2)
            sl = round(entry * 0.99, 2)
            target = round(entry * 1.02, 2)
            return f"📈 *Scenario A Breakout Trade*\nStock: {symbol}\nEntry: ₹{entry}\nTarget: ₹{target}\nStop Loss: ₹{sl}\nTime: {now.strftime('%I:%M %p')}\nExit: Intraday or 3:15 PM"
    return "❌ No valid breakout setup found."
