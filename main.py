import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


tickers = ["AAPL", "MSFT", "AMZN", "META", "NVDA"]
data = yf.download(tickers, start="2020-01-01", end="2023-12-31")

close_prices = data["Close"]
close_prices.plot(figsize=(14, 7))
plt.title("Stock Closing Prices")
plt.xlabel("Data")
plt.ylabel("Price ($)")
plt.legend(tickers)
plt.grid(True)
plt.show()

returns = close_prices.pct_change()
summary = returns.describe()
print(summary)


def prepare_data(ticker):
    df = close_prices[[ticker]].dropna()
    df['Return'] = df[ticker].pct_change()
    df['Lag1'] = df['Return'].shift(1)
    df.dropna(inplace=True)
    return df


df = prepare_data('AAPL')
X = df[['Lag1']]
y = df['Return']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

plt.figure(figsize=(10, 6))
plt.plot(y_test.index, y_test, label='Actual Values')
plt.plot(y_test.index, predictions, label='Predictions', linestyle='--')
plt.title("Actual Values vs Predictions")
plt.xlabel("Date")
plt.ylabel("Return")
plt.legend()
plt.grid(True)
plt.show()
