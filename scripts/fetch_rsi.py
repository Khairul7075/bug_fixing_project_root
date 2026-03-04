import os
import datetime
import pandas as pd
from dotenv import load_dotenv
from scripts.utils import connect_google_sheet, calculate_rsi, fetch_stock_data

# Load environment variables
load_dotenv()
SHEET_URL = os.getenv("SHEET_URL")
RSI_COLUMN = 5 # Column GY for RSI values

def main():
    # Connect to the sheet
    sheet = connect_google_sheet(SHEET_URL)

    # Get tickers from column B, skipping first 3 header rows
    tickers = sheet.col_values(2)[3:]

    # Loop through tickers starting at row 4
    for i, ticker in enumerate(tickers, start=4):
        try:
            # Skip empty cells
            if not ticker.strip():
                continue

            # Fetch stock data (daily interval, 1 month history)
            data = fetch_stock_data(ticker, period="1mo", interval="1d")

            # Calculate latest RSI value
            rsi_value = calculate_rsi(data)

            # Ensure RSI is a float, not a Series
            if rsi_value is None or isinstance(rsi_value, pd.Series):
                log_message(f"RSI not available for {ticker}")
            else:
                sheet.update_cell(i, RSI_COLUMN, round(float(rsi_value), 2))
                log_message(f"Updated RSI for {ticker}: {rsi_value}")

        except Exception as e:
            log_message(f"Error fetching RSI for {ticker}: {e}")

def log_message(message):
    os.makedirs("logs", exist_ok=True)
    with open("logs/run_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

if __name__ == "__main__":
    main()
