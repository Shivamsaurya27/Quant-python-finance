# Question 3
# Write a Python program that finds:
# maximum price
# minimum price
# average price
# From the list:
prices = [100, 102, 101, 103, 105]
# Do not use NumPy.

print(f"Maximum price is: {max(prices)}")
print(f"Minimum price is: {min(prices)}")

avg = 0
for i in range(len(prices)):
    avg += prices[i]

average = avg/len(prices)
print(f"The average price is: {average}")
