import pandas as pd

prices = [100,102,101,103,105]

returns = []

for i in range(len(prices)-1):
    r = (prices[i+1] - prices[i]) / prices[i]
    returns.append(r)

print(returns)
