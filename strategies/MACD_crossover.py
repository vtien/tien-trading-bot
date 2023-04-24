from TechnicalDataIndicators import TechnicalIndicatorsFactory
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd

def MACD(values, slow, fast, signal):

    df = pd.DataFrame(values)
    tdi = TechnicalIndicatorsFactory(df)
    return tdi.MACD(slow, fast, signal)

class MACDCross(Strategy):

    ma_fast: float = 12
    ma_slow: float = 26
    signal: float = 9

    def init(self):

        self.macd_data = self.I(MACD, self.data.Close, self.ma_slow, self.ma_fast, self.signal)

        # select columns associated with MACD (they will always be the last two)
        self.MACD1 = self.macd_data[-2]
        self.MACD2 = self.macd_data[-1]

    def next(self):

        # this is incorrect logic, look up a MACD trading strategy video
        if crossover(self.MACD1, self.MACD2):
            self.buy()
        elif crossover(self.MACD2, self.MACD1):
            self.sell()
