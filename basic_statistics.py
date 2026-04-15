"""
Basic statistical analysis for financial data
Author: Matteo Bianchini
Course: Finance - University of Parma (UNIPR)
"""

import statistics

# Example dataset: daily returns in percentage
daily_returns = [0.5, -0.2, 0.3, 1.1, -0.4, 0.0, 0.8]

mean_return = statistics.mean(daily_returns)
volatility = statistics.stdev(daily_returns)

print("Mean daily return:", mean_return, "%")
print("Volatility (standard deviation):", volatility)
