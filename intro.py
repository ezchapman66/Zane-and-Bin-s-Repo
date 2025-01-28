import yfinance as yf

stocks = yf.Ticker("MSFT") #creates a Ticker object from its class
stock_info = stocks.calendar #uses Ticker's calendar function to return a dictionary of data
print(stock_info) #this is a dictionary with analytical data
print(stock_info["Earnings Average"], "\n") #this is how you iterate over a dictionary
print(stocks.info)