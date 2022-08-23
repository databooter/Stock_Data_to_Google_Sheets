class Category:
    """ Categories which are stocks grouped by a industry,
     they have a set timeframe, and a workbook - superclass """
    def __init__(self, industry, stocks, workbook):
        self.industry = industry
        self.stocks = stocks
        self.workbook = workbook

    def __str__(self):
        return f"Industry: {self.industry}\n" \
               f"Stocks: {self.stocks}\n" \
               f"Workbook: {self.workbook}"

    def set_industry(self, industry):
        """Set the category of the ticker symbol"""
        self.industry = industry
        print(f"Industry set to {self.industry} for {self.stocks}")

    def set_stocks(self, stocks):
        """Set the ticker symbols of the stocks"""
        self.stocks = stocks
        print(f"Ticker symbols set to {self.stocks}")

    def set_workbook(self, workbook):
        """Set the workbook to push data to"""
        self.workbook = workbook
        print(f"Workbook set to {self.workbook}")

    def push_to_gsheet(self):
        """Import Packages"""
        import gspread
        from gspread_dataframe import set_with_dataframe
        import pandas as pd
        import yfinance as yf
        from datetime import datetime
        from pandas_datareader import data
        import time
        from oauth2client.service_account import ServiceAccountCredentials

        """Pulling market cap data from yahoo and putting into caps_df dataframe"""
        time.sleep(10)
        caps = data.get_quote_yahoo(self.stocks)['marketCap']
        caps_df = pd.DataFrame(caps)

        """Pulling historical stock price data from yahoo and putting in str_data dataframe"""
        time.sleep(10)
        end = datetime.today().strftime('%Y-%m-%d')
        str_data = yf.download(self.stocks, start="2020-01-01", end=end, rounding=bool)
        time.sleep(10)

        """Defining scope"""
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        """Defining credentials"""
        creds = ServiceAccountCredentials.from_json_keyfile_name(r'../creds.json', scope)

        """Connecting to Google Sheets"""
        client = gspread.authorize(creds)

        """Opening specified workbook and defining worksheets"""
        sheet = client.open(self.workbook)
        ticker_data_worksheet = sheet.get_worksheet(7)
        market_caps_worksheet = sheet.get_worksheet(0)

        """Inserting caps_df into market_caps_worksheet"""
        set_with_dataframe(market_caps_worksheet,
                           caps_df,
                           include_index=True,
                           include_column_header=True,
                           allow_formulas=False,
                           row=40,
                           col=1)

        """Inserting str_data into ticker_data_worksheet"""
        set_with_dataframe(ticker_data_worksheet,
                           str_data,
                           include_index=True,
                           include_column_header=True,
                           allow_formulas=False)
        print("Ticker data upload complete")


