from stock import StockLookup

API_KEY = "Enter Your API Key Here"

def main():
    Stock = StockLookup(API_KEY)
    print(Stock.lookup("AAPL", "2024-06-01"))
    print("Minimum price in last 5 days:", Stock.min_price("AAPL", 5))
    print("Maximum price in last 5 days:", Stock.max_price("AAPL", 5)) 

if __name__ == "__main__":
    main()