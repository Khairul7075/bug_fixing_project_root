import os
import datetime
import pandas as pd
from dotenv import load_dotenv
from scripts.utils import connect_google_sheet, fetch_stock_data

# Load environment variables
load_dotenv()
SHEET_URL = os.getenv("SHEET_URL")
PRICE_COLUMN = 4  # Example: Column GW for Live Price

def main():
    sheet = connect_google_sheet(SHEET_URL)
    tickers = sheet.col_values(2)[3:]  # Column B, skip headers

    for i, ticker in enumerate(tickers, start=4):
        try:
            if not ticker.strip():
                continue

            # Fetch stock data (latest daily interval)
            data = fetch_stock_data(ticker, period="5d", interval="1d")

            if data.empty or "Close" not in data.columns:
                log_message(f"No price data for {ticker}")
                continue

            latest_price = data["Close"].iloc[-1]
            if isinstance(latest_price, pd.Series):
                latest_price = latest_price.values[0]

            latest_price = float(latest_price) if pd.notna(latest_price) else None

            if latest_price is not None:
                sheet.update_cell(i, PRICE_COLUMN, round(latest_price, 2))
                log_message(f"Updated price for {ticker}: {latest_price}")
            else:
                log_message(f"Price not available for {ticker}")

        except Exception as e:
            log_message(f"Error fetching price for {ticker}: {e}")

def log_message(message):
    os.makedirs("logs", exist_ok=True)
    with open("logs/price_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

if __name__ == "__main__":
    main()
