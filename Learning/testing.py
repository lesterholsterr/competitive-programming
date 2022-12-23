# s = "hello"
# for i in range(len(s) - 1, -1, -1):
#   print(i)

class Stock:
  def __init__(self, ticker, price):
    self.ticker = ticker
    self.price = price
  def __str__(self):
    return f"{self.ticker}: ${self.price}"
  def quote(self):
    print(self.ticker, " is at $", self.price, sep='')

apple_stock = Stock("AAPL", 130)
print(apple_stock)

apple_stock.price = 140
print(apple_stock.price)

apple_stock.quote()
# del apple_stock.ticker
