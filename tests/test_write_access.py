import os
from dotenv import load_dotenv
from scripts.utils import connect_google_sheet

load_dotenv()
SHEET_URL = os.getenv("SHEET_URL")

def test_write_access():
    try:
        sheet = connect_google_sheet(SHEET_URL, sheet_name="Sheet1")
        sheet.update_acell("A1", "Access OK")
        print("Write test successful: 'Access OK' written to A1")
        print("Read back:", sheet.acell("A1").value)
    except Exception as e:
        print("Write test failed:", e)

if __name__ == "__main__":
    test_write_access()
