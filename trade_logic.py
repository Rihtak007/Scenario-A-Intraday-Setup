from datetime import datetime

def get_trade_signal():
    now = datetime.now()
    print("🔥 TEST get_trade_signal() called at", now)
    return f"""📈 *Test Breakout Trade*
Stock: TESTSTOCK
Entry: ₹123.45
Target: ₹126.90
Stop Loss: ₹121.00
Time: {now.strftime('%I:%M %p')}
Exit: Intraday or 3:15 PM"""
