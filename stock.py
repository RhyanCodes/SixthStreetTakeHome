import requests 

class StockLookup:
    def __init__(self, api_key):
        self.api_key = api_key

    def lookup(self, ticker, date):
        
        data = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={self.api_key}")
        data = data.json()
        for days in data["Time Series (Daily)"].items():
        
            if days[0] == date:
                return (data["Time Series (Daily)"][days[0]])
   
    def min_price(self,ticker, n):
        
        data = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={self.api_key}")
        data = data.json()
        res = float('inf')
        daily_data = list(data["Time Series (Daily)"].items())
        for day in daily_data[:n]:
            res = min(res, float(day[1]["3. low"]))
        return round(res, 4)

    def max_price(self, ticker, n):
        data = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={self.api_key}")
        data = data.json()
        res = float('-inf')
        daily_data = list(data["Time Series (Daily)"].items())
        for day in daily_data[:n]:
            res = max(res, float(day[1]["2. high"]))
        return round(res, 4)

