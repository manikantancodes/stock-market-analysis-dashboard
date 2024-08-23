# stock_dashboard.py

import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import yfinance as yf
from stock_analysis import load_data, calculate_moving_averages, calculate_bollinger_bands, calculate_rsi, calculate_macd

# Streamlit app setup
st.title("Stock Market Analysis Dashboard")

# User input for stock symbol and date range
symbol = st.text_input("Enter Stock Symbol", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime('2023-01-01'))
end_date = st.date_input("End Date", pd.to_datetime('2023-12-31'))

# Fetch stock data
df = load_data(symbol, start_date, end_date)

if df.empty:
    st.error("No data found for the symbol.")
else:
    st.write(f"Showing data for {symbol} from {start_date} to {end_date}")

    # Calculate and display moving averages
    window_size = st.slider("Select Moving Average Window", min_value=5, max_value=50, value=20)
    df[f'{window_size}_SMA'] = calculate_moving_averages(df, window_size)

    # Plotting
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))
    fig.add_trace(go.Scatter(x=df.index, y=df[f'{window_size}_SMA'], mode='lines', name=f'{window_size}-SMA'))

    fig.update_layout(title=f'{symbol} Stock Price and Moving Averages',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      template='plotly_dark')

    st.plotly_chart(fig)

    # Calculate and plot Bollinger Bands
    df = calculate_bollinger_bands(df)
    fig_bollinger = go.Figure()
    fig_bollinger.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))
    fig_bollinger.add_trace(go.Scatter(x=df.index, y=df['Upper Band'], mode='lines', name='Upper Bollinger Band'))
    fig_bollinger.add_trace(go.Scatter(x=df.index, y=df['Lower Band'], mode='lines', name='Lower Bollinger Band'))

    fig_bollinger.update_layout(title=f'{symbol} Bollinger Bands',
                                xaxis_title='Date',
                                yaxis_title='Price',
                                template='plotly_dark')

    st.plotly_chart(fig_bollinger)

    # Calculate and plot RSI
    df['RSI'] = calculate_rsi(df)
    fig_rsi = go.Figure()
    fig_rsi.add_trace(go.Scatter(x=df.index, y=df['RSI'], mode='lines', name='RSI'))
    fig_rsi.update_layout(title=f'{symbol} RSI',
                          xaxis_title='Date',
                          yaxis_title='RSI',
                          template='plotly_dark')

    st.plotly_chart(fig_rsi)

    # Calculate and plot MACD
    df = calculate_macd(df)
    fig_macd = go.Figure()
    fig_macd.add_trace(go.Scatter(x=df.index, y=df['MACD'], mode='lines', name='MACD'))
    fig_macd.add_trace(go.Scatter(x=df.index, y=df['Signal Line'], mode='lines', name='Signal Line'))
    fig_macd.update_layout(title=f'{symbol} MACD',
                           xaxis_title='Date',
                           yaxis_title='MACD',
                           template='plotly_dark')

    st.plotly_chart(fig_macd)
