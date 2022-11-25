import pandas as pd
import pandas_ta as ta
from dataclasses import dataclass

@dataclass
class TechnicalIndicatorsFactory:

    ''' Data class for manipulating and adding various techincal indicators to pre-downloaded historical data. Currently
    using TradingView API to download historical data for testing (script for this in TradingView repo) '''

    def __init__(self, data_fpath: str):

        self.df = pd.read_csv(data_fpath)

    def MACD(self, slow: int, fast: int, signal: int):

        self.df.ta.macd(close='close', fast=fast, slow=slow, signal=signal, append=True)
        # new_fpath = self.fpath.replace(".csv", "_MACD.csv")
        # print(f"Saving to csv: {new_fpath}")
        # self.df.to_csv(new_fpath, index=False)
        return self.df