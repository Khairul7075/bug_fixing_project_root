import os
import datetime
from dotenv import load_dotenv
from scripts.utils import connect_google_sheet, fetch_stock_data

# Load environment variables
load_dotenv()

if not SHEET_URL:
    raise ValueError("SHEET_URL not found in .env")
if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not set in .env")


SHEET_URL = os.getenv("SHEET_URL")

PRICE_COLUMN = 3  # Example: column C for prices

def main():
    sheet = connect_google_sheet(SHEET_URL)
    tickers = sheet.col_values(2)[1:]  # Column B for tickers, skip header

    for i, ticker in enumerate(tickers, start=2):
        try:
            data = fetch_stock_data(ticker, period="1d")
            price = data["Close"].iloc[-1]
            sheet.update_cell(i, PRICE_COLUMN, round(price, 2))
            log_message(f"Updated {ticker} price: {price}")
        except Exception as e:
            log_message(f"Error updating {ticker}: {e}")

def log_message(message):
    os.makedirs("logs", exist_ok=True)
    with open("logs/run_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

if __name__ == "__main__":
    main()
