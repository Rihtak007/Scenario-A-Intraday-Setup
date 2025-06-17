def is_pivot_breakout(df):
    try:
        if len(df) < 2:
            return False
        prev = df.iloc[-2]
        pivot = (prev['high'] + prev['low'] + prev['close']) / 3
        today_high = float(df['high'].iloc[-1])
        return bool(today_high > pivot)
    except Exception as e:
        print("❌ Error in is_pivot_breakout:", e)
        return False

def check_volume_surge(df, factor=1.5):
    try:
        if len(df) < 11:
            return False
        avg_vol = float(df['volume'].iloc[-11:-1].mean())
        current_vol = float(df['volume'].iloc[-1])
        return bool(current_vol > avg_vol * factor)
    except Exception as e:
        print("❌ Error in check_volume_surge:", e)
        return False

def check_momentum(df):
    try:
        if 'close' not in df.columns or len(df) < 15:
            return False
        delta = df['close'].diff()
        gain = delta.where(delta > 0, 0).rolling(14).mean()
        loss = -delta.where(delta < 0, 0).rolling(14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        latest_rsi = float(rsi.iloc[-1]) if not rsi.empty else 0
        return bool(latest_rsi > 60)
    except Exception as e:
        print("❌ Error in check_momentum:", e)
        return False
