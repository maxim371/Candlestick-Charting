import requests, json, csv
from datetime import datetime

ALPACA_API_KEY = "R2QmmTkyUCVHirNLLz56DMCWEwZ9h1WdY3QRQhAZ"
TICKER = 'AAPL'
START_DATE = '2020-01-01'
END_DATE = '2020_12_27'
POLYGON_URL = 'https://api.polygon.io/v2/aggs/ticker/{}/range/1/day/{}/{}?apiKey={}'

r = requests.get(POLYGON_URL.format(TICKER, START_DATE, END_DATE, ALPACA_API_KEY))

data = json.loads(r.content)

print("date, open, high, low, close")
print(data)

for item in data['results']:
    formatted_date = datetime.fromtimestamp(item['t'] / 1000)
    date_only = formatted_date.strftime('%Y-%m-%d')

    print("{}.{},{},{},{}".format(date_only, item['o'], item['h'], item['l'], item['c']))