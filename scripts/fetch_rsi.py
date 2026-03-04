import os
import datetime
from turtle import pd
from dotenv import load_dotenv
from scripts.utils import connect_google_sheet, calculate_rsi, fetch_stock_data

# Load environment variables
load_dotenv()
SHEET_URL = os.getenv("SHEET_URL")
RSI_COLUMN = 231  # Column GY

def main():
    sheet = connect_google_sheet(SHEET_URL)
    tickers = sheet.col_values(2)[1:]  # skip header row

    for i, ticker in enumerate(tickers, start=2):
        try:
            data = fetch_stock_data(ticker)
            rsi_value = calculate_rsi(data)
            if pd.isna(rsi_value):
                log_message(f"RSI not available for {ticker}")
            else:
                sheet.update_cell(i, RSI_COLUMN, round(rsi_value, 2))
                log_message(f"Updated RSI for {ticker}: {rsi_value}")

        except Exception as e:
            log_message(f"Error fetching RSI for {ticker}: {e}")

def log_message(message):
    os.makedirs("logs", exist_ok=True)
    with open("logs/run_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

if __name__ == "__main__":
    main()
