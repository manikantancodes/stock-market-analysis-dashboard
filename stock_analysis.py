# stock_analysis.py

import yfinance as yf
import pandas as pd

# Function to fetch stock data
def load_data(symbol, start, end):
    df = yf.download(symbol, start=start, end=end)
    return df

# Function to calculate moving averages
def calculate_moving_averages(df, window_size):
    return df['Close'].rolling(window=window_size).mean()

# Function to calculate Bollinger Bands
def calculate_bollinger_bands(df):
    df['20_SMA'] = df['Close'].rolling(window=20).mean()
    df['stddev'] = df['Close'].rolling(window=20).std()
    df['Upper Band'] = df['20_SMA'] + (df['stddev'] * 2)
    df['Lower Band'] = df['20_SMA'] - (df['stddev'] * 2)
    return df

# Function to calculate RSI
def calculate_rsi(df, window=14):
    delta = df['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    RS = gain / loss
    RSI = 100 - (100 / (1 + RS))
    return RSI

# Function to calculate MACD
def calculate_macd(df):
    df['12_EMA'] = df['Close'].ewm(span=12, adjust=False).mean()
    df['26_EMA'] = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = df['12_EMA'] - df['26_EMA']
    df['Signal Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
    return df
