import ccxt
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize Binance client through ccxt
binance = ccxt.binance()

def fetch_data():
    since = binance.milliseconds() - 150 * 60 * 1000  # Last 150 minutes to cover 10 intervals of 15 minutes
    ohlcv = binance.fetch_ohlcv('BTC/USDT', '15m', since, 10)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df
fig, ax = plt.subplots()

def update(frame):
    df = fetch_data()
    ax.clear()
    mpf.plot(df, ax=ax, type='candle')
    plt.title('Live BTC/USDT Price')
    plt.xlabel('Time')
    plt.ylabel('Price (USDT)')

ani = FuncAnimation(fig, update, interval=0, save_count=100)  # Update every minute
plt.show()
