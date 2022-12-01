''' Use this script to backtest different strategies and log their results '''

from backtesting import Strategy
from strategies.SMA_crossover import SmaCross
from TechnicalDataIndicators import TechnicalIndicatorsFactory
from backtesting import Backtest
from backtesting.test import GOOG
import pandas as pd

def run_experiment(data_fpath: str, strategy: Strategy) -> pd.Series:

    # Read data from csv
    df = pd.read_csv(data_fpath)
    df.columns = [col.capitalize() for col in df.columns] # Backtest library requires capitalized column names

    # Call Backtest library
    # bt = Backtest(GOOG, SmaCross, cash=10_000, commission=.002)
    bt = Backtest(df, strategy, cash=10_000, commission=.002)
    # stats = bt.run()
    stats = bt.optimize(n1=range(5, 30, 5),
                    n2=range(10, 70, 5),
                    maximize='Equity Final [$]',
                    constraint=lambda param: param.n1 < param.n2)
    # bt.plot()

    return stats

def main():

    # Define strategy and data filepath
    strategy = SmaCross
    data_fpath = './data/TradingViewData/oil_futures.csv'
    
    # Run experiment
    stats = run_experiment(data_fpath, strategy)
    print(stats)
    print(stats._strategy)    

if __name__ == "__main__":

    main()
