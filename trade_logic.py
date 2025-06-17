import pandas as pd
import yfinance as yf
from utils import is_pivot_breakout, check_volume_surge, check_momentum
from datetime import datetime

def get_trade_signal():
    try:
        stocks_df = pd.read_csv("stocks_list.csv")
    except FileNotFoundError:
        return "❌ stocks_list.csv not found."

    # Time check: run only after 9:20 AM
    now = datetime.now()
    if now.hour < 9 or (now.hour == 9 and now.minute < 20):
        return "⏳ Waiting until after 9:20 AM to scan breakouts."

    for symbol in stocks_df["Symbol"]:
        try:
            yahoo_symbol = symbol + ".NS"
            print(f"🔍 Checking {symbol}...")

            data = yf.download(yahoo_symbol, period="15d", interval="1d", progress=False, auto_adjust=False)
            if data.empty or len(data) < 2:
                print(f"⚠️ Not enough data for {symbol}")
                continue

            df = data.reset_index()
            df.rename(columns={
                "Open": "open", "High": "high", "Low": "low",
                "Close": "close", "Volume": "volume"
            }, inplace=True)

            if is_pivot_breakout(df) and check_volume_surge(df) and check_momentum(df):
                entry_price = round(df.iloc[-1]["close"], 2)
                stop_loss = round(entry_price * 0.99, 2)
                target = round(entry_price * 1.02, 2)

                return f"""📈 *Scenario A Breakout Trade*
Stock: {symbol}
Entry: ₹{entry_price}
Target: ₹{target}
Stop Loss: ₹{stop_loss}
Time: {now.strftime('%I:%M %p')}
Exit: Intraday or 3:15 PM"""

        except Exception as e:
            print(f"❌ Error checking {symbol}: {e}")
            continue

    return "❌ No valid breakout setup found today."
