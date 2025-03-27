import quandl
import os

import pandas as pd
import numpy as np
import yfinance as yf

from loguru import logger

df_yahoo = yf.download(
    ["AAPL", "MSFT", "GOGL"],
    start="2000-01-01",
    end="2010-12-31",
    progress=True,
    actions="inline",
)

# Take a peek
logger.info(df_yahoo.head(1))

# Using Qunadl API

QUANDL_KEY = os.getenv("quandl_key")
quandl.ApiConfig.api_key = QUANDL_KEY

df_quandl = quandl.get(
    dataset="WIKI/AAPL", start_date="2000-01-01", end_date="2010-12-31"
)

logger.info(df_quandl.head(3))
