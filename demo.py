prices = [12, 13, 14, 15, 16]

prices.append("hello")
prices.extend([17, 18, 19])

prices[3] = "bye"

print(prices.index("hello"))
print(prices)
