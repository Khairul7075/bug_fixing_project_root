import os
from dotenv import load_dotenv
from scripts.utils import connect_google_sheet

# Load environment variables
load_dotenv()
SHEET_URL = os.getenv("SHEET_URL")

def test_connection():
    """Test connection to Google Sheet and print header row."""
    try:
        sheet = connect_google_sheet(SHEET_URL)
        header = sheet.row_values(3)
        print("Connection successful. Header row:", header)
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    test_connection()
