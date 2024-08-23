import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import yfinance as yf

# Streamlit app setup
st.title("Stock Market Analysis Dashboard")

# User input for stock symbol and date range
symbol = st.text_input("Enter Stock Symbol", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime('2023-01-01'))
end_date = st.date_input("End Date", pd.to_datetime('2023-12-31'))

# Fetch stock data
@st.cache_data
def load_data(symbol, start, end):
    df = yf.download(symbol, start=start, end=end)
    return df

df = load_data(symbol, start_date, end_date)

if df.empty:
    st.error("No data found for the symbol.")
else:
    st.write(f"Showing data for {symbol} from {start_date} to {end_date}")

    # Calculate moving averages
    window_size = st.slider("Select Moving Average Window", min_value=5, max_value=50, value=20)
    df[f'{window_size}_SMA'] = df['Close'].rolling(window=window_size).mean()

    # Plotting
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))
    fig.add_trace(go.Scatter(x=df.index, y=df[f'{window_size}_SMA'], mode='lines', name=f'{window_size}-SMA'))

    fig.update_layout(title=f'{symbol} Stock Price and Moving Averages',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      template='plotly_dark')

    st.plotly_chart(fig)
