import pandas as pd
import pandas_ta as ta
from dataclasses import dataclass

@dataclass
class HistoricalDataIndicators:

    ''' Data class for manipulating and adding various techincal indicators to pre-downloaded historical data. Currently
    using TradingView API to download historical data for testing (script for this in TradingView repo) '''

    def __init__(self, df):

        self.df = df

    def MACD(self, slow, fast, signal):

        self.df.ta.macd(close='close', fast=fast, slow=slow, signal=signal, append=True)
        # new_fpath = self.fpath.replace(".csv", "_MACD.csv")
        # print(f"Saving to csv: {new_fpath}")
        # self.df.to_csv(new_fpath, index=False)
        return self.df