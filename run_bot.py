''' Specify real or test and the trading strategy at the command line (make sure this is easy to deploy
on AWS in this manner) '''

from TradingBot import *
import pandas as pd

def main():

    test_bot = TradingBot()
    ticker = "SPY"
    data = test_bot.get_historical_bar_data(ticker)
    df = pd.DataFrame.from_records(data)
    df.to_csv(f"./data/IBData/{ticker}.csv", index=False)

if __name__ == "__main__":

    main()