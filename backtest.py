''' Use this script to backtest different strategies and log their results '''

from strategies import *
from os import listdir
from os.path import isfile, join
from HistoricalDataIndicators import HistoricalDataIndicators
from typing import Callable

def read_data():

    hdi = HistoricalDataIndicators(fpath='./TradingViewData/oil_futures.csv')
    df = hdi.MACD()
    df.to_csv()

    return df

def backtest(strategy: Callable):
    
    # define backtesting implementation

    # log results to a text file for the given strategy
    return

if __name__ == "__main__":

    df = read_data()
    print(df)

    # get the name of all functions in strategy directory
    # strategies = [f for f in listdir("./strategies") if isfile(join("./strategies", f))]
    # for strategy in strategies:
    #     backtest(strategy)
