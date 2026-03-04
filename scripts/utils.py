import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_google_sheet(sheet_url, sheet_name="Sheet1"):
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not os.path.exists(creds_path):
        raise FileNotFoundError(f"Credentials file not found: {creds_path}")

    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open_by_url(sheet_url)
    return spreadsheet.worksheet(sheet_name)  # choose tab by name
