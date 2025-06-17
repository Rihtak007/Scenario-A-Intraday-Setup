def is_pivot_breakout(df):
    if len(df) < 2:
        return False
    prev = df.iloc[-2]
    pivot = (prev['high'] + prev['low'] + prev['close']) / 3
    today_high = float(df.iloc[-1]['high'])  # Ensure it's not a Series
    return bool(today_high > pivot)

def check_volume_surge(df, factor=1.5):
    if len(df) < 11:
        return False
    avg_vol = float(df['volume'].iloc[-11:-1].mean())
    curr_vol = float(df['volume'].iloc[-1])
    return bool(curr_vol > avg_vol * factor)

def check_momentum(df):
    if 'close' not in df.columns or len(df) < 15:
        return False
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0).rolling(14).mean()
    loss = -delta.where(delta < 0, 0).rolling(14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    latest_rsi = float(rsi.iloc[-1]) if not rsi.empty else 0
    return bool(latest_rsi > 60)
