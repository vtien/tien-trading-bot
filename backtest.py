''' Use this script to backtest different strategies and log their results '''

from strategies.SMA_crossover import SmaCross
from TechnicalDataIndicators import TechnicalIndicatorsFactory
from backtesting import Backtest
from backtesting.test import GOOG

def run_experiment():

    # Define data
    hdi = TechnicalIndicatorsFactory(data_fpath='./data/TradingViewData/oil_futures.csv')
    df = hdi.MACD(12, 26, 9)
    df = df[['open', 'high', 'low', 'close', 'volume']]
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

    # Call Backtest library
    # bt = Backtest(GOOG, SmaCross, cash=10_000, commission=.002)
    bt = Backtest(df, SmaCross, cash=10_000, commission=.002)
    # stats = bt.run()
    stats = bt.optimize(n1=range(5, 30, 5),
                    n2=range(10, 70, 5),
                    maximize='Equity Final [$]',
                    constraint=lambda param: param.n1 < param.n2)
    # bt.plot()

    return stats

if __name__ == "__main__":

    stats = run_experiment()
    print(stats)
    print(stats._strategy)
