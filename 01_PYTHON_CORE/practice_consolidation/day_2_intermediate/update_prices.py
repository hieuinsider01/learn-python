# T.2 Phiên bản cơ bản
prices = {"NPK": 15000, "Urea": 12000, "Kali": 18000}
for new_price in prices:
  prices[new_price] *= 1.1
print(prices)

# T.2 Phiên bản refactor
def prices_update():
  prices = {"NPK": 15000, "Urea": 12000, "Kali": 18000}
  new_price = {key: value * 1.1 for key, value in prices.items()}
  return new_price

result = prices_update()

print(result)