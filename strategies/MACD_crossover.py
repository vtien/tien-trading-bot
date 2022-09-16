from HistoricalDataIndicators import HistoricalDataIndicators
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd

class MACD_Crossover(Strategy):

    def __init__(self, ma_slow: float, ma_fast: float, signal: float, data: pd.DataFrame):

        self.ma_slow = ma_slow
        self.ma_fast = ma_fast
        self.signal = signal
        self.hdi = HistoricalDataIndicators(data)
        self.data = self.hdi.MACD(slow=self.ma_slow, fast=self.ma_fast, signal = self.signal)

        # find columns associated with MACD (they will always be the last two)
        column_names = self.data.columns
        self.MACD1 = self.data[column_names[-2]]
        self.MACD2 = self.data[column_names[-1]]
        

    def next(self):

        # this is incorrect logic, look up a MACD trading strategy video
        if crossover(self.MACD1, self.MACD2):
            self.buy()
        elif crossover(self.MACD2, self.MACD1):
            self.sell()
