from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import finpy_tse as fpy
import pytse_client as tse
import yfinance as yf
import ta 
import asyncio


symbol_analyze="BTC-USD"


last_day =datetime.now()
last_day=last_day.date()
last_day=str(last_day)
last_day

print(last_day)



def yahoo_symbol(symbol="BTC-USD",timeframe='1d'):
    while True:
        try:
            data = yf.download(symbol,period='max',interval= timeframe)
            return(data)
        except Exception as e:
            print(f"An error occurred: {e}")
            asyncio.sleep(2)  # Sleep for 10 seconds before retrying



symbol_data=yahoo_symbol(symbol=symbol_analyze)
symbol_data

print(symbol_data)



symbol_data.plot()