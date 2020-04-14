import alpaca_trade_api as tradeapi
import time

key = "<YOUR KEY HERE>"
sec = "<YOUR SECRET KEY HERE>"

#API endpoint URL
url = "https://paper-api.alpaca.markets"

#api_version v2 refers to the version that we'll use
#very important for the documentation
api = tradeapi.REST(key, sec, url, api_version='v2')

#Init our account var
account = api.get_account()

#Should print 'ACTIVE'
print(account.status)

#Place buy order:
#When placing orders, use the 'api' object we define above^
#api.submit_order() allows you to pass params to place orders
#Example buy order:

#All args in the submit_order() MUST BE STR!
#Symbol means the stock ticker (FB, AAPL, IBM)
#qty means quantity
#side means buy or sell
order = api.submit_order(symbol="FB",
                         qty="10",
                         side="buy",
                         type="limit",
                         limit_price="180.15",
                         time_in_force="day")

print(order)

time.sleep(3)

order1 = api.submit_order(symbol="FB",
                         qty="10",
                         side="sell",
                         type="limit",
                         limit_price="180.25",
                         time_in_force="day")

time.sleep(5)

print(order1)


