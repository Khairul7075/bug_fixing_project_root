

## 🔧 Setup Instructions

1. Clone the repository:
   git clone https://github.com/Khairul7075/bug_fxing project_root.git
   cd bug_fxing project_root

2. Install dependencies:
   pip install -r requirements.txt

3. Configure environment variables:
   - Create a `.env` file in the project root:
     SHEET_URL=https://docs.google.com/spreadsheets/d/your-sheet-id/edit#gid=0
     GOOGLE_APPLICATION_CREDENTIALS=credentials.json
   - Keep `credentials.json` only on your machine (do not commit it).
   - 

---

## 📈 Running RSI Script
Calculate RSI values and update them in Google Sheet:
   python scripts/fetch_rsi.py

Updates column **GY (231)** with RSI values for each ticker.

---

## 💹 Running Stock Price Script (Bug Fix)
Fetch live stock prices dynamically from Yahoo Finance:
   python scripts/fetch_prices.py

- Ticker Source: Column B  
- Price Destination: Column C  
- Logs: `logs/run_log.txt`

This replaces the old API/scraping code and ensures dynamic prices.

---

## 🧪 Testing
- Connection Test:
   python test_connection.py

- RSI Unit Test:
   pytest tests/test_rsi.py

---

## 📂 Project Structure
bug_fixing_project_root/
├── scripts/
│   ├── utils.py
│   ├── fetch_rsi.py
│   ├── fetch_prices.py
│   └── __init__.py
├── tests/
│   ├── test_rsi.py
│   └── test_connection.py
├── logs/
│   └── run_log.txt
├── requirements.txt
├── .env.example
└── README.md
