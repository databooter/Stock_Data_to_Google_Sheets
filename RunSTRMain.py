from str_data_pull import str_data_pull
from oauth2client.service_account import ServiceAccountCredentials

# Defining tickers:
stocks = ['EXPE', 'ABNB', 'BKNG', 'VCSA', 'SOND', 'ISPO']

# Defining scope:
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Defining credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("../creds.json", scope)

# Defining workbook:
workbook = "Short-term Rental Equity Data"

# Running str_data_pull
str_data_pull(stocks, creds, workbook)
