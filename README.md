# Future Stock

This project leverages historical stock price data to allow users to analyze market trends and predict future price changes.

## Overview

The system performs the following tasks:
- **Data Collection:** Retrieves historical stock price data using `yfinance`.
- **Data Processing:** Processes the raw data and calculates percentage changes.
- **Modeling:** Uses `scikit-learn` to apply linear regression for predicting future stock prices.
- **Visualization:** Displays results through charts using `matplotlib`.

## Libraries and Tools Used

- **yfinance:** For retrieving historical stock price data.
- **matplotlib:** For visualizing stock price trends and prediction results.
- **scikit-learn:** For applying linear regression to make predictions.

## How It Works

1. **Data Collection:** 
   - The system collects historical stock prices from specified companies.
2. **Data Processing:** 
   - The data is processed to calculate daily returns and prepare the dataset for modeling.
3. **Modeling:** 
   - Linear regression is applied to predict future stock price movements based on historical trends.
4. **Visualization:** 
   - The actual and predicted stock prices are displayed in charts for easy comparison.
