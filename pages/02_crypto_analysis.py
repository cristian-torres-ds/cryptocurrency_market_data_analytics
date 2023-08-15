import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
#import plotly.graph_objects as go
#import time as t
from pycoingecko import CoinGeckoAPI
#import seaborn as sns
#import matplotlib.pyplot as plt
import mplfinance as fplt
st.set_option('deprecation.showPyplotGlobalUse', False)


cg = CoinGeckoAPI()

ohlc_data = cg.get_coin_ohlc_by_id(id = 'monero', vs_currency = 'usd', days = '180')
ohlc_data_frame = pd.DataFrame(data = ohlc_data, columns = ['Date', 'Open', 'High' ,'Low', 'Close'])
ohlc_data_frame['Date'] = ohlc_data_frame['Date'].apply(lambda x: dt.datetime.fromtimestamp(x/1000).strftime('%m-%d-%Y %H:%M:%S'))
ohlc_data_frame['Date'] = pd.to_datetime(ohlc_data_frame['Date'])
ohlc_data_frame = ohlc_data_frame.set_index('Date')
ohlc_data_frame.head()

def wwma(values, n):
    """
     J. Welles Wilder's EMA 
    """
    return values.ewm(alpha=1/n, adjust=False).mean()

def atr(df, n=14):
    data = df.copy()
    high = data['High']
    low = data['Low']
    close = data['Close']
    data['tr0'] = abs(high - low)
    data['tr1'] = abs(high - close.shift())
    data['tr2'] = abs(low - close.shift())
    tr = data[['tr0', 'tr1', 'tr2']].max(axis=1)
    atr = wwma(tr, n)
    return atr


ohlc_data_frame['ATR'] = atr(ohlc_data_frame)


ohlc_data_frame['MA5'] = abs(ohlc_data_frame['Close'] - ohlc_data_frame['Open']).rolling(window = 5).mean()
ohlc_data_frame['MA15'] = abs(ohlc_data_frame['Close'] - ohlc_data_frame['Open']).rolling(window = 15).mean()
ohlc_data_frame['MA30'] = abs(ohlc_data_frame['Close'] - ohlc_data_frame['Open']).rolling(window = 30).mean()

ohlc_data_frame['change'] = ohlc_data_frame['Close'].diff()
ohlc_data_frame['gain'] = ohlc_data_frame.change.mask(ohlc_data_frame.change < 0, 0.0)
ohlc_data_frame['loss'] = -ohlc_data_frame.change.mask(ohlc_data_frame.change > 0, -0.0)

#@numba.jit
def rma(x, n):
    """Running moving average"""
    a = np.full_like(x, np.nan)
    a[n] = x[1:n+1].mean()
    for i in range(n+1, len(x)):
        a[i] = (a[i-1] * (n - 1) + x[i]) / n
    return a

ohlc_data_frame['avg_gain'] = rma(ohlc_data_frame.gain.to_numpy(), 14)
ohlc_data_frame['avg_loss'] = rma(ohlc_data_frame.loss.to_numpy(), 14)

ohlc_data_frame['rs'] = ohlc_data_frame.avg_gain / ohlc_data_frame.avg_loss
ohlc_data_frame['RSI'] = 100 - (100 / (1 + ohlc_data_frame.rs))
ohlc_data_frame = ohlc_data_frame.drop(['change', 'gain', 'loss', 'avg_gain', 'avg_loss', 'rs'], axis=1)


atr = fplt.make_addplot(ohlc_data_frame["ATR"])

fig = fplt.plot(
            ohlc_data_frame,
            type='candle',
            addplot = atr,
            style='charles',
            title='Crypto, March - 2020',
            ylabel='Price ($)',
            )

st.pyplot(fig)