import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


tickers = ['DIS', 'NFLX', 'CMCSA', 'SONY']  
start_date = '2019-01-01'
end_date = '2023-12-31'

#1. Download Historical Stock Price Data
stock_data = yf.download(tickers, start=start_date, end=end_date, group_by='tickers')

# Backup the data as a CSV file
stock_data.to_csv('movie_stocks.csv')

#2. Load and Preprocess Data
stock_data = pd.read_csv('movie_stocks.csv', header=[0, 1], index_col=0, parse_dates=True)
print(stock_data.head())

#3. Trend Analysis
plt.figure(figsize=(12, 6))
for ticker in tickers:
    stock_data[(ticker, 'Close')].plot(label=ticker)

plt.title('Stock Price Trends for Movie Industry Companies')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

#4. Volatility Analysis
returns = stock_data.xs('Close', axis=1, level=1).pct_change()
plt.figure(figsize=(12, 6))
returns.plot()
plt.title('Daily Returns of Movie Industry Companies')
plt.xlabel('Date')
plt.ylabel('Daily Return (%)')
plt.legend(tickers)
plt.grid(True)
plt.show()

#5. Correlation Analysis
correlation = returns.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Stock Correlation Between Movie Industry Companies')
plt.show()

#6. Moving Average Analysis for Disney (DIS)
stock_data[('DIS', '20_MA')] = stock_data[('DIS', 'Close')].rolling(window=20).mean()
stock_data[('DIS', '50_MA')] = stock_data[('DIS', 'Close')].rolling(window=50).mean()

plt.figure(figsize=(12, 6))
stock_data[('DIS', 'Close')].plot(label='Close Price')
stock_data[('DIS', '20_MA')].plot(label='20-Day Moving Average')
stock_data[('DIS', '50_MA')].plot(label='50-Day Moving Average')
plt.title('Moving Average Analysis for Disney (DIS)')
plt.xlabel('Date(Year)')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

#Analysis Summary
print('Analysis Summary:')
print('1. Stock price trends show how the companies performed over time.')
print('2. Volatility analysis reveals how sensitive the companies are to market fluctuations.')
print('3. Correlation analysis highlights relationships between companies, useful for diversification.')
print('4. Moving averages help identify short-term and long-term trends for Disney (DIS).')
