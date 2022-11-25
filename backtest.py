''' Use this script to backtest different strategies and log their results '''

from strategies.SMA_crossover import SmaCross
from TechnicalDataIndicators import TechnicalIndicatorsFactory
from backtesting import Backtest
from backtesting.test import GOOG

def run_experiment():

    # Define data
    hdi = TechnicalIndicatorsFactory(data_fpath='./data/TradingViewData/oil_futures.csv')
    df = hdi.MACD(12, 26, 9)

    # Call Backtest library
    bt = Backtest(GOOG, SmaCross, cash=10_000, commission=.002)
    stats = bt.run()
    bt.plot()

    return stats

if __name__ == "__main__":

    stats = run_experiment()
    print(stats)
