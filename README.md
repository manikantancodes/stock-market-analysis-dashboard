# Stock Market Analysis Dashboard

## Overview
This project provides a **Stock Market Analysis Dashboard** using **Streamlit**, **yFinance**, and **Plotly**. It allows users to visualize historical stock data, apply various technical indicators like Moving Averages, Bollinger Bands, RSI, and MACD, and forecast future stock prices using the ARIMA model.

### Key Features:
- **Interactive Stock Price Visualization**: Explore historical stock prices with dynamic date ranges and indicators.
- **Technical Indicators**: Includes Moving Averages, RSI (Relative Strength Index), MACD (Moving Average Convergence Divergence), and Bollinger Bands.
- **Forecasting**: Predict future stock prices using the ARIMA time series model.
- **Customizable Analysis**: Users can select moving average windows and visualize key market trends.

---

## Installation

### Prerequisites:
- Python 3.x
- Pip (Python package installer)
- Streamlit, Plotly, yFinance, and other Python libraries (detailed in `requirements.txt`)

### Steps to Install:
1. Clone the repository:
   ```bash
   git clone 
   cd stock-market-analysis-dashboard
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your **API Key** for Alpha Vantage in the `config.py` file:
   ```python
   API_KEY = 'YOUR_API_KEY'
   ```

---

## How to Use the App

1. **Run the Streamlit app**:
   ```bash
   streamlit run stock_dashboard.py
   ```

2. **Open the web browser**: Go to the URL displayed in your terminal (usually `http://localhost:8501`).

3. **Enter stock symbol and date range**: Provide a stock ticker (e.g., `AAPL` for Apple) and select the desired date range for analysis.

4. **Explore the data**:
   - View stock prices and different technical indicators.
   - Adjust the moving average window size using a slider.
   - Analyze Bollinger Bands, MACD, and RSI.
   - Predict future stock prices using the ARIMA model.

---

## Features Explained

- **Moving Averages (SMA)**: Smooth out short-term fluctuations to help identify trends. Supports both 20-day and 50-day SMAs by default.
- **Bollinger Bands**: Shows price volatility by plotting bands two standard deviations above and below a 20-period moving average.
- **RSI (Relative Strength Index)**: A momentum oscillator used to identify overbought or oversold conditions.
- **MACD**: Measures the difference between short-term and long-term exponential moving averages to indicate buy/sell signals.
- **ARIMA Model**: A time series forecasting model used for predicting future stock prices.

---

## Project Structure

```bash
stock-market-analysis-dashboard/
├── stock_dashboard.py      # Streamlit dashboard application
├── stock_analysis.py       # Stock data retrieval and technical indicator calculations
├── requirements.txt        # Required Python libraries
├── config.py               # API key configuration
└── README.md               # Project documentation
```

---

## API Key Setup

1. Go to [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and sign up for a free API key.
2. Add the API key to the `config.py` file:
   ```python
   API_KEY = 'YOUR_API_KEY'
   ```

---

## Technical Dependencies

This project requires the following libraries, which are automatically installed using `pip`:

- **Streamlit**: A Python web framework for creating interactive dashboards and applications.
- **yFinance**: A Python library to fetch historical market data from Yahoo Finance.
- **Plotly**: For creating interactive data visualizations.
- **Pandas**: To handle data manipulation and analysis.
- **Statsmodels**: For time series forecasting with ARIMA.
- **Matplotlib**: To plot stock prices for static analysis.

---

## Example Plots

### Stock Price with Moving Averages

### Bollinger Bands

### MACD and RSI
---

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## Acknowledgments
- **Alpha Vantage** for providing stock market data.
- **Yahoo Finance** for real-time stock data access.
- **Plotly and Streamlit** for enabling interactive data visualization and web apps.

---



