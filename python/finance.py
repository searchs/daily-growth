import pandas as pd
import numpy as np
import yfinance as yf

df_yahoo = yf.download(['AAPL', 'MSFT', 'GOGL'],
                    start='2000-01-01',
                    end='2010-12-31',
                    progress=True,
                    actions='inline')

# Take a peek
print(df_yahoo.head(1))

# Using Qunadl API
import quandl
import os

QUANDL_KEY = os.getenv('quandl_key')
quandl.ApiConfig.api_key = QUANDL_KEY

df_quandl = quandl.get(dataset='WIKI/AAPL',
                        start_date='2000-01-01',
                        end_date='2010-12-31')

print(df_quandl.head(3))