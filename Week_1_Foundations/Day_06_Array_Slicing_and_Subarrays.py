# Problems: Slice time-series stock prices.
# Learning Objective: Slicing rules, views vs copies.

import numpy as np

# Stock Prices array setup
stock_prices = np.array([120.5, 121.0, 119.8, 122.3, 123.5, 124.0, 123.2, 125.1, 126.4, 127.0])

# Extracting prices from day 3 to day 8
print(stock_prices[2:8])

# Extracting every 2nd day
print(stock_prices[::2])

# Extracting every 3nd day
print(stock_prices[::3])

# Extracting the last 5 days
print(stock_prices[-5::])

# Reverse the price series
print(stock_prices[-1:0:-1])

# Storing a slice into a new variable
first_3_days = stock_prices[0:3]
first_3_days[0] = 999.0

print(stock_prices)
print(first_3_days) # Original array changes

first_3_days_copy = stock_prices[0:3].copy()
first_3_days_copy[0] = 888.0

print(first_3_days_copy)
print(stock_prices)