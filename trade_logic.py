import pandas as pd
import yfinance as yf
from utils import is_pivot_breakout, check_volume_surge, check_momentum
from datetime import datetime

from datetime import datetime

def get_trade_signal():
    now = datetime.now()
    return f"""📈 *Scenario A Breakout Trade [Test]*
Stock: TESTSTOCK
Entry: ₹123.45
Target: ₹126.90
Stop Loss: ₹121.00
Time: {now.strftime('%I:%M %p')}
Exit: Intraday or 3:15 PM"""
