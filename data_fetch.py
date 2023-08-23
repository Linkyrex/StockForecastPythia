import yfinance as yf

def get_data(stock, start_date, end_date):
    # Fetch data for a specific stock
    data = yf.download(stock, start_date, end_date)
    return data