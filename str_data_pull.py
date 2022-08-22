import gspread
from gspread_dataframe import set_with_dataframe
import pandas as pd
import yfinance as yf
from datetime import datetime
from pandas_datareader import data
import time


def str_data_pull(stocks, creds, workbook):

    # Pulling market cap data from yahoo and putting into caps_df dataframe
    time.sleep(10)
    caps = data.get_quote_yahoo(stocks)['marketCap']
    time.sleep(20)
    caps_df = pd.DataFrame(caps)
    time.sleep(10)

    # Pulling historical stock price data from yahoo and putting in str_data dataframe
    time.sleep(10)
    end = datetime.today().strftime('%Y-%m-%d')
    str_data = yf.download(stocks, start="2020-01-01", end=end, rounding=bool)
    time.sleep(10)

    # Connecting to Google Sheets
    client = gspread.authorize(creds)

    # Opening specified workbook and defining worksheets
    sheet = client.open(workbook)
    ticker_data_worksheet = sheet.get_worksheet(7)
    market_caps_worksheet = sheet.get_worksheet(0)

    # Inserting caps_df into market_caps_worksheet
    set_with_dataframe(market_caps_worksheet,
                       caps_df,
                       include_index=True,
                       include_column_header=True,
                       allow_formulas=False,
                       row=40,
                       col=1)


    # Inserting str_data into ticker_data_worksheet
    set_with_dataframe(ticker_data_worksheet,
                       str_data,
                       include_index=True,
                       include_column_header=True,
                       allow_formulas=False)
    print("Ticker data upload complete")


