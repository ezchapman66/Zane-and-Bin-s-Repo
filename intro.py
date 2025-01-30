import finnhub
import yfinance as yf
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
import requests

top_50_stocks = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "BRK.B", "META", "V", "JNJ",
    "PG", "UNH", "DIS", "HD", "MA", "PYPL", "NVDA", "VZ", "INTC", "NFLX",
    "AMD", "BA", "IBM", "NVDA", "CSCO", "WMT", "ORCL", "XOM", "CVX", "PFE",
    "PEP", "MRK", "ABT", "KO", "MCD", "GM", "BABA", "TWTR", "T", "GS",
    "COST", "SPGI", "CAT", "MO", "WFC", "AMT", "MS", "MDT", "UPS", "DE",
    "LMT", "GE", "NSC", "AIG", "AXP", "ZM", "SAP"
]



#this is stuff you can do with yfinance
# stocks = yf.Ticker("MSFT") #creates a Ticker object from its class
# stock_info = stocks.calendar #uses Ticker's calendar function to return a dictionary of data
# history = stocks.history(period='1y')
# print(history['Close'])
# print(stock_info) #this is a dictionary with analytical data
# print(stock_info["Earnings Average"], "\n") #this is how you iterate over a dictionary
# print(stocks.info) #this prints out info on the company that is the ticker

#this is stuff you can do with finnhub
finnhub_client = finnhub.Client(api_key="")

# print(finnhub_client.recommendation_trends("MSFT"))

#this is what you can do with the alpaca_trade_api
api_key = ""
secret_key = ""
base_url = ''

client = TradingClient(api_key, secret_key, paper=True)

account = client.get_account()

print(account.buying_power)

for stock in top_50_stocks:
    stock_reccomendation = finnhub_client.recommendation_trends(stock)
    if stock_reccomendation[0]["buy"] + stock_reccomendation[0]["strongBuy"] > stock_reccomendation[0]["sell"] + stock_reccomendation[0]["strongSell"]:

        client.submit_order()





