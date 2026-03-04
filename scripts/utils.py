import os
import pandas as pd
import yfinance as yf
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def connect_google_sheet(sheet_url, sheet_name="Sheet1"):
    """
    Connect to a Google Sheet using service account credentials.
    Args:
        sheet_url (str): Full URL of the Google Sheet.
        sheet_name (str): Name of the worksheet/tab to connect to.
    Returns:
        gspread.Worksheet: Worksheet object for interacting with the sheet.
    """
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not creds_path or not os.path.exists(creds_path):
        raise FileNotFoundError(f"Credentials file not found: {creds_path}")

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open_by_url(sheet_url)
    return spreadsheet.worksheet(sheet_name)


def calculate_rsi(data, period=14):
    if "Close" not in data.columns or data.empty:
        return None

    delta = data["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    if rsi.empty:
        return None

    latest_rsi = rsi.iloc[-1]

    # If latest_rsi is a Series, extract the first element
    if isinstance(latest_rsi, pd.Series):
        latest_rsi = latest_rsi.values[0]

    return float(latest_rsi) if pd.notna(latest_rsi) else None

def fetch_stock_data(ticker, period="1mo", interval="1d"):
    """
    Fetch stock data from Yahoo Finance.
    Args:
        ticker (str): Stock symbol (e.g., "MSFT").
        period (str): Data period (e.g., "1d", "5d", "1mo", "6mo", "1y").
        interval (str): Data interval (e.g., "1m", "5m", "15m", "1h", "1d").
    Returns:
        pd.DataFrame: Historical stock data with columns like 'Open', 'High', 'Low', 'Close', 'Volume'.
    """
    try:
        data = yf.download(ticker, period=period, interval=interval, progress=False)
        if data.empty:
            raise ValueError(f"No data returned for ticker {ticker}")
        return data
    except Exception as e:
        raise RuntimeError(f"Error fetching data for {ticker}: {e}")
