

##  Setup Instructions

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

3.Running RSI Script
Calculate RSI values and update them in Google Sheet:

python scripts/fetch_rsi.py

Ticker Source: Column B

RSI Destination: Column E (5)



Running Stock Price Script (Bug Fix) 
Ticker Source: Column B

Price Destination: Column D

Logs: logs/price_log.txt
---

##  Testing
- Connection Test:
   python -m  tests.test_connection.py

RSI Unit Test: 

python -m tests.test_rsi.py 




 

---

##  Project Structure
bug_fxing_project_root/
├── scripts/
│   ├── utils.py
│   ├── fetch_rsi.py
│   ├── fetch_prices.py
│   └── __init__.py
├── tests/
│   ├── test_rsi.py
│   └── test_connection.py
├── logs/
│   ├── run_log.txt
│   └── price_log.txt
├── requirements.txt
├── .env.example
└── README.md

