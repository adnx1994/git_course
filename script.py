from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import finpy_tse as fpy
import pytse_client as tse
import yfinance as yf
import ta 


last_day =datetime.now()
last_day=last_day.date()
last_day=str(last_day)
last_day