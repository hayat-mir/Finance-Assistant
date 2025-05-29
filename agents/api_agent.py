import time
import yfinance as yf
from datetime import date, timedelta
from yfinance.exceptions import YFRateLimitError

def get_stock_summary(tickers):
    """
    MOCK: Returns fake data for testing without hitting Yahoo API.
    """
    summary = {
        "TSM": {
            "yesterday_close": 120.5,
            "today_close": 122.3,
            "change_pct": 1.49
        },
        "005930.KQ": {
            "yesterday_close": 60.1,
            "today_close": 59.3,
            "change_pct": -1.33
        }
    }

    return {ticker: summary.get(ticker, {}) for ticker in tickers}
